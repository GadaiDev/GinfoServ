import requests

sv_name = ""
ERROR = """<!doctype html>
<html lang=en>
<title>500 Internal Server Error</title>
<h1>Internal Server Error</h1>
<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>"""

def write(port,text):
    requests.post(f"{sv_name}w",{"port":port,"data":text})
    return f""
def read(port):
    return requests.post(f"{sv_name}r",{"port":port}).text
def is_exist(port):
    if read(port) == ERROR:
        return False
    else:
        return True
def setup(url):
    global sv_name
    sv_name = url
