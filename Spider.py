import urllib.request
import urllib.parse
import re
import os


class Spider:
    """
    创建Spider爬虫类，其中包括以下方法：
    """

    def __init__(self, page):
        self.page = page

    def send_request(self):
        """
        1.访问网页，发送请求
        """
        # 定义URL
        url = "https://pacaio.match.qq.com/irs/rcd?"

        # 伪装header
        header = {
            "accept-language": "en, en - US;q = 0.9, zh - CN;q = 0.8, zh;q = 0.7",
            "cookie": "tvfe_boss_uuid = 8def89799ee6e2e3;pgv_pvid = 2262001280;pac_uid = 0_5dc81b3d0e7e1;pgv_pvi = "
                      "3285164032;RK = XK7EpJdYPj;ptcz = "
                      "3ff8692644e238f507420b2b5479e476dd7e4ad1f6ffda16a74647bcc0f52e10;pgv_info = ssid = "
                      "s133614294;ts_uid = 2404414514;ts_last = new.qq.com / ch / world /;ad_play_index = 85",
            "user-agent": "Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / "
                          "79.0.3945.88Safari / 537.36",
        }

        # 解析formdata并进行编译
        formdata = {
            "cid": "135",
            "token": "6e92c215fb08afa901ac31eca115a34f",
            "ext": "world",
            "page": self.page,
            "expIds": "20200131009129|20200203A049ND|20200203A04L93|20200203A0271M|20200203A009T6",
            "expIds": "20200201A04Q9M|20200201A0CE83|20200201A0HESF|20200201A0FRVA|20200201A09EEK|20200201V06Y9D"
                      "|20200201A04I6R|20200121A0ME7R|20200201V05BCV|20200201A0HESC",
            "callback": "__jp9"
        }
        formdata = urllib.parse.urlencode(formdata).encode()
        self.page += 1

        # 使用IP proxy
        """
        1.设置代理IP以及端口
        2.创建Proxyhandler
        3.创建opener
        4.安装opener
        """
        proxy = {
            "http": "123.149.136.241:9999"
        }
        proxy_obj = urllib.request.ProxyHandler(proxies=proxy)
        opener = urllib.request.build_opener(proxy_obj)
        urllib.request.install_opener(opener)

        # 发送Request（包含URL和header）
        request = urllib.request.Request(url, headers=header)

        # 发送URLopen（包含Request和formdata）
        self.response = urllib.request.urlopen(url=request, data=formdata)
        self.excute_response()

    def excute_response(self):
        """
        2.接收数据，并根据需求进行清洗
        """
        # 通过正则处理过后的返回结果（类型：列表）
        self.result_title = re.findall(r'title":"(.*?)",', self.response.read().decode())
        self.file_save()

    def file_save(self):
        """
        3.写入文件
        """
        print("开始执行IO方法")
        try:
            with open(r"腾讯国际新闻2020-02-03.json", "a+") as fp:
                for item in self.result_title:
                    fp.write(item + "\n")
                print("数据写入成功")
        except FileNotFoundError:
            with open(r"腾讯国际新闻2020-02-03.json", "w") as fp:
                print("文件创建成功")
        # self.excute_response(fp)

    def user_controller(self):
        """
        4.用户控制器（非必须，可以在其中定义一些爬虫开始与关闭的行为。）
        """
        pass


if __name__ == '__main__':
    i = 1
    spider_tecent_news = Spider(i)
    while i <= 10:
        spider_tecent_news.send_request()
        i += 1
