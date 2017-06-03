import requests,json
import urllib.parse

LINE_ACCESS_TOKEN="9qdZizFM5G6T767RFZLH1hdyyXnUCpDZw8WMzqyyrB1"
url = "https://notify-api.line.me/api/notify"


message ="Food or drink expired." # ข้อความที่ต้องการส่ง
msg = urllib.parse.urlencode({"message":message})
LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
session = requests.Session()
a=session.post(url, headers=LINE_HEADERS, data=msg)
print(a.text)
