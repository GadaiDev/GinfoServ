import os
from flask import Flask, request
import random

app = Flask(__name__)


@app.route('/w', methods=["POST"])
def write():
  open(f"port-{request.form.get('port')}.txt", "w",
       encoding="utf-8").write(request.form.get("data"))
  return ""


@app.route('/r', methods=["POST"])
def read():
  txt = open(f"port-{request.form.get('port')}.txt", "r",
             encoding="utf-8").read()
  os.remove(f"port-{request.form.get('port')}.txt")
  return txt


@app.route('/e', methods=["POST"])
def exist():
  try:
    txt = open(f"port-{request.form.get('port')}.txt", "r", encoding="utf-8")
    return "true"
  except FileNotFoundError:
    return "false"


app.run(host='0.0.0.0', port=8000)
