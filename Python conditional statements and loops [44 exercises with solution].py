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
# try:
#     while file_name:
#             with open(file_name, "a", encoding="utf-8") as file_object:
#                 user_name = input("请问你的名字是： ")
#                 print(f"你好，{user_name}。欢迎来到我的网站！")
#                 file_object.write(f"{user_name}\n于{time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))}刚刚访问了网站\n")
# except:
#     pass
# import  random
# class Dize:
#     """
#     随机掷骰子两次
#     """
#     # def __init__(self):
#     #     self = self
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
#     """
#     - 姓名
#     - 性别
#     - 分数
#     - 成绩等级（A、B、C、D）
#     """
#
#     def __init__(self, name):
#         self.grade = int(input("请输入你的分数： "))
#         self.name = name
#
#     def grade_lv_calculate(self):
#         try:
#             if 60 > int(self.grade) >= 0:
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
