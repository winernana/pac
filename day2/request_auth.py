import requests
from requests.auth import HTTPBasicAuth

auth = ("admin","123456")
res=requests.get("http://api.github.com/user",auth=auth)
print(res.text)