# 代码参考
# https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Bm0hnziyn

import os
import qianfan
from API_KEY import *

# os.environ["QIANFAN_ACCESS_KEY"] = "b04d47257bb841038ff9d43e1db9e1ac"
# os.environ["QIANFAN_SECRET_KEY"] = "649eacc61c204e288e4fa4ea6d87baaf"

# https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application/v1
os.environ["QIANFAN_AK"] = "oQhY7UyGH5cDnbRYka4xLuXw"
os.environ["QIANFAN_SK"] = "62KqXQYuZa9A2wXgJpiv18jGeF2a9Rh4"

chat_comp = qianfan.ChatCompletion()

# 指定特定模型
resp = chat_comp.do(model="ERNIE-Speed-Pro-128K", messages=[{
    "role": "user",
    "content": "你好"
}])

print(resp["body"])