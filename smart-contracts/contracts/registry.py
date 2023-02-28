# from . import constants
from datetime import datetime
from typing import Final, Literal

from beaker import (AccountStateValue, Approve, LogicSignature,
                    TemplateVariable, sandbox)
from beaker.application import Application
from beaker.client import ApplicationClient
from beaker.decorators import create, external, opt_in
from beaker.precompile import LSigPrecompile
from pyteal import (Assert, AtomicTransactionComposer, Bytes,
                    Ed25519Verify_Bare, Int, Seq, TealType, Txn, abi)
from utils import sign_msg

Signature = abi.StaticBytes[Literal[64]]

# Create a class, subclassing Application from beaker
class Registry(Application):
    class SigChecker(LogicSignature):
        """Simple program to check an ed25519 signature given a message and signature"""
        user_addr = TemplateVariable(stack_type=TealType.bytes)

        def evaluate(self):
            return Seq(
                # Borrow the msg and sig from the abi call arguments
                # TODO: this kinda stinks, what do?
                (msg := abi.String()).decode(Txn.application_args[2]),
                (sig := abi.make(Signature)).decode(Txn.application_args[3]),
                # Assert that the sig matches
                Assert(Ed25519Verify_Bare(msg.get(), sig.get(), self.user_addr)),
                Int(1),
            )

    sig_checker = LSigPrecompile(SigChecker())
    @external
    def check(self, signer_address: abi.Address):
        return Assert(
            Txn.sender() == self.sig_checker.logic.template_hash(signer_address.get())
        )


    dns_owner: Final[AccountStateValue] = AccountStateValue(
        stack_type=TealType.bytes,
        default=Bytes(""),
        descr="dns name owner address",
    )

    dns_name: Final[AccountStateValue] = AccountStateValue(
        stack_type=TealType.bytes,
        default=Bytes(""),
        descr="dns name",
    )

    dns_expiry: Final[AccountStateValue] = AccountStateValue(
        stack_type=TealType.uint64,
        descr="dns expiry time",
    )

    dns_social: Final[AccountStateValue] = AccountStateValue(
        stack_type=TealType.bytes,
        default=Bytes(""),
        descr="dns social binded account - Pokemon Go",
    )

    @create
    def create(self):
        """Deploys the contract and intialize app states"""
        return self.initialize_application_state()

    @opt_in
    def opt_in(self):
        # Defaults to sender
        return self.initialize_account_state()

    @external
    def health(self, *, output: abi.String):
        """Returns the contract health"""
        return output.set(Bytes("Registry is up and running!"))

    @external
    def register(
        self,
        name: abi.String,
        owner: abi.String,
        valid_year: abi.Uint64,
        current_time: abi.Uint64,
    ):
        """Register a new DNS name"""
        expiry = current_time.get() + valid_year.get() * Int(86400) * Int(356)
        return Seq(
            self.dns_name.set(name.get()),
            self.dns_owner.set(owner.get()),
            self.dns_expiry.set(expiry),
        )

    @external
    def renew(self, renew_year: abi.Uint64):
        """Renew a new DNS name"""
        new_expiry = self.dns_expiry.get() + renew_year.get() * Int(86400) * Int(356)
        return self.dns_expiry.set(new_expiry)

    @external
    def update(self, social_account: abi.String):
        """Update a new DNS name"""
        return self.dns_social.set(social_account.get())


def demo():
    # Test data setup
    name = "Yanbang"
    valid_year = 5
    current_time = int(datetime.now().timestamp())
    renew_year = 1
    social_account = "1234567"

    client = sandbox.get_algod_client()
    account = sandbox.get_accounts().pop()
    print("new account created:\n", account)

    # Create an Application client
    app_client = ApplicationClient(
        client,
        app=Registry(version=8),
        signer=account.signer,
    )

    # Deploy dapp
    app_id_sc, app_addr_sc, txid_sc = app_client.create()
    print(
        f"""Deployed app in
        txid: {txid_sc}
        App ID: {app_id_sc}
        Address: {app_addr_sc}
        """
    )

    app_client.opt_in()

    # Get the signer for the lsig from its populated precompile
    lsig_signer = app_client.sig_checker.template_signer(decode_address(acct.address))
    # Prepare a new client so it can sign calls
    lsig_client = app_client.prepare(signer=lsig_signer)

    atc = AtomicTransactionComposer()

    # Call and test method
    print("test 1 - Register")
    result = app_client.call(
        Registry.register,
        name=name,
        owner=account.address,
        valid_year=valid_year,
        current_time=current_time,
    )
    print(result.return_value)  # return None or add output in the smart contract func
    # Print the current account state
    print(f"Current account state: {app_client.get_account_state()}")

    print("test 2 - Renew")
    result = app_client.call(Registry.renew, renew_year=renew_year)
    print(result.return_value)
    # Print the current account state
    print(f"Current account state: {app_client.get_account_state()}")

    print("test 3 - Update social accnt")
    result = app_client.call(Registry.update, social_account=social_account)
    print(result.return_value)
    # Print the current account state
    print(f"Current account state: {app_client.get_account_state()}")


if __name__ == "__main__":
    registry = Registry()
    demo()
