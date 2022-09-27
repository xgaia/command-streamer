# History stream

## Install

```bash
pip install flask
```
## Run

```bash
SECRET_TOKEN="azerty" FLASK_APP=app.py flask run
```

## Run with docker

```bash
docker run -d -e SECRET_TOKEN=azerty -p 5000:5000 xgaia/command-streamer
```

## Stream your terminal

### zsh

source cmd_zsh.sh

```zsh
source zshrc.sh
```
### Bash

you have to install bash-preexec: https://github.com/rcaloras/bash-preexec
source cmd_bash.sh

## Stream your python interperter

python -i cmd.py

Type some command and go to [localhost:5000](http://localhost:5000)
