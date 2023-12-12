# request_handler.py

import requests
import urllib.parse
import urllib3

# 发送查询请求
def send_query_request(username, password, ip):

    # 禁止urllib3库产生的InsecureRequestWarning警告
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    url = f"https://10.1.1.1:802/eportal/portal/Custom/" \
          f"online_data?callback=dr1003&username={username}" \
          f"&password={urllib.parse.quote(password)}&ip={ip}"

    response = requests.get(url, verify=False).content
    return response

# 发送登录请求
def send_login_request(username, password, ip, belongs):

    # 禁止urllib3库产生的InsecureRequestWarning警告
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    url = f"https://10.1.1.1:802/eportal/portal/" \
          f"login?callback=dr1004&login_method=1" \
          f"&user_account=%2C0%2C{username}%40{belongs}" \
          f"&user_password={urllib.parse.quote(password)}" \
          f"&wlan_user_ip={ip}"

    response = requests.get(url, verify=False).content
    return response