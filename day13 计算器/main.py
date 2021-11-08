"""
    1.加载所有的测试用例
    2.执行用例并生成测试报告
"""
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

from HTMLTestRunner import HTMLTestRunner
import unittest
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 1.加载所有用例
tests = unittest.defaultTestLoader.discover(r"C:\Users\20680\Desktop\python自动化测试\demo\day13 单元测试", pattern="Test*.py")

# 2.创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title="计算器的测试报告",
    description="这是综合测试报告",
    verbosity=1,
    stream=open(file="calculator.html", mode="w+", encoding="utf-8")
)

# 3.执行用例
runner.run(tests)


# 4.任务： 使用邮件发送附件，把报告发送给我
def send_email(name):
    sender = '2068098717@qq.com'
    passwd = "ikunjjxfsrpiedjj"
    receivers = '2068098717@qq.com'
    subject = '计算器综合测试'

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


send_email("calculator.html")
