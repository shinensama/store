"""
要求：
1、定义老手机类，有品牌属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的带一个Str类型参数的打电话的方法，内容为：“正在给xxx打电话...”
2、定义新手机类，继承老手机类，重写父类的打电话的方法，内容为2句话：“语音拨号中...”、“正在给xxx打电话...”要求打印“正在给xxx打电话...”这一句调用父类的方法实现，不能在子类的方法中直接打印；提供无返回值的无参数的手机介绍的方法，内容为：“品牌为：xxx的手机很好用...”
3、定义测试类，创建新手机对象，并使用该对象，对父类中的品牌属性赋值；
4、使用新手机对象调用手机介绍的方法；
5、使用新手机对象调用打电话的方法；
"""


class OldCellPhone:
    __brand = ""

    def setbrand(self, brand):
        self.__brand = brand

    def getbrand(self):
        return self.__brand

    def call(self, someone):
        print("正在给", someone, "打电话")


class NewPhone(OldCellPhone):

    def call(self, someone):
        print("语音拨号中...")
        super().call(someone)

    def show(self):
        print("品牌为：", self.getbrand(), "的手机很好用")


class test1:
    newPhone = NewPhone()
    newPhone.setbrand("vivo")
    newPhone.show()
    newPhone.call("朋友")


print("\n")

"""
要求：
1、定义厨师类，有姓名和年龄的属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的无参数的蒸饭方法；
2、定义厨师的子类，该类中要求只能写一个无返回值的无参数的炒菜的方法，其他的方法不能写；
3、定义厨师的子类的子类，重写所有父类的方法，每个方法的内容只需打印一句话描述方法的功能即可；(蒸饭，炒菜)
4、定义测试类，创建厨师的子类的子类（厨师的孙子类）对象，使用该对象，对厨师类中的姓名和年龄属性赋值，并获取赋值后的属性值打印到控制台上；
5、使用厨师的孙子类对象调用该对象除了getXxx与setXxx以外的其他方法；
"""


class chef:
    __name = ""
    __age = 0

    def setname(self, name):
        self.__name = name

    def getname(self):
        return self.__name

    def setage(self, age):
        self.__age = age

    def getage(self):
        return self.__age

    def steamRice(self):
        pass


class Cook(chef):
    def cooking(self):
        pass


class Apprentice(Cook):
    def steamRice(self):
        print("蒸饭")

    def cooking(self):
        print("炒菜")


class test2:
    cook = Cook()
    cook.setname("小福贵")
    cook.setage("17")
    print("厨师姓名：", cook.getname(), "年龄：", cook.getage())


print("\n")
"""
i.	人：年龄，性别，姓名。
"""


class Person:
    age = 0
    gender = ""
    name = ""


"""
ii.	现在有个工种，工人：年龄，性别，姓名 。行为：干活。请用继承的角度来实现该类。
"""


class Worker(Person):
    def labour(self):
        print(self.name, "正在干活")


"""
iii. 现在有学生这个工种，学生：年龄，性别，姓名，学号。行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。
"""


class student(Person):
    studentId = ""

    def learn(self):
        print(self.name, "正在学习")

    def sing(self):
        print(self.name, "正在唱歌")
