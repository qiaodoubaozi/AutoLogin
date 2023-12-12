import json

# 提取相应中的关键信息并打印
def process_response(response):
    # 将响应内容从字节串转换为字符串
    response_str = response.decode('utf-8')
    json_str = response_str[response_str.find('{'):response_str.rfind('}')+1]

    # 将字符串转换为字典
    response_dict = json.loads(json_str)

    # 提取关键信息
    result = response_dict.get('result')
    msg = response_dict.get('msg')

    # 打印关键信息
    print(f"Result: {result}")
    print(f"Message: {msg}")
    if msg == "查询数据成功":
        print(f"total: {response_dict.get('total')}")
        print(f"AccountMaxLogin: {response_dict.get('accountmaxlogin')}")
        data = response_dict.get('data')
        for i in range(len(data)):
            print("--------------------------------------------------")
            print(f"第{i+1}个设备:")
            for key, value in data[i].items():
                print(f"{key}: {value}")

    print("==================================================")