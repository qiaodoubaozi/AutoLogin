from request_handler import send_query_request, send_login_request
from response_handler import process_response
from utils.get_current_ip import get_current_ip
from utils.persistence import read_data_from_file

# 获取用户信息
user_info = read_data_from_file()

# 用户账号
username = user_info.get('username')

# 用户密码
password = user_info.get('password')

# ip地址
ip = get_current_ip()

# 运营商
belongs = user_info.get('belongs')

process_response(send_query_request(username, password, ip))

process_response(send_login_request(username, password, ip, belongs))
