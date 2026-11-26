import urllib.request
res = urllib.request.urlopen("https://xn--pe5b27r.com/")
print("[ header 정보 ]----------")
res_header = res.getheaders()
for s in res_header :
    print(s)
print("[ body 내용 ]-----------")
print(res.read().decode('utf-8'))