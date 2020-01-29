import urllib.request
import gevent

"""
实现通过协程下载多张图片
"""


# 1.定义下载的函数（URL，file_name）
def download_img(url, file_name):
    """
    读取url对应的文件，并通过协程下载
    :param url:
    :param file_name:
    """
    try:
        # 1.解析URL
        response = urllib.request.urlopen(url)
        # 2.获取文件对象的内容
    except IOError:
        print("获取url失败")
    else:
        try:
            with open(file_name, "wb") as img_file:
                while True:
                    img_data = response.read(1024)
                    print(f"当前正在下载{file_name}")
                    # 3.将读取的内容写入文件
                    if img_data:
                        img_file.write(img_data)
                    else:
                        print(f"{file_name}下载完成")
                        break
        except IOError:
            print(f"下载{file_name}失败")


# 2.创建协程对象
if __name__ == '__main__':
    url1 = "http://t8.baidu.com/it/u=3571592872,3353494284&fm=79&app=86&f=JPEG?w=1200&h=1290"
    url2 = "http://t8.baidu.com/it/u=1484500186,1503043093&fm=79&app=86&f=JPEG?w=1280&h=853"
    url3 = "http://t8.baidu.com/it/u=2247852322,986532796&fm=79&app=86&f=JPEG?w=1280&h=853"

    gevent_url1 = gevent.spawn(download_img, url1, "1.jpg")
    gevent_url2 = gevent.spawn(download_img, url2, "2.jpg")
    gevent_url3 = gevent.spawn(download_img, url3, "3.jpg")

    gevent.joinall([gevent_url1, gevent_url2, gevent_url3])
