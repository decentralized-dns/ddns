from pyteal import *
from beaker import *
from typing import Final
# from . import constants
from datetime import datetime
from algosdk.encoding import decode_address
from typing import Literal
import base64
from nacl.signing import SigningKey
from algosdk.atomic_transaction_composer import (
    AtomicTransactionComposer,
    TransactionWithSigner,
)
from algosdk import transaction

# Create a class, subclassing Application from beaker
class dot_somedao_registry(Application):
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
        return self.initialize_application_state()

    @opt_in
    def opt_in(self):
        return self.initialize_account_state()
    
    @external
    def register(self, 
                 name: abi.String,
                 owner: abi.String,
                 valid_year: abi.Uint64,
                 current_time: abi.Uint64
                ):
        
        expiry = current_time.get() + valid_year.get() * Int(86400) * Int(356)
        return Seq(
            self.dns_name.set(name.get()),
            self.dns_owner.set(owner.get()),
            self.dns_expiry.set(expiry)
        )
    
    @external
    def renew(self, renew_year: abi.Uint64):
        new_expiry = self.dns_expiry.get() + renew_year.get() * Int(86400) * Int(356)
        return self.dns_expiry.set(new_expiry)
    
    @external
    def update(self, social_account: abi.String):
        return self.dns_social.set(social_account.get())
    
class logicAccount(Application):
    class SigChecker(LogicSignature):
        user_addr = TemplateVariable(stack_type=TealType.bytes)
        def evaluate(self):
            return Seq(
                Int(1)
            )
    sig_checker = LSigPrecompile(SigChecker())
    @external
    def check(self, signer_address: abi.Address, msg: abi.String):
        return Assert(
            Txn.sender() == self.sig_checker.logic.template_hash(signer_address.get())
        )
    
# ------------------------------------------------------------------------------------    
# Input from front end
name = "Yanbang"
valid_year = 5
current_time = int(datetime.now().timestamp())
renew_year = 1
social_account = "1234567"

# Create an Application client
account = sandbox.get_accounts().pop()
print("new account created:\n", account)

logic_app = logicAccount()
logic_app_client = client.ApplicationClient(
    sandbox.get_algod_client(), 
    logic_app, 
    signer=account.signer
)
app_id, app_addr, txid = logic_app_client.create()
print(
    f"""Deployed logic signature in
    txid: {txid}
    App ID: {app_id} 
    Address: {app_addr} 
    """
)

lsig_signer = logic_app.sig_checker.template_signer(decode_address(account.address))
lsig_client = logic_app_client.prepare(signer=lsig_signer)
print("logic client: \n", lsig_client)
print("")

app_client = client.ApplicationClient(
    client=sandbox.get_algod_client(),
    app=dot_somedao_registry(version=8),
    signer=account.signer,
)
# Deploy the app on-chain
app_id_sc, app_addr_sc, txid_sc = app_client.create()
print(
    f"""Deployed app in
    txid: {txid_sc}
    App ID: {app_id_sc} 
    Address: {app_addr_sc} 
    """
)

# make the log sig opt-in to Smart Contract
app_client.prepare(signer=lsig_signer)
app_client.opt_in()
#---------------------

def sign_msg(msg: str, sk: str) -> bytes:
    """utility function for signing arbitrary data"""
    pk: list[int] = list(base64.b64decode(sk))
    return SigningKey(bytes(pk[:32])).sign(msg.encode()).signature

sig = sign_msg("hi this is msg", account.signer.private_key)
atc = AtomicTransactionComposer()
atc.add_transaction(
        TransactionWithSigner(
            txn=transaction.PaymentTxn(account.address,
                                       app_client.client.suggested_params(),
                                       app_addr_sc,
                                       0),
            signer=account.signer,
        )
    )


lsig_client.add_method_call(
    atc,
    logic_app.check,
    suggested_params=lsig_client.client.suggested_params(),
    signer_address=account.address,# not share
    msg="hi this is msg",
    sig=sig,
)

# run it
result = atc.execute(app_client.client, 4)
print(f"Confirmed in round {result.confirmed_round}")
#----------------------
# Call and test method
print("test 1 - Register")
result = app_client.call(dot_somedao_registry.register, 
                         name=name, 
                         owner=account.address,
                         valid_year=valid_year,
                         current_time=current_time
                         )
print(result.return_value) 
# Print the current account state
print(f"Current account state: {app_client.get_account_state()}")

print("test 2 - Renew")
result = app_client.call(dot_somedao_registry.renew,
                         renew_year = renew_year
                         )
print(result.return_value) 
# Print the current account state
print(f"Current account state: {app_client.get_account_state()}")

print("test 3 - Update social accnt")
result = app_client.call(dot_somedao_registry.update,
                         social_account = social_account
                         )
print(result.return_value) 
# Print the current account state
print(f"Current account state: {app_client.get_account_state()}")
