import random


def interface():
    print("***********************")
    print("*   中国工商银行        *")
    print("***********************")
    print("*     1、开户          *")
    print("*     2、存钱          *")
    print("*     3、取钱          *")
    print("*     4、转账          *")
    print("*     5、查询          *")
    print("*     6、再见          *")
    print("***********************")


# 空字典
bank = {'欧斯': {'account': 98835406, 'password': '1', 'country': '中国', 'province': '昌平', 'street': '001', 'door': '001',
               'money': 100},
        '斯麦卢': {'account': 98835406, 'password': '1', 'country': '中国', 'province': '昌平', 'street': '001', 'door': '001',
                'money': 100}
        }
# 'F': {'account': 98835406, 'password': '1', 'country': '中国', 'province': '昌平', 'street': '001', 'door': '001',
# 'money': 0}
bank_name = "M73迪迦银行"


# 调用的函数元素是一一对应的，不是名称对应
def bank_add(account, username, password, country, province, street, door):
    if username in bank:  # 名字  重名
        return 2
    elif len(bank) >= 100:  # 大于100个用户
        return 3
    else:  # 正常添加用户
        bank[username] = {
            "account": account,
            "password": password,
            "country": country,
            "province": province,
            "street": street,
            "door": door,
            "money": 0,
            "bank_name": bank_name
        }
        return 1


def useradd():
    account = random.randint(10000000, 99999999)  # 账号随机产生的
    username = input("请输入您的姓名")
    password = input("请输入你的密码")
    print("下面请输入您的地址：")
    country = input("\t\t请输入你的国家")
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    add = bank_add(account, username, password, country, province, street, door)
    if add == 3:
        print("数据库已满，请到光之国银行开户")
    elif add == 2:
        print("用户已存在")
    elif add == 1:
        print("恭喜你添加用户成功，以下是您的账户信息：")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))


# 存钱
def storage():
    username1 = input("请输入您的账户名：")
    add = storage_1(username1)
    if not add:
        print("无此账户，请确认账户是否输入正确")
    elif add:
        depositAmount = int(input("请输入存入金额:"))
        bank[username1]["money"] = bank[username1]["money"] + depositAmount
        print("存储成功")


def storage_1(username1):
    if username1 not in bank:
        return False
    elif username1 in bank:
        return True


def drawMoney():
    username1 = input("请输入您的账户名：")
    password1 = input("请输入密码：")
    drawMoney = int(input("请输入取钱金额："))
    add = drawMoney_1(username1, password1, drawMoney)
    if add == 1:
        print("无此账户，请确认账户是否输入正确")
    elif add == 2:
        print("密码输入错误")
    elif add == 3:
        print("账户余额不足！")
    else:
        bank[username1]["money"] = bank[username1]["money"] - drawMoney
        print("取钱成功！")


def drawMoney_1(username1, password1, drawMoney):
    if username1 not in bank:
        return 1
    else:
        if password1 != bank[username1]["password"]:
            return 2
        else:
            if drawMoney > bank[username1]["money"]:
                return 3


def transferAccounts():
    username1 = input("请输入转出的账户名：")
    username2 = input("请输入转入的账户名：")
    password1 = input("请输入转出账户的密码：")
    drawMoney = int(input("请输入转账金额："))
    add = transferAccounts_1(username1, username2, password1, drawMoney)
    if add == 1:
        print("转入账户或转出账户不存在，请再检查一下！")
    elif add == 2:
        print("密码输入错误")
    elif add == 3:
        print("转出账户余额不足！")
    elif add == 0:
        print("转账成功")


def transferAccounts_1(username1, username2, password1, drawMoney):
    if (username1 or username2) not in bank:
        return 1
    else:
        if password1 != bank[username1]["password"]:
            return 2
        else:
            if drawMoney > bank[username1]["money"]:
                return 3
            else:
                bank[username1]["money"] -= drawMoney
                bank[username2]["money"] += drawMoney
                return 0


def inquire():
    username1 = input("请输入要查询的的账户名：")
    password1 = input("请输入要查询账户的密码：")
    if username1 not in bank:
        print("该用户不存在")
    else:
        if password1 != bank[username1]["password"]:
            print("密码错误")
        else:
            print("以下是您的账户信息：")
            info = '''
                        ------------个人信息------------
                        用户名:%s
                        账号：%s
                        密码：*****
                        国籍：%s
                        省份：%s
                        街道：%s
                        门牌号：%s
                        余额：%s
                        开户行名称：%s
                    '''
            print(info % (
                username1, bank[username1]["account"], bank[username1]["country"], bank[username1]["province"],
                bank[username1]["street"], bank[username1]["door"], bank[username1]["money"], bank_name))


while True:
    interface()
    index = int(input("请输入您的操作："))
    if index == 1:
        useradd()
    elif index == 2:
        storage()
    elif index == 3:
        drawMoney()
    elif index == 4:
        transferAccounts()
    elif index == 5:
        inquire()
    elif index == 6:
        print("退出系统")
        break
