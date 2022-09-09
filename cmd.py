import requests
import json
import readline

APP_URL = "http://localhost:5000"
SECRET_TOKEN = "azerty"


def cmd_stream():
    hl = readline.get_current_history_length()
    last_cmd = readline.get_history_item(hl)
    headers = {
        "token": SECRET_TOKEN,
        "Content-Type": "application/json",
    }
    data = {
        "command": last_cmd,
        "type": "python",
    }
    requests.post(f"{APP_URL}/command", headers=headers, data=json.dumps(data))


readline.set_pre_input_hook(cmd_stream)
