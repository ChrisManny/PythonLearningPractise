"""
模拟浏览器访问一个网页
"""

# 1.导入模块
import socket
import sys

# 2.创建socket
browser_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3.连接某个网址 www.google.com
browser_client.connect(("www.baidu.com", 80))

# 4.拼接请求头
"""
1.请求行
2.请求头
3.请求空行
"""
request_line = "GET / HTTP/1.1\r\n"
request_header = "HOST:www.baidu.com\r\n"
request_blank = "\r\n"

request_data = request_line + request_header + request_blank
# 5.发送请求头
browser_client.send(request_data.encode())

# 6.通过文件保存response

data_body = ""
try:
    while True:
        recv_data = browser_client.recv(1024) # 接受服务器返回的数据
        recv_data_decode = recv_data.decode("latin1")  # 接受服务器返回的数据
        if not recv_data_decode:
            break
        else:
            data_body += recv_data_decode
        # raise UnicodeDecodeError("有个别字符无法转译")
finally:
    print("receive完成，正在提取中")
    recv_data_html_location = data_body.find("<!DOCTYPE html>")
    print(f"从第{recv_data_html_location}个字符开始提取...")
    recv_data_html_location_cut = data_body[recv_data_html_location:]
    # print(recv_data_html_location_cut)
    with open("index.html","w") as file_baidu:
        file_baidu.write(recv_data_html_location_cut)
    print("写入文件完成")

# 7.关闭socket
browser_client.close()
print("服务结束")