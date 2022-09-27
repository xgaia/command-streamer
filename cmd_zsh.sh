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
