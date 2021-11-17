import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import xlrd
from selenium import webdriver
from unittest import TestCase
from ddt import ddt
from ddt import data
from xlutils.copy import copy
from InitPage import InitPage
from LoginOperation import LoginOpera
import time

wb = xlrd.open_workbook(filename=r"C:\Users\20680\Desktop\python自动化测试\demo\2.自动化\day3 自动化框架\HKR.xlsx",
                        encoding_override=True)
wb_len = len(wb.sheets())
wb_copy = copy(wb)

loginSuccessData = []
loginErrorData = []

for i in range(wb_len):
    st = wb.sheet_by_index(i)
    rows = st.nrows
    for j in range(1, rows):
        data1 = st.row_values(j)
        if i == 0:
            loginSuccessData.append([data1[0], data1[1], data1[2], j])
        elif i == 1:
            loginErrorData.append([data1[0], data1[1], data1[2], j])


@ddt
class TestHkr(TestCase):
    global wb_copy

    # 在所有用例执行前执行
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8081/HKR")
        self.driver.maximize_window()

    # 在所有用例执行后执行
    def tearDown(self) -> None:
        self.driver.quit()

    @data(*loginSuccessData)
    def testLoginSuccess(self, testdata):
        username = testdata[0]
        password = testdata[1]
        expect = testdata[2]

        login = LoginOpera(self.driver)

        # 执行登陆的三项操作
        login.login(username, password)

        # 获取实际结果
        result = login.getLoginSuccessResult()

        time.sleep(3)

        if result == expect:
            wb_copy.get_sheet(0).write(testdata[3], 3, "通过")
            wb_copy.sava('HKR.xls')
        else:
            wb_copy.get_sheet(0).write(testdata[3], 3, "不通过")
            wb_copy.sava('HKR.xls')

        # 断言
        self.assertEqual(expect, result)

    @data(*loginErrorData)
    def testLoginError(self, testdata):
        username = testdata[0]
        password = testdata[1]
        expect = testdata[2]

        login = LoginOpera(self.driver)

        # 执行登陆的三项操作
        login.login(username, password)

        # 获取实际结果
        result = login.getLoginErrorResult()

        time.sleep(3)

        if result == expect:
            wb_copy.get_sheet(1).write(testdata[3], 3, "通过")
            wb_copy.sava('HKR.xls')
        else:
            wb_copy.get_sheet(1).write(testdata[3], 3, "不通过")
            wb_copy.sava('HKR.xls')

        # 断言
        self.assertEqual(expect, result)


def send_email(name):
    sender = 'XXXXXXX@qq.com'
    passwd = "XXXXXXXXX"
    receivers = 'XXXXXXXX@qq.com'
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


send_email("HKR.xls")
