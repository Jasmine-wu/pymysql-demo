"""Send a reply from the proxy without sending any data to the remote server."""
from mitmproxy import http
import json


# def request(flow: http.HTTPFlow) -> None:
#     if "quote.json" in flow.request.pretty_url:
#         with open("/Users/neil/Desktop/test/课件/web/maplocal_xueqiu.json", encoding="utf-8") as f:
#
#             flow.response = http.HTTPResponse.make(
#                 200,  # (optional) status code
#                 f.read(),  # (optional) content
#                 {"Content-Type": "application/json"}  # (optional) headers
#             )

def response(flow):
    if "quote.json" in flow.request.pretty_url:
        # loads 加载字符串
        # load 加载文件
        data = json.loads(flow.response.content)
        data["data"]["items"][1]["quote"]["name"]="aliali"
        flow.response.text=json.dumps(data)
        # 字符串格式化成json, indent缩进为2
        print(json.dumps(data, indent=2))

