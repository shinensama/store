# #     姓名  年龄  性别  编号   任职公司   薪资   部门编号
# names = [
#     ["曹操", 56, "男", "106", "IBM", 500, "50"],
#     ["大乔", 19, "女", "230", "微软", 501, "60"],
#     ["小乔", 19, "女", "210", "Oracle", 600, "60"],
#     ["许褚", 45, "男", "230", "Tencent", 700, "10"]
# ]
# sum1 = 0
# sum2 = len(names)
# age = 0
# # 统计每个人的平均薪资
# for i in range(sum2):
#     money = names[i][5]
#     sum1 += money
# print("每个人的平均薪资:", sum1 / sum2)
# # 统计每个人的平均年龄
# for i in range(sum2):
#     money1 = names[i][1]
#     age += money1
# print("每个人的平均年龄:", age / sum2)
# # 公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
# name = input("请输入新员工姓名:")
# age1 = input("请输入新员工年龄:")
# gender = input("请输入新员工性别:")
# number = input("请输入新员工编号:")
# company = input("请输入新员工任职公司:")
# pay = input("请输入新员工薪资:")
# departmentNumber = input("请输入新员工部门编号:")
# list1 = [name, age1, gender, number, company, pay, departmentNumber]
# names.append(list1)
# print(names)
# # 统计公司男女人数
# man = 0
# woman = 0
# for i in range(sum2):
#     if names[i][2] == "男":
#         man += 1
#     elif names[i][2] == "女":
#         woman += 1
# print("公司男性人数为:", man, "公司女性人数为:", woman)
# # 每个部门的人数
#
#
# # 现在魔法学院有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。但是呢，因为有些魔法作业有一定难度，教授不强制同学们必须上交，所以大家上交作业的次数并不一致
# performance = {
#     "罗恩": [23, 35, 44],
#     "哈利": [60, 77, 68, 88, 90],
#     "赫敏": [97, 99, 89, 91, 95, 90],
#     "马尔福": [100, 85, 90]
# }
# for i in performance:
#     print(i, "的总成绩为：", sum(performance[i]))
#
#
# # 当输入是54321时，写出下面程序的执行结果
# num = int(input("请输入一个数："))
# while num != 0:
#     print(num % 10)
#     num = num // 10
# # 执行结果为
# # 1
# # 2
# # 3
# # 4
# # 5
#
# # 对下列列表进行冒泡排序
# a = [5, 2, 4, 7, 9, 1, 3, 5, 4, 0, 6, 1, 3]
# for i in range(len(a)):
#     for j in range(len(a) - i - 1):
#         if a[j] > a[j+1]:
#             a[j+1], a[j] = a[j], a[j+1]
# print("排列之后的数组为：", a)
