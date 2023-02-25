from pyteal import *
from beaker import *

# Create a class, subclassing Application from beaker
class DDNS(Application):
    # Add an external method with ABI method signature `ping(string)string`
    @external
    def ping(self, name: abi.String, *, output: abi.String):
        return output.set(Concat(Bytes("ping, "), name.get()))


def main():
    app_client = client.ApplicationClient(
        client=sandbox.get_algod_client(),
        app=DDNS(version=8),
        signer=sandbox.get_accounts().pop().signer,
    )

    app_id, app_addr, txid = app_client.create()
    print(
        f"""Deployed app in txid {txid}
        App ID: {app_id}
        Address: {app_addr}
    """
    )

    result = app_client.call(DDNS.ping, name="ddnsbot")
    print(result.return_value)  # "Hello, Beaker"


if __name__ == "__main__":
    main()
