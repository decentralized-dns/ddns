#!/bin/bash

brew install asdf poetry
# for deployment
brew install flyctl
# for local https development
brew install mkcert

asdf plugin-add python
asdf install python 3.11.2
asdf global python 3.11.2
