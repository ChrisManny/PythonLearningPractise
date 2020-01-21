# 1.导入模块
import socket


# 4.socket发送消息
def send():
    """向服务端发送一条消息"""
    send_content = input("请输入要发送的消息： ")
    tcp_chat_client.send(send_content.encode())


# 5.socket接收消息
def recv():
    """接收来自服务端的消息"""
    recv_content, ip_port = tcp_chat_client.recv()
    print(f"接收到一条新消息：{recv_content.decode()}")


# 7.主函数
if __name__ == '__main__':
    # 2.创建socket对象
    tcp_chat_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 3.socket连接服务器
    tcp_chat_client.connect(("127.0.0.1", 8080))

    # 4.socket发送消息
    send()

    # 5.socket接收消息
    recv()

    # 6.关闭soc
    tcp_chat_client.close()
