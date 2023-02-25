from beaker import sandbox

client = sandbox.get_algod_client()
accounts = sandbox.get_accounts()

for account in accounts:
    pk = account.address
    account_info = client.account_info(pk)
    balance = account_info.get("amount")
    print(f"Account balance {pk[:5]}...{pk[-5:]}: {balance:,.0f} microAlgos")
