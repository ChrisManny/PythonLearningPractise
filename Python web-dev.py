# -*- coding:UTF-8 -*-

# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
#
# for number in range(1500,2701):
#     if number % 7 == 0 or number in range(1500,2701,5):
#         print(number)
#
# 3. Write a Python program to guess a number between 1 to 9.
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

# answer = 6
#
# for user in range(1,10):
#     user = int(input("请输入一个1-9之间的数字： "))
#     if user == answer:
#         print("Well guessed.")
#         break
#     elif user != answer:
#         print("Try again")


# 4. Write a Python program to construct the following pattern, using a nested for loop.
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# i = 1
# for i in range(1,6):
#     print("*" * i)
#     i += 1
# for i in range(6,11):
#     print("*" * (10-i))
#     i += 1

# 5. Write a Python program that accepts a word from the user and reverse it.

# user = input("请输入一个数字，系统将返回其反向文字： ")
#
# for i in range(len(user)-1,-1,-1):
#     print(user[i],end="")
# print(",")
#

# 6. Write a Python program to count the number of even and odd numbers from a series of numbers.

# even_count = 0
# odd_count = 0
# for item in range(101):
#     if item % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print(f"""
# 0-100之间的偶数共有{even_count}个，
# 0-100之间的奇数共有{odd_count}个
# """)

# 7. Write a Python program that prints each item and its corresponding type from the following list.
# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
#
# for item in range(len(datalist)):
#     print(str(datalist[item])+ "," + str(type(datalist[item])))
#     item += 1

# 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.Note : Use 'continue' statement.

# for item in range(7):
#     if item == 3 or item == 6 :
#         continue
#     print(item ,end=" ")
#
# 9. Write a Python program to get the Fibonacci series between 0 to 50.

# output = []
# output.append(1)
# output.append(1)
# for item in range(2,51):
#     output.append((output[item - 1] + output[item - 2]))
#     item +=1
#     if int((output[item - 1] + output[item - 2])) > 50:
#         break
# print(output)

# 10. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print

# item = 1
# while item < 51:
#     if item % 15 == 0 :
#         print("FizzBuzz")
#         item += 1
#     elif item % 5 == 0 :
#         print("Buzz")
#         item += 1
#     elif item % 3 == 0 :
#         print("Fizz")
#         item += 1
#     else:
#         print(item)
#         item += 1


# write a Python program to remove the duplicates in a list
# number = [5,2,3,4,6,3,5,7,3,2,56,8,7,978,3,87]
#
# for item in number:
#     if number.count(item) != 1:
#         number.remove(item)
# number.sort()
# print(number)

# number = input("Phone: ")
#
# dict = {
#     0 : "零",
#     1 : "一",
#     2 : "二",
#     3 : "三",
#     4: "四",
#     5: "五",
#     6: "六",
#     7: "七",
#     8: "八",
#     9: "九",
#     10: "十"
# }
#
# for item in number:
#     if int(item) in dict:
#         print(dict.get(int(item)),end=" ")

# def greet_user():
#     print("Hi,everyone")
#     print("nihao a ")
# greet_user()

# try:
#     age = int(input("Age: "))
#     print(age)
# except ValueError:
#     print("value Error")

# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# result = []
# for item in thisdict.keys():
#     result.append(str(thisdict[item]))
# result.sort()
# print(result)
#
#
# 2. Write a Python script to add a key to a dictionary.

# sample = {
#     0: 10,
#     1: 20
# }
# sample[2] = 30
# print(sample)

# 20. Write a Python program to print all unique values in a dictionary.

# sample = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

# Write a Python function to multiply all the numbers in a list.

# 定义求和方法


# def sum_list(list):
#     sum1 = 0
#     for i in range(len(list)):
#         sum1 += int(list[i])
#     return sum1
#
#
# try:
#     print(sum_list((8, 2, 3, -1, 7)))
# except ValueError:
#     print("Oops!  That was no valid number.  Try again...")

# Write a Python function that takes a list and returns a new list with unique elements of the first list.


# def new_list(l):
#     m = []
#     for i in l:
#         if i not in m:
#             m.append(i)
#     return m
#
#
# print(new_list([1,2,3,3,3,3,4,5]))

# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.

# class Rectangle:
#     """
#     1.定义【长方形】的参数：length,width
#     2.定义长方形面积的计算函数：area
#
#     """
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         """
#         面积计算
#         :return:result_area 根据用户输入的长度、宽度输出面积
#         """
#         result_area = self.length * self.width
#         print(f"面积是： {result_area}")
#
#
# try:
#     input_length = float(input("请输入长度： "))
#     input_width = float(input("请输入宽度： "))
#     rectangle = Rectangle(input_length,input_width)
#     rectangle.area()
# except ValueError:
#     print("请输入纯数字，包括整数或者小数")

# 编写一个程序，它读取这个文件，并将你所写的内容打印三次：第一次打印时读取整个文件；第二次打印时遍历文件对象；第三次打印时将各行存储在一个列表中，再在with 代码块外打印它们。

# file_name = "C:\\Users\\Chris Manny\\Desktop\\Ireland\\learning_python.txt"
# try:
#     with open(file_name,encoding="utf-8") as file_object:
#         eachline = file_object.readlines()
#         for item in eachline:
#             # item.replace("Python", "C")
#             print(f"第行内容：{item.rstrip()}")
#         # print(file_object.read())
# except UnicodeDecodeError:
#     print("包含非法字符")

# 编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写入到文件guest.txt中。
# file_name = "C:\\Users\\Chris Manny\\Desktop\\Ireland\\guest.txt"
#
# user_input = input("请输入你的姓名： ")
# with open(file_name,"r+",encoding="utf-8") as file_object:
#     file_object.write(user_input)
#     print(file_object.read())
#
# 编写一个while 循环，提示用户输入其名字。用户输入其名字后，在屏幕上打印一句问候语，并将一条访问记录添加到文件guest_book.txt中。确保这
# 个文件中的每条记录都独占一行。
# import time
# file_name = "C:\\Users\\Chris Manny\\Desktop\\Ireland\\guest_book.txt"
#
# try: while file_name: with open(file_name, "a", encoding="utf-8") as file_object: user_name = input("请问你的名字是： ")
# print(f"你好，{user_name}。欢迎来到我的网站！") file_object.write(f"{user_name}\n于{time.strftime('%Y-%m-%d %H:%M:%S',
# time.localtime(time.time()))}刚刚访问了网站\n") except: pass import  random class Dize: """ 随机掷骰子两次 """ # def __init__(
# self): #     self = self
#
#     def roll(self):
#         """
#         随机掷骰子
#         :return: 两次的结果
#         """
#         x = random.randint(1,6)
#         y = random.randint(1,6)
#         result = (x,y)
#         return result
#
# dize = Dize()
# print(dize.roll())

"""
创建一个student类，包括以下属性：
    - 姓名
    - 性别
    - 分数
    - 成绩等级（A、B、C、D）
"""

# class Student():
# #     """
# #     - 姓名
# #     - 性别
# #     - 分数
# #     - 成绩等级（A、B、C、D）
# #     """
# #
# #     def __init__(self, name):
# #         self.grade = int(input("请输入你的分数： "))
# #         self.name = name
# #
# #     def grade_lv_calculate(self):
# #         try:
# #             if 60 > int(self.grade) >= 0:
#                 self.grade_lv = "D"
#                 print(f"你的等级是{self.grade_lv}")
#             elif 75 > int(self.grade) >= 60:
#                 self.grade_lv = "C"
#                 print(f"你的等级是{self.grade_lv}")
#             elif 90 > int(self.grade) >= 75:
#                 self.grade_lv = "B"
#                 print(f"你的等级是{self.grade_lv}")
#             elif 100 >= int(self.grade) >= 90:
#                 self.grade_lv = "A"
#                 print(f"你的等级是{self.grade_lv}")
#             else:
#                 print("请输入0-100之间的数整数")
#         except ValueError:
#             print("抱歉，您输入的不是数字。成绩应该为0-100之间的整数")
#
#
# student = Student("zhnagzeyu")
# student.grade_lv_calculate()
# 测试Git

# import multiprocess

"""
请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
"""

# class Student:
#     def __init__(self, name, gender):
#         self.name = name
#         self.__gender = gender
#
#     def get_gender(self):
#         """
#         获取gender（增加访问权限，防止外部修改）
#         :return: self.__gender
#         """
#         print(f"你当前的性别是： {self.__gender}")
#
#     def set_gender(self):
#         """
#         修改gender
#         :return: self.__gender
#         """
#         user_input_gender = input("请输入你的新性别： ")
#         self.__gender = user_input_gender
#         print(f"你当前的新性别是： {self.__gender}")
#         # print(type(self.__gender))
#
#
# stu = Student("Zoey", "male")
# stu.get_gender()
# stu.set_gender()

# """
# 请利用@property给一个Student对象计算他的年龄
# """
#
#
# class Student:
#     """
#     birth 生日（要求用户输入，属于setter）
#     age 年龄 = 2020 - 生日（只读属性）
#     """
#
#     @property
#     def birth(self):
#         return self._birth
#
#     @birth.setter
#     def birth(self, user_input_birth):
#         self._birth = user_input_birth
#
#     @property
#     def age(self):
#         return 2020 - self._birth
#
#
# stu = Student()
# stu.birth = 1994
# print(stu.age)
#
# """
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
# """
#
#
# class Screen:
#     # width属性声明
#     @property
#     def width(self):
#         return self._width
#
#     @width.setter
#     def width(self, user_input_width):
#         self._width = user_input_width
#
#     # height属性声明
#     @property
#     def height(self):
#         return self._height
#
#     @height.setter
#     def height(self, user_input_height):
#         self._height = user_input_height
#
#     # resolution属性声明
#     @property
#     def resolution(self):
#         return self._resolution
#
#     def count_area(self,width,height):
#         width = self._width
#         height = self._height
#         area = width * height
#         print(f"面积是： {area} 。")
#
# screen = Screen()
# screen.width = int(input("请输入宽度： "))
# screen.height = int(input("请输入高度： "))
# screen.count_area(screen.width,screen.height)

# """
# 模拟浏览器访问一个网页
# """
#
# # 1.导入模块
# import socket
# import sys
#
# # 2.创建socket
# browser_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # 3.连接某个网址 www.google.com
# browser_client.connect(("www.baidu.com", 80))
#
# # 4.拼接请求头
# """
# 1.请求行
# 2.请求头
# 3.请求空行
# """
# request_line = "GET / HTTP/1.1\r\n"
# request_header = "HOST:www.baidu.com\r\n"
# request_blank = "\r\n"
#
# request_data = request_line + request_header + request_blank
# # 5.发送请求头
# browser_client.send(request_data.encode())
#
# # 6.通过文件保存response
#
# data_body = ""
# try:
#     while True:
#         recv_data = browser_client.recv(1024) # 接受服务器返回的数据
#         recv_data_decode = recv_data.decode("latin1")  # 接受服务器返回的数据
#         if not recv_data_decode:
#             break
#         else:
#             data_body += recv_data_decode
#         # raise UnicodeDecodeError("有个别字符无法转译")
# finally:
#     recv_data_html_location = data_body.find("<!DOCTYPE html>")
#     recv_data_html_location_cut = recv_data_decode[recv_data_html_location:]
#     with open("index.html","w") as file_baidu:
#         file_baidu.write(recv_data_html_location_cut)
#     print("done")
#
# # 7.关闭socket
# browser_client.close()
#
# """
# 测试子线程守护机制
# """
#
# # 导入模块
# import threading
# import time
#
# # 自定义线程类（执行一个循环函数，设置time sleep）
# class Mythread(threading.Thread):
#     def run(self):
#         for i in range(5):
#             print(i)
#             i += 1
#             time.sleep(0.2)
#         print("子线程执行结束")
#
# # 创建线程实例，查看子线程与主线程结束顺序
# mythread = Mythread()
# mythread.setDaemon(True)
# mythread.start()
# print("主线程执行结束")


# """
# 通过两个线程锁实现计数两百万（各100万）
# """
# from threading import Thread
# import time
#
# # 定义一个计数函数
# count_num = 0
# # thread_lock = Lock()
#
# def get_time():
#     now = time.time()
#     # 格式化年月日时分秒
#     local_time = time.localtime(now)
#     date_format_localtime = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
#     return date_format_localtime
#
#
# def count():
#     global count_num
#     for i in range(1000):
#         # thread_lock.acquire()
#         count_num += 1
#     # thread_lock.release()
#     date_format_localtime = get_time()
#     print("1000000执行完成" + date_format_localtime)
#
#
# # 创建一个线程1
# count_thread1 = Thread(target=count)
#
# # 创建一个线程2
# count_thread2 = Thread(target=count)
#
#
# # 定义主函数
#
# def main():
#     date_format_localtime = get_time()
#     count_thread1.start()
#     count_thread1.join()
#     count_thread2.start()
#     print("全部执行完成" + format(date_format_localtime))
#
#
# if __name__ == '__main__':
#     main()
#
# from threading import Thread,Lock
# import threading
#
# # 定义函数，根据下标获取列表元素值
# class Get_list(threading.Thread):
#     def run(self):
#         list_example = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#         for i in range(len(list_example)):
#             thread_lock.acquire()
#             print(str(i) + " " + str(threading.current_thread().getName()))
#             thread_lock.release()
#
# # 创建10个线程，观察资源的等待状态
#
# if __name__ == '__main__':
#     thread_lock = Lock()
#     thread1 = Get_list()
#     thread2 = Get_list()
#     thread3 = Get_list()
#     thread4 = Get_list()
#     thread5 = Get_list()
#     thread6 = Get_list()
#     thread7 = Get_list()
#     thread8 = Get_list()
#     thread9 = Get_list()
#     thread10 = Get_list()
#     thread1.start()
#     thread2.start()
#     thread3.start()
#     thread4.start()
#     thread5.start()
#     thread6.start()
#     thread7.start()
#     thread8.start()
#     thread9.start()
#     thread10.start()

"""
进程的基本使用
1.导入模块
2.创建一个进程对象
3.启动进程
4.主函数
"""

# # 1.导入模块
# import multiprocessing
#
#
# # 3.函数
# def count():
#     for i in range(5):
#         print(i)
#
#
# # 2.创建一个进程对象
# demo_process = multiprocessing.Process(target=count)
#
# # 4.主函数
# if __name__ == '__main__':
#     demo_process.start()
#     print("进程已启动")

#
# """
# 创建一个循环函数
# """
# import multiprocessing, time, os
#
#
# def count():
#     """
# 函数循环打印
#     """
#
#     print(multiprocessing.current_process(), multiprocessing.current_process().pid)
#     for i in range(10):
#         print("*" * i)
#         time.sleep(2)
#     # 打印进程的名称以及进程编号
#
#
# # import os
#
# if __name__ == '__main__':
#     # 创建一个进程执行上述函数
#     print_process = multiprocessing.Process(target=count, name="s")
#     print_process.start()
#     print(os.path.abspath("index.html"))  # 通过os.path模块获取文件路径

# """
# 队列的基本使用
# """
#
# # 创建一个队列（指定长度）
# import multiprocessing
# quene_example = multiprocessing.Queue(5)
# quene_example.put()

# """
# 实现一个线程不断生成一个随机数到一个队列中(考虑使用Queue这个模块)
# 实现一个线程从上面的队列里面不断的取出奇数
# 实现另外一个线程从上面的队列里面不断取出偶数
# """
# import queue
# import random
# import threading
#
#
# # 实现一个线程不断生成一个随机数到一个队列中(考虑使用Queue这个模块)
# def random_thread():
#     """
# 随机生成一个数字，并且将该数字保存到队列中
#     """
#     for i in range(10):
#         qu_save_num.put(random.randint(0,100),block=False)
#     print(f"1.队列内容是： {int(qu_save_num.get(block=False))}")
#
#
# # 实现一个线程从上面的队列里面不断的取出奇数
# def get_odd_in_queue():
#     while qu_save_num:
#         qu_save_num.get()
#         if qu_save_num.get(block=False) % 2 != 0:
#             print(f"2.队列中的奇数是 {qu_save_num.get(block=False)}")
#
#
#     # 实现另外一个线程从上面的队列里面不断取出偶数
#
#
# def get_even_in_queue():
#     while qu_save_num:
#         if qu_save_num.get(block=False) % 2 == 0 and qu_save_num.empty() == False:
#             print(f"3.队列中的偶数是 {qu_save_num.get(block=False)}")
#
#
#     # 主函数
#
#
# if __name__ == '__main__':
#     qu_save_num = queue.Queue()
#     random_thread = threading.Thread(target=random_thread)
#     odd_num_in_qu = threading.Thread(target=get_odd_in_queue)
#     even_num_in_qu = threading.Thread(target=get_even_in_queue)
#     random_thread.start()
#     random_thread.join()
#     odd_num_in_qu.start()
#     even_num_in_qu.start()

# import multiprocessing
#
#
# def copy():
#     print("正在拷贝")
#
#
# if __name__ == '__main__':
#     copy_file = multiprocessing.Pool(1)
#     for i in range(200):
#         copy_file.apply_async(copy)
#     copy_file.close()  # 停止该进程池接收其他进程任务
#     copy_file.join()


"""
测试进程池中的进程异步执行效果
"""

#
# from multiprocessing import Pool
# import os
#
#
# def count(i):
#     """
# 打印当前正在异步执行的进程池中的进程id
#     """
#     print(f"{i}——进程id：{os.getpid()}")
#
#
# if __name__ == '__main__':
#     pool_exm = Pool(3)
#     pool_exm.map()
#     for i in range(1,101):
#         pool_exm.apply_async(count(i),args=(i,))
#     pool_exm.close()
#     pool_exm.join()

#
# from multiprocessing import Pool, Process  # 引进程池pool 和进程
# import time
#
#
# # 打印功能函数
# def func(n):
#     """
# 打印数字1-10
#     :param n:
#     """
#     for i in range(10):
#         print(n + 1)
#
#
# if __name__ == '__main__':
#     start = time.time()
#     pool = Pool(5)  # 不写默认是你电脑的核数+1
#     pool.map(func, range(100))  # 必须是一个可迭代的类型
#     pool_time = time.time() - start
#
#     # 开100个进程
#     p_lst = []
# from multiprocessing import Pool, Process  # 引进程池pool 和进程
# import time
#
#
# # 打印功能函数
# def func(n):
#     """
# 打印数字1-10
#     :param n:
#     """
#     for i in range(10):
#         print(n + 1)
#
#
# if __name__ == '__main__':
#     start = time.time()
#     pool = Pool(5)  # 不写默认是你电脑的核数+1
#     pool.map(func, range(100))  # 必须是一个可
#     start = time.time()
#     for i in range(100):
#         p = Process(target=func, args=(i,))
#         p_lst.append(p)
#         p.start()
#     for p in p_lst: p.join()
#     Process_time = time.time() - start
#     print(pool_time, Process_time)

# def gen_squares(num):
#     for x in range(num):
#         yield x ** 2
#
#
# G = gen_squares(5)
# print(str(G))
# print(iter(G))

# """
# 自定义生成器
# """
#
#
# def main():
#     list_example = [i ** 2 for i in range(10)]
#     print(list_example)
#     for item in list_example:
#         print(item)
#
#
# if __name__ == '__main__':
#     main()


"""
greenlet实现协程
"""
#
# import time
# from greenlet import greenlet
# import gevent
#
#
# # 1.导入grennlet模块
#
#
# # 2.创建work1生成器
# def work1():
#     while True:
#         print("正在执行work1...")
#         time.sleep(0.5)
#         g2.switch()
#
#
# # 3.创建work2生成器
# def work2():
#     while True:
#         print("正在执行work2.........")
#         time.sleep(0.5)
#         g1.switch()
#
#
# if __name__ == '__main__':
#     # 4.创建greenlet对象
#     g1 = greenlet(work1)
#     g2 = greenlet(work2)
#     g1.switch()

from gevent import monkey

monkey.patch_all()

import gevent
import time


def eat(name):
    print('%s eat 1' % name)
    gevent.sleep(2)
    print('%s eat 2' % name)


def play(name):
    print('%s play 1' % name)
    gevent.sleep(1)
    print('%s play 2' % name)


g1 = gevent.spawn(eat, 'egon')
g2 = gevent.spawn(play, name='egon')
g1.join()
g2.join()
# 或者gevent.joinall([g1,g2])
print('主')
