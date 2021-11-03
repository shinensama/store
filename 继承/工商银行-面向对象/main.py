from Utils import Utils
from LogicalFunction import LogicalFunction
from Dbutils import Dbutils
from Welcome import Welcome

utils = Utils()
logicalFunction = LogicalFunction()
dbutils = Dbutils()
welcome = Welcome()


# 开户方法
def addUser():
    username = utils.inputHelp("用户名")
    password = utils.inputHelp("密码")
    country = utils.inputHelp("居住地址：1.国家：")
    province = utils.inputHelp("省份")
    street = utils.inputHelp("街道")
    door = utils.inputHelp("门牌号")
    money = utils.inputHelp("银行卡余额", "int")

    # 调用银行的开户方法完成开户操作  返回 1 2 3
    status = logicalFunction.bank_addUser(username, password, country, province, street, door, money)
    # 判断1   2   3
    if status == 1:
        sql8 = "select * from user where username = %s"
        param8 = [username]
        user = dbutils.select(sql8, param8)
        print("恭喜开户成功！以下是您的开户信息：")
        print(logicalFunction.myinfo.format(account=user[0][0],
                                            username=username,
                                            password=user[0][2],
                                            country=user[0][3],
                                            province=user[0][4],
                                            street=user[0][5],
                                            door=user[0][6],
                                            money=user[0][7],
                                            registerDate=user[0][8],
                                            bank_name=user[0][9]
                                            ))
    elif status == 2:
        print("该用户已经存在！请携带证件到其他银行办理！谢谢！！！！！")
    elif status == 3:
        print("银行库已满！请携带证件到其他银行办理！谢谢！！！！！")


# 存钱
def saveMoney():
    account = utils.inputHelp("账号")
    m = utils.inputHelp("存入的金额", "int")

    flag = logicalFunction.bank_saveMoney(account, m)

    if flag:
        print("存储成功!您的个人信息为：")
        sql = "select * from user where account = %s"
        param = [account]
        user = dbutils.select(sql, param)
        print(logicalFunction.myinfo.format(account=user[0][0],
                                            username=user[0][1],
                                            password=user[0][2],
                                            country=user[0][3],
                                            province=user[0][4],
                                            street=user[0][5],
                                            door=user[0][6],
                                            money=user[0][7],
                                            registerDate=user[0][8],
                                            bank_name=user[0][9]
                                            ))
    else:
        print("对不起，您的个人信息不存在！请先开户后再次操作！")


# 取钱
def takeMoney():
    account = utils.inputHelp("账户")
    password = utils.inputHelp("密码")
    tmoney = utils.inputHelp("取出金额", "int")

    f = logicalFunction.bank_takeMoney(account, password, tmoney)

    if f == 1:
        print("该用户不存在！")
    elif f == 2:
        print("密码错误！")
    elif f == 3:
        print("取款金额不足！")
    elif f == 0:
        print("取款成功！")
        logicalFunction.bank_selectUser(account, password)


# 转账功能
def transformMoney():
    output = utils.inputHelp("转出的账号")
    input = utils.inputHelp("转入的账号")
    outputpass = utils.inputHelp("转出的密码")
    outputmoney = utils.inputHelp("要转出的金额", "int")

    f = logicalFunction.bank_transformMoney(output, input, outputpass, outputmoney)

    if f == 1:
        print("转出或转入的账号不存在！")
    elif f == 2:
        print("输入密码错误！")
    elif f == 3:
        print("转账金额不足！")
    elif f == 0:
        print("转账成功！")
        print("您的个人信息：")
        logicalFunction.bank_selectUser(output, outputpass)


# 查询账户方法
def selectUser():
    account = utils.inputHelp("账号")
    password = utils.inputHelp("密码")

    logicalFunction.bank_selectUser(account, password)


# 核心程序
while True:

    welcome.print_welcome()
    chose = utils.inputHelp("选项")
    if logicalFunction.isExists(chose, logicalFunction.bank_choice):
        if chose == "1":
            addUser()
        elif chose == "2":
            saveMoney()
            pass
        elif chose == "3":
            takeMoney()
            pass
        elif chose == "4":
            transformMoney()
        elif chose == "5":
            selectUser()
            pass
        elif chose == "6":
            print("Bye,Bye您嘞！！！！")
            break
    else:
        print("不存在该选项，别瞎弄！")
