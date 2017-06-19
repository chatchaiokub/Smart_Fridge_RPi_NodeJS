# -*- coding: utf-8 -*-f
import requests,json
from urlparse import urlparse
import urllib

LINE_ACCESS_TOKEN="9qdZizFM5G6T767RFZLH1hdyyXnUCpDZw8WMzqyyrB1"
url = "https://notify-api.line.me/api/notify"

message ="อาหาร หรือ เครื่องดื่ม หมดอายุ !"
msg = urllib.urlencode(({"message":message}))
LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
session = requests.Session()
a=session.post(url, headers=LINE_HEADERS, data=msg)
print(a.text)
