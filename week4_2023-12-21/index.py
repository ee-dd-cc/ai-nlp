import requests
import json

positiveList = []
negativeList = []

def send_post_request(url, data):
    # 定义自定义请求头
    headers = {'Content-Type': 'application/json'}

    # 发送 POST 请求
    response = requests.post(url, json=data, headers=headers)

    # 检查响应
    if response.status_code == 200:
        # 返回响应的 JSON 对象
        return response.json()
    else:
        print('POST 请求失败，状态码：', response.status_code)
        return None

# 打开 JSON 文件
with open('./raw.json', 'r') as file:
    # 解析 JSON 数据
    JsonList = json.load(file)

for item in JsonList:
    url = 'https://language.googleapis.com/v2/documents:analyzeSentiment?key=AIzaSyBIxJg42ZoIoOnju6cJavUTWsAjlIQN2FY'
    params = {
        "document": {"type": "PLAIN_TEXT", "content": item}
    }
    res = send_post_request(url, params)

    # 检查 res 是否为 None
    if res is not None:
        # 将 res 添加到列表中
        if res['documentSentiment']['score'] > 0:
            positiveList.append(item)
        else:
            negativeList.append(item)

print('positiveList----  ', positiveList)
print('================')
print('negativeList----  ', negativeList)
