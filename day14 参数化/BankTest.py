import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from unittest import TestCase

import xlrd
from ddt import data
from ddt import ddt
from ddt import unpack
from xlutils.copy import copy

from 工商银行完整版 import *

# username,password,country,province,street,door,money
wb = xlrd.open_workbook(filename=r"C:\Users\20680\Desktop\python自动化测试\demo\day14 参数化/bank.xls",
                        encoding_override=True)

df = wb.sheet_names()  # 列表名
wb_len = len(wb.sheets())
wb_copy = copy(wb)

da_addUser = []
da_saveMoney = []
da_takeMoney = []
da_transformMoney = []
da_selectUser = []

for i in range(wb_len):
    st = wb.sheet_by_index(i)
    rows = st.nrows
    for j in range(1, rows):
        data1 = st.row_values(j)
        if i == 0:
            da_addUser.append([data1[0], data1[1], data1[2], data1[3], data1[4], data1[5], data1[6], data1[7], j])
        elif i == 1:
            da_saveMoney.append([data1[0], data1[1], data1[2], j])
        elif i == 2:
            da_takeMoney.append([data1[0], data1[1], data1[2], data1[3], j])
        elif i == 3:
            da_transformMoney.append([data1[0], data1[1], data1[2], data1[3], data1[4], j])
        elif i == 4:
            da_selectUser.append([data1[0], data1[1], data1[2], j])
print(da_addUser)
print(da_saveMoney)
print(da_takeMoney)
print(da_transformMoney)
print(da_selectUser)


# da = xlrd.read("hkr.xlsx")  # 程序自动去读取参数化数据


@ddt
class TestBank(TestCase):
    global wb_copy

    @data(*da_addUser)
    @unpack
    def testAddUser(self, a, b, c, d, e, f, g, h, i):
        result = bank_addUser(a, b, c, d, e, f, g)

        if result == h:  # 让程序自动将测试结果写到excel表里。
            wb_copy.get_sheet(0).write(i, 8, "通过！")
            wb_copy.save('bank.xls')
        else:
            wb_copy.get_sheet(0).write(i, 8, "不通过")
            wb_copy.save('bank.xls')
        # 断言
        self.assertEqual(result, h)

    @data(*da_saveMoney)
    @unpack
    def testSaveMoney(self, a, b, c, d):
        result = bank_saveMoney(a, b)

        if result == c:  # 让程序自动将测试结果写到excel表里。
            wb_copy.get_sheet(1).write(d, 3, "通过！")
            wb_copy.save('bank.xls')
        else:
            wb_copy.get_sheet(1).write(d, 3, "不通过")
            wb_copy.save('bank.xls')
        # 断言
        self.assertEqual(result, c)

    @data(*da_takeMoney)
    @unpack
    def testTakeMoney(self, a, b, c, d, e):
        result = bank_takeMoney(a, b, c)

        if result == d:  # 让程序自动将测试结果写到excel表里。
            wb_copy.get_sheet(2).write(e, 4, "通过！")
            wb_copy.save('bank.xls')
        else:
            wb_copy.get_sheet(2).write(e, 4, "不通过")
            wb_copy.save('bank.xls')
        # 断言
        print(d)
        self.assertEqual(result, d)

    @data(*da_transformMoney)
    @unpack
    def testTransformMoney(self, a, b, c, d, e, f):
        result = bank_transformMoney(a, b, c, d)

        if result == e:  # 让程序自动将测试结果写到excel表里。
            wb_copy.get_sheet(3).write(f, 5, "通过！")
            wb_copy.save('bank.xls')
        else:
            wb_copy.get_sheet(3).write(f, 5, "不通过")
            wb_copy.save('bank.xls')
        # 断言
        self.assertEqual(result, e)

    @data(*da_selectUser)
    @unpack
    def testSelectUser(self, a, b, c, d):
        result = bank_selectUser(a, b)

        if result == c:  # 让程序自动将测试结果写到excel表里。
            wb_copy.get_sheet(4).write(d, 3, "通过！")
            wb_copy.save('bank.xls')
        else:
            wb_copy.get_sheet(4).write(d, 3, "不通过")
            wb_copy.save('bank.xls')
        # 断言
        self.assertEqual(result, c)


def send_email(name):
    sender = '2068098717@qq.com'
    passwd = "ikunjjxfsrpiedjj"
    receivers = '2068098717@qq.com'
    subject = '工商银行管理系统测试'

    # 构造邮件对象
    message = MIMEMultipart()
    message['From'] = Header("shinensama", 'utf-8')
    message['To'] = Header("Jason", 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    message_content = "附件为测试结果"
    message.attach(MIMEText(message_content, 'plain', 'utf-8'))

    # 添加附件
    with open(name, mode='rb') as f:
        attfile = f.read()
    att1 = MIMEApplication(attfile)
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="%s"' % name
    message.attach(att1)

    # 发送邮件
    try:
        smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
        smtpObj.login(sender, passwd)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException as cause:
        print("无法发送邮件", cause)


send_email("bank.xls")
