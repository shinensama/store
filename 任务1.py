import random
import time
from ctypes import windll

# 实现输入10个数字，并打印10个数的求和结果
list1 = []
while len(list1) < 10:
    list1.append(int(input("请输入数字:")))
    print(list1)
print("十个数的和为:", sum(list1))
print('\n')

# 从键盘依次输入10个数，最后打印最大的数、10个数的和、平均数
list2 = []
while len(list2) < 10:
    list2.append(int(input("请输入数字:")))
    print(list2)
print("十个数种最大的数为:", max(list2))
print("十个数的和为:", sum(list2))
print("十个数的平均数为:", (sum(list2) / 10))
print('\n')

# 使用random模块，如何产生50~150之间的数
randint = random.randint(50, 150)
print('\n')

# 从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。)
num = float(input("请输入第一条边长:"))
num1 = float(input("请输入第二条边长:"))
num2 = float(input("请输入第三条边长:"))
if num + num1 > num2 and num + num2 > num1 and num1 + num2 > num:
    if num == num1 and num == num2 and num1 == num2:
        print("此三角形为等边三角形")
    elif (num == num1 and num == num2 and num1 != num2) or (num == num1 and num != num2 and num1 == num2) or (num != num1 and num == num2 and num1 == num2):
        if num**2 == num1**2 + num2**2 or num1**2 == num**2 + num2**2 or num2**2 == num1**2 + num**2:
            print("此三角形为等腰直角三角形")
        else:
            print("此三角形为等腰三角形")
    elif num**2 == num1**2 + num2**2 or num1**2 == num**2 + num2**2 or num2**2 == num1**2 + num**2:
        print("此三角形为直角三角形")
    else:
        print("此三角形为普通三角形")
else:
    print("此三边不能构成三角形")
print('\n')

# 使用+，-号实现两个数的调换
while True:
    switch = input("请输入切换按键:")
    if switch == ("+"):
        print("A=56,B=78")
    elif switch == ("-"):
        print("A=78,B=56")
    elif switch == ("B") or switch == ("b"):
        break
    else:
        print("不支持此操作指令")
print('\n')

# 实现登录系统的三次密码输入错误锁定功能（用户名：root，密码：admin）
frequency = 0
while True:
    user = input("请输入用户名:")
    if user == "root":
        break
    elif user != "root":
        print("不存在此用户")
while True:
    frequency = frequency + 1
    password = input("请输入密码:")
    if password == "admin":
        print("密码正确！")
        break
    elif password != "admin" and frequency < 3:
        print("密码输入错误，请重新输入")
    elif password != "admin" and frequency == 3:
        print("输入错误三次，即将锁定")
        time.sleep(3)
        user32 = windll.LoadLibrary('user32.dll')
        user32.LockWorkStation()
        break
print('\n')

# 编程实现三角形打印
for i in range(7):
    print(" "*(6-i),"* "*(i+1))
    for h in range(6-i):
        print(end=" ")
    for j in range(6-i,7):
        print("*",end=" ")
    print("")
print('\n')

# 编程实现99乘法表的倒序打印
for i in range(9,0,-1):
    for j in range(1,i+1):
        print(j,"x",i,"=",j*i,"\t",end="")
    print("")
print('\n')

# 用循环来实现20以内的数的阶乘。（1！+2！+3！+......+20！）
list1 = []
num = 0
n1 = 0
while num < 20:
    num = num + 1
    list1.append(num)
    n = 1
    for i in list1:
        n *= i
    n1 += n
print("20以内的数的阶乘和为:",n1)