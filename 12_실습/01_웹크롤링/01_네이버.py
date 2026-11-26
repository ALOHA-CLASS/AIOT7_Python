import urllib.request
res = urllib.request.urlopen("http://www.naver.com/")
print(type(res))
print(res.status)
print("NAVER 웹페이지의 소스 내용----------------------------------------------------------------")
print(res.read(1000).decode('utf-8'))