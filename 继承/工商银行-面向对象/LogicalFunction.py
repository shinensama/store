from Utils import Utils
from Dbutils import Dbutils

utils = Utils()
dbutils = Dbutils()


class LogicalFunction:
    # 银行库
    __bank_name = "中国工商银行昌平支行"
    bank_choice = {"1": "开户", "2": "存钱", "3": "取钱", "4": "转账", "5": "查询", "6": "Bye"}  # 银行业务选项
    # 开户成功的信息模板
    myinfo = '''
        \033[0;32;40m
        ------------账户信息------------
        账号：{account}
        姓名：{username}
        密码：{password}
        地址：
            国家：{country}
            省份：{province}
            街道：{street}
            门牌号：{door}
        账户余额：{money}
        注册时间：{registerDate}
        注册银行名：{bank_name}
        -------------------------------
        \033[0m
    '''

    def getBankName(self):
        return self.__bank_name

    # 判断是否存在该银行选项
    def isExists(self, chose, data):
        if chose in data:
            return True
        return False

    # 通过账号获取账户信息
    def findByAccount(self, account):
        sql9 = "select * from user where account = %s"
        param9 = [account]
        data9 = dbutils.select(sql9, param9)
        if len(data9) == 1:
            return data9
        return None

    # 银行的开户方法
    def bank_addUser(self, username, password, country, province, street, door, money):
        # 查询是否已满
        sql = "select count(*) from user"
        param = []
        data = dbutils.select(sql, param)
        if len(data) >= 100:
            return 3

        # 查询是否存在
        sql1 = "select * from user where username = %s"
        param1 = [username]
        data = dbutils.select(sql1, param1)
        if len(data) != 0:
            return 2

        # 插入数据
        sql2 = "insert into user value(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"
        param2 = [utils.getRandom(), username, password, country, province, street, door, money, self.__bank_name]
        dbutils.update(sql2, param2)
        return 1

    # 银行的存钱方法
    def bank_saveMoney(self, ac, money):
        if self.findByAccount(ac) is not None:
            sql6 = "update user set money = money + %s where account = %s "
            param6 = [money, ac]
            dbutils.update(sql6, param6)
            return True
        return False

    # 银行的取钱功能
    def bank_takeMoney(self, account, password, money):
        uname = self.findByAccount(account)
        if uname is not None:
            if int(uname[0][2]) == int(password):
                if uname[0][7] < money:
                    return 3
                else:
                    sql10 = "update user set money = money - %s where account = %s "
                    param10 = [money, account]
                    dbutils.update(sql10, param10)
                    return 0
            else:
                return 2
        else:
            return 1

    # 银行的转账功能
    def bank_transformMoney(self, outputaccount, inputaccount, outputpassword, outputmoney):
        uname = self.findByAccount(outputaccount)
        uname2 = self.findByAccount(inputaccount)
        if uname is None or uname2 is None:
            return 1
        else:
            if int(outputpassword) != uname[0][2]:
                return 2
            else:
                if int(outputmoney) > uname[0][7]:
                    return 3
                else:
                    self.bank_takeMoney(outputaccount, outputpassword, outputmoney)
                    self.bank_saveMoney(inputaccount, outputmoney)
                    return 0

    # 银行的查询功能
    def bank_selectUser(self, account, password):
        uname = self.findByAccount(account)

        if uname is not None and len(uname) != 0:
            data11 = self.findByAccount(account)
            if int(password) == int(data11[0][2]):
                user = data11
                print(self.myinfo.format(account=account,
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
                print("用户密码错误！")
        else:
            print("该用户不存在！")
