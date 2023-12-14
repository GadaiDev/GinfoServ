import requests

sv_name = ""
def write(port,text):
    requests.post(f"{sv_name}w",{"port":port,"data":text})
    return f""

def read(port):
    return requests.post(f"{sv_name}r",{"port":port}).text

def is_exist(port):
    txt = requests.post(f"{sv_name}e",{"port":port}).text
    return txt == "true"
def setup(url):
    global sv_name
    sv_name = url
