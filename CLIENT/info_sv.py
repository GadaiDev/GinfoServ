import requests

SV_NAME = "https://info.gadaidev.repl.co/"
ERROR = """<!doctype html>
<html lang=en>
<title>500 Internal Server Error</title>
<h1>Internal Server Error</h1>
<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>"""

def write(port,text):
    requests.post(f"{SV_NAME}w",{"port":port,"data":text})
    return f""
def read(port):
    return requests.post(f"{SV_NAME}r",{"port":port}).text
def is_exist(port):
    if read(port) == ERROR:
        return False
    else:
        return True
