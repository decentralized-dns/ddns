# sandbox setup

```
$ ./sandbox status

algod - goal node status
Last committed block: 392
Time since last block: 19237.3s
Sync Time: 0.0s
Last consensus protocol: https://github.com/algorandfoundation/specs/tree/44fa607d6051730f5264526bf3c108d51f0eadb6
Next consensus protocol: https://github.com/algorandfoundation/specs/tree/44fa607d6051730f5264526bf3c108d51f0eadb6
Round for next consensus protocol: 393
Next consensus protocol supported: true
Last Catchpoint:
Genesis ID: sandnet-v1
Genesis hash: Ru33QvL2WGFUeBPer9lUWp04wj8F3MosHz/Go7MyFes=

indexer - health
{
  "data": {
    "migration-required": false,
    "migration-status": "Migrations Complete"
  },
  "db-available": true,
  "errors": [
    "fetcher error: HTTP 404: {\"message\":\"failed to retrieve information from the ledger\"}\n"
  ],
  "is-migrating": false,
  "message": "392",
  "round": 392,
  "version": "(unknown version)"
}
```

# testnet setup

```
$ ./sandbox up testnet

Starting sandbox for: testnet
Sandbox was already started for 'dev'.
Would you like to reset the local sandbox with 'testnet'? [Y/n] y

Cleaning up sandbox environment...

Starting sandbox for: testnet
see sandbox.log for detailed progress, or use -v.
* docker containers started!
* waiting for services to initialize.
* services ready!

algod version
12885819394
3.14.2.stable [rel/stable] (commit #8fd6e702)
go-algorand is licensed with AGPLv3.0
source code available at https://github.com/algorand/go-algorand

Indexer version
Indexer disabled for this configuration.

Postgres version
postgres (PostgreSQL) 13.10

algod - goal node status
Last committed block: 47
Time since last block: 0.0s
Sync Time: 2.2s
Last consensus protocol: https://github.com/algorand/spec/tree/a26ed78ed8f834e2b9ccb6eb7d3ee9f629a6e622
Next consensus protocol: https://github.com/algorand/spec/tree/a26ed78ed8f834e2b9ccb6eb7d3ee9f629a6e622
Round for next consensus protocol: 48
Next consensus protocol supported: true
Last Catchpoint:
Consensus upgrate state: Voting
Yes votes: 47
No votes: 18446744073709551615
Votes remaining: 9954
Yes votes required: 9000
Vote window close round: 10001
Genesis ID: testnet-v1.0
Genesis hash: SGO1GKSzyE7IEPItTxCByw9x8FmnrCDexi9/cOUJOiI=

indexer - health
Indexer disabled for this configuration.

Starting fast-catchup with catchpoint: 28010000#DJGSAW476PZRTWEAQYDHNHLAHYTVFQBGZTO54X6GUY4GYJFD4G2Q
...
Fast-catchup complete! Printing status...

algod - goal node status
Last committed block: 82
Sync Time: 274.7s
Catchpoint: 28010000#DJGSAW476PZRTWEAQYDHNHLAHYTVFQBGZTO54X6GUY4GYJFD4G2Q
Catchpoint total accounts: 1845635
Catchpoint accounts processed: 1845635
Catchpoint accounts verified: 1845635
Catchpoint total KVs: 81493
Catchpoint KVs processed: 81493
Catchpoint KVs verified: 81493
Catchpoint total blocks: 1321
Catchpoint downloaded blocks: 1321
Genesis ID: testnet-v1.0
Genesis hash: SGO1GKSzyE7IEPItTxCByw9x8FmnrCDexi9/cOUJOiI=

indexer - health
Indexer disabled for this configuration.
```
