import requests
from PIL import Image
from io import BytesIO

r = requests.get('https://pics2.gundamboom.kr/web/product/big/943386001687249541_2526909.jpg')
i = Image.open(BytesIO(r.content))
print(type(i))
i.save("./파일명.jpg")
i.show()