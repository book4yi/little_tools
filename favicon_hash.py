import base64
import mmh3
import requests
# shodan 语法：http.favicon.hash:-1323954008
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 OPR/52.0.2871.40',
}
image_url = 'https://wshantinghotels.huazhu.com/hworld/NewWeb/img/favicon.ico?v=1612148400'

r = requests.get(url=image_url, headers=headers)
base64_data = base64.encodebytes(r.content)
hash_data = mmh3.hash(base64_data)
print(hash_data)

# 将图片保存到本地进行验证
# raw_data = base64.b64decode(base64_data)
# f = open(r'C:\Users\xxxx\Desktop\666.png', 'wb')
# f.write(raw_data)
# f.close()

