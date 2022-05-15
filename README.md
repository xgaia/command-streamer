# History stream

## Install

```bash
pip install flask sqlite3
```

## Run


```bash
SECRET_TOKEN="<secret_token>" FLASK_APP=app.py flask run
```

## Stream your terminal

### zsh

create a `zshrc.sh` file with the following content

```zsh
function post_command () {
 curl -s -X POST http://localhost:5000/command -H 'token: <secret_token>' -H 'Content-Type: application/json' -d '{"command":"'${1}'"}' > /dev/null
}
autoload -Uz  add-zsh-hook
add-zsh-hook preexec post_command
```

source the file

```zsh
source zshrc.sh
```

Type some command and go to [localhost:5000](http://localhost:5000)
