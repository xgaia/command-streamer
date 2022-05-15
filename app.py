import os
from flask import Flask
from flask import request
from flask import render_template
import string
import random

import sqlite3

TOKEN = os.getenv(
    "SECRET_TOKEN", "".join(random.choices(string.ascii_letters + string.digits, k=25))
)

print("++++++++++++++ TOKEN ++++++++++++++")
print("     {}     ".format(TOKEN))
print("+++++++++++++++++++++++++++++++++++")

connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS command (id INTEGER PRIMARY KEY AUTOINCREMENT, command text)"
)
connection.commit()
connection.close()

app = Flask(__name__)


@app.route("/")
def ui():
    return render_template("index.html")


@app.route("/command", methods=["POST"])
def command():

    if "token" not in request.headers:
        return {"message": "no"}, 401
    else:
        if request.headers["token"] != TOKEN:
            return {"message": "no"}, 401

    data = request.get_json()
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO command VALUES (NULL, ?)", (data["command"],))
    connection.commit()
    connection.close()
    return {"message": "ok"}


@app.route("/commands", methods=["GET"])
def get_commands():

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT command FROM command")
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
    data = []
    for row in rows:
        data.append(row[0])
    return {"commands": data}
