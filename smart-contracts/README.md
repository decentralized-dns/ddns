# smart_contracts test <!-- omit in toc -->

- [Setup sandbox](#setup-sandbox)
  - [demo](#demo)
  - [Check with dappflow](#check-with-dappflow)
- [Setup](#setup)
- [Local run](#local-run)

## Setup sandbox

```
git clone https://github.com/algorand/sandbox.git
cd sandbox
# assuming docker and docker-compose have been setup
./sandbox up dev -v
# after the sandbox is up
./sandbox goal account list # sanity check
```

### demo

```
$ ./sandbox goal account list
[online]	YBHNJCX6LJNS73YKDEXTZVS24WDF53DHJ5N2DKZEK4LGWJG6KMSV7QFJUU	YBHNJCX6LJNS73YKDEXTZVS24WDF53DHJ5N2DKZEK4LGWJG6KMSV7QFJUU	4000000000000000 microAlgos
[online]	6RAEOFSNR4OPCWJ5VAABE2KKEMIDEIHASHUGCFLZU7YIGD5LHUBQDVKY3Q	6RAEOFSNR4OPCWJ5VAABE2KKEMIDEIHASHUGCFLZU7YIGD5LHUBQDVKY3Q	3999999876542211 microAlgos
[online]	62RZZ2EWRSFLAVLSSG55NYMSMOCMDWGJQFKNZDPVVPSXOF6LZHDUOURPWU	62RZZ2EWRSFLAVLSSG55NYMSMOCMDWGJQFKNZDPVVPSXOF6LZHDUOURPWU	2000000123456789 microAlgos
```

```
# test transaction
$ ./sandbox goal clerk send -a 123456789 -f 6RAEOFSNR4OPCWJ5VAABE2KKEMIDEIHASHUGCFLZU7YIGD5LHUBQDVKY3Q -t 62RZZ2EWRSFLAVLSSG55NYMSMOCMDWGJQFKNZDPVVPSXOF6LZHDUOURPWU
```

### Check with [dappflow](https://app.dappflow.org/)

## Setup

```
brew install asdf poetry

asdf plugin-add python
asdf install python 3.10.10
asdf global python 3.10.10
```

## Local run

```
poetry install
poetry shell
```
