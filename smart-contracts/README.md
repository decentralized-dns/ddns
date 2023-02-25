# smart_contracts test <!-- omit in toc -->

- [Setup sandbox](#setup-sandbox)
  - [demo](#demo)
  - [Check with dappflow](#check-with-dappflow)
  - [Demo (deploy dapp)](#demo-deploy-dapp)
- [Setup](#setup)
- [Local run](#local-run)

## Setup sandbox

```sh
git clone https://github.com/algorand/sandbox.git
cd sandbox
# assuming docker and docker-compose have been setup
./sandbox up dev -v
# after the sandbox is up
./sandbox goal account list # sanity check
```

```sh
$ docker ps
CONTAINER ID   IMAGE                COMMAND                  CREATED       STATUS             PORTS                                                                                                      NAMES
86ecc16dc0ce   sandbox-indexer      "/tmp/start.sh"          10 days ago   Up About an hour   0.0.0.0:8980->8980/tcp, :::8980->8980/tcp                                                                  algorand-sandbox-indexer
a4439ecdc815   postgres:13-alpine   "docker-entrypoint.s…"   10 days ago   Up About an hour   0.0.0.0:5433->5432/tcp, :::5433->5432/tcp                                                                  algorand-sandbox-postgres
3c10e7e5e85e   sandbox-algod        "/opt/start_algod.sh"    10 days ago   Up About an hour   0.0.0.0:4001-4002->4001-4002/tcp, :::4001-4002->4001-4002/tcp, 0.0.0.0:9392->9392/tcp, :::9392->9392/tcp   algorand-sandbox-algod
```

### demo

```sh
$ ./sandbox goal account list
[online]	YBHNJCX6LJNS73YKDEXTZVS24WDF53DHJ5N2DKZEK4LGWJG6KMSV7QFJUU	YBHNJCX6LJNS73YKDEXTZVS24WDF53DHJ5N2DKZEK4LGWJG6KMSV7QFJUU	4000000000000000 microAlgos
[online]	6RAEOFSNR4OPCWJ5VAABE2KKEMIDEIHASHUGCFLZU7YIGD5LHUBQDVKY3Q	6RAEOFSNR4OPCWJ5VAABE2KKEMIDEIHASHUGCFLZU7YIGD5LHUBQDVKY3Q	3999999876542211 microAlgos
[online]	62RZZ2EWRSFLAVLSSG55NYMSMOCMDWGJQFKNZDPVVPSXOF6LZHDUOURPWU	62RZZ2EWRSFLAVLSSG55NYMSMOCMDWGJQFKNZDPVVPSXOF6LZHDUOURPWU	2000000123456789 microAlgos
```

```sh
# test transaction
$ ./sandbox goal clerk send -a 123456789 -f 6RAEOFSNR4OPCWJ5VAABE2KKEMIDEIHASHUGCFLZU7YIGD5LHUBQDVKY3Q -t 62RZZ2EWRSFLAVLSSG55NYMSMOCMDWGJQFKNZDPVVPSXOF6LZHDUOURPWU
```

### Check with [dappflow](https://app.dappflow.org/)

Switch to use testnode

<img width="1257" alt="demo1" src="https://user-images.githubusercontent.com/1580956/221351172-00a98ab2-f7e7-4bba-8390-442c60ea3e1b.png">

Then you should see the test results in the transaction tab

<img width="1357" alt="demo2" src="https://user-images.githubusercontent.com/1580956/221351237-aa748760-5a5c-4556-ad0b-4858d7157b64.png">


### Demo (deploy dapp)

Deploying calculator example app

```sh
$ python hello.py
Deployed app in txid SECWWIIFW6REE3RROAPPHVIIS7XNDOWQIUX6EM2WOJDPEDF5EZQQ
        App ID: 108
        Address: 7WP6IWQOXYYADHQBRJT3FEQTVQNIKBGLUQ75CJ36JNRLGINZ22WGGVKYVE

Hello, Beaker
```

## Setup

```sh
$ brew install asdf poetry

$ asdf plugin-add python
$ asdf install python 3.10.10
$ asdf global python 3.10.10
```

## Local run

```sh
$ poetry install
$ poetry shell
$ poetry run pytest
```
