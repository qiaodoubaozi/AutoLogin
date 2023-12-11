from request_handler import send_query_request, send_login_request
from response_handler import process_response
# 用户账号
username = 8209210611

# 用户密码
password = "/wsq/123/"

#ip地址
ip = "100.69.251.161"

# 运营商,依次是电信,联通,移动,校园网
belongs = ["telecomn", "unicomn", "cmccn", ""]

process_response(send_query_request(username, password, ip))

print("==================================================")


process_response(send_login_request(username, password, ip, belongs[2]))

print("==================================================")