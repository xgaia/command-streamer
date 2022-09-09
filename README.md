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

create a `zshrc.sh` file with the following content

```zsh
app_url=http://localhost:5000
secret_token=azerty
function post_command () {
 curl -s -X POST ${app_url}/command -H 'token: '${secret_token}'' -H 'Content-Type: application/json' -d '{"command":"'${1}'"}' > /dev/null
}
function reset () {
 curl -s ${app_url}/reset -H 'token: '${secret_token}'' > /dev/null
}
autoload -Uz  add-zsh-hook
add-zsh-hook preexec post_command
```

source the file

```zsh
source zshrc.sh
```

## Stream your python interperter

python -i cmd.py

Type some command and go to [localhost:5000](http://localhost:5000)
