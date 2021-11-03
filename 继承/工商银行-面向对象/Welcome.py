from LogicalFunction import LogicalFunction
logicalFunction = LogicalFunction()

# 欢迎模板
welcome = '''
***********************************
*      中国工商银行账户管理系统       *
***********************************
*               选项              *
'''

welcome_item = '''*              {0}.{1}             *'''


class Welcome:
    def print_welcome(self):
        print(welcome, end="")
        keys = logicalFunction.bank_choice.keys()
        for i in keys:
            print(welcome_item.format(i, logicalFunction.bank_choice[i]))
        print("**********************************")