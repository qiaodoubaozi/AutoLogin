import json
import os

# 运营商,依次是电信,联通,移动,校园网
all_belongs = ["telecomn", "unicomn", "cmccn", ""]

def read_data_from_file():
    if not os.path.exists("user_info.json"):
        print(f"Profile not found. Creating a new one: ")
        write_data_to_file()
    with open("user_info.json", 'r') as f:
        data = json.load(f)
    return data

def write_data_to_file():
    username = input("请输入用户名: ")
    password = input("请输入密码: ")
    belongs = input("请输入运营商(电信: 0, 联通: 1, 移动: 2, 校园网: 3): ")
    data = {
        "username": username,
        "password": password,
        "belongs": all_belongs[int(belongs)]
    }
    with open("user_info.json", 'w') as f:
        json.dump(data, f)