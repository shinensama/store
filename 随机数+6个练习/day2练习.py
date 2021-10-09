import random
from ctypes import windll
import time

# 随机数
randint = random.randint(10, 90)  # 从10到90之前随机取一个数字
num1 = randint
count = 0
print("10~90范围内，三次机会猜大小")
while True:
    count = count + 1
    num = int(input("请输入一个数字:"))
    if num1 == int(num):
        print("蒙对了!(〃'▽'〃)")
        break
    elif num1 > int(num) and count < 3 and 10 < num < 90:
        print("猜小了⊙︿⊙")
    elif num1 < int(num) and count < 3 and 10 < num < 90:
        print("猜大了⊙﹏⊙")
    elif num < int(10) or num > int(90):
        print("请仔细看范围！不要浪费机会！┗( ▔, ▔ )┛")
    elif num1 != int(num) and count == 3:
        print("已错误三次，程序五秒后退出￣へ￣")
        time.sleep(5)
        user32 = windll.LoadLibrary('user32.dll')
        user32.LockWorkStation()
        break
print('\n')

# 1.华氏温度转换到摄氏温度
print("❀华氏温度转换到摄氏温度❀")
num = float(input("请输入华氏温度:"))
print("摄氏温度：", (5 / 9 * (num - 32)))
print('\n')

# 2.输入圆的半径计算周长和面积
print("❀输入圆的半径计算周长和面积❀")
num = float(input("请输入圆的半径:"))
print("圆的周长：", 2 * 3.14 * num, "圆的面积：", 3.14 * num ** 2)
print('\n')

# 3.判断此年份是不是闰年
print("❀判断此年份是不是闰年❀")
num = int(input("请输入年份："))
if (num % 100) == 0:
    if (num % 400) == 0:
        print("是闰年")
    else:
        print("不是闰年")
else:
    if (num % 4) == 0:
        print("是闰年")
    else:
        print("不是闰年")
print('\n')

# 4.英制单位英寸与公职单位厘米互换
print("❀英制单位英寸与公职单位厘米互换❀")
num = float(input("请输入长度:"))
num1 = input("请输入单位:")
if num1 == "in":
    print((num * 2.54), "cm")
elif num1 == "cm":
    print((num / 2.54), "in")
else:
    print("不支持此单位的转换")
print('\n')

# 5.百分制成绩转换为等级制成绩
print("❀百分制成绩转换为等级制成绩❀")
num = int(input("请输入百分制成绩:"))
if 90 <= num <= 100:
    print("A")
elif 80 <= num < 90:
    print("B")
elif 70 <= num < 80:
    print("C")
elif 60 <= num < 70:
    print("D")
elif 0 <= num < 60:
    print("E")
else:
    print("此分数无效")
print('\n')

# 6.输入三条边长，如果能构成三角形就计算周长和面积
print("❀输入三条边长，如果能构成三角形就计算周长和面积❀")
num = float(input("请输入第一条边长:"))
num1 = float(input("请输入第二条边长:"))
num2 = float(input("请输入第三条边长:"))
p = ((num + num1 + num2) / 2)
if num + num1 > num2 and num + num2 > num1 and num1 + num2 > num:
    print("三角形周长为:", num + num1 + num2, "三角形面积:", ((p * (p - num) * (p - num1) * (p - num2)) ** 0.5))
else:
    print("三条边长不能构成三角形")
