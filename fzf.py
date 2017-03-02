import urllib.request
import re

values = {"CertNo":"130923199303160014"}
data = urllib.parse.urlencode(values).encode("utf-8")
url = "http://ent.sipmch.com.cn/ModuleDefaultCompany/RentManage/SearchRentNo"
req = urllib.request.Request(url)
with urllib.request.urlopen(req,data=data) as f:
    resp = f.read().decode("utf-8")
    print(resp)

srtingtest = "23r2rsdfdsf"
pattern = re.compile(r'"2"')
match = pattern.match(stringtest)
if match:
    print(match)
