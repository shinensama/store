from threading import Thread
import time

eggTart = 0
cashier = 0
first_time = time.time()


class production(Thread):
    username = ""
    count = 0

    def run(self) -> None:  # 生产
        global eggTart
        global cashier
        while True:
            if time.time() - first_time < 30:
                if eggTart < 500:
                    eggTart += 1
                    self.count += 1
                    cashier -= 1.5
                else:
                    time.sleep(3)

            else:
                salary = self.count * 1.5
                print(self.username, "共生产了", self.count, "个蛋挞，今日的工资为:", salary)
                break


class purchase(Thread):
    username = ""
    money = 3000
    count = 0

    def run(self) -> None:
        global eggTart
        global cashier
        while True:
            if time.time() - first_time < 30:
                if self.money > 2:
                    if eggTart > 0:
                        eggTart -= 1
                        self.money -= 3
                        self.count += 1
                        cashier += 3
                    else:
                        time.sleep(2)
            else:
                print(self.username, "共抢购了", self.count, "个蛋挞，个人还剩金额为：", self.money)
                break


chef1 = production()
chef2 = production()
chef3 = production()
chef1.username = "卫宫士郎"
chef2.username = "玉藻猫"
chef3.username = "小麻雀"
customer1 = purchase()
customer2 = purchase()
customer3 = purchase()
customer4 = purchase()
customer5 = purchase()
customer6 = purchase()
customer1.username = "阿尔托莉雅·潘德拉贡"
customer2.username = "黑呆"
customer3.username = "白枪呆"
customer4.username = "黑枪呆"
customer5.username = "C呆"
customer6.username = "迷之女主角X"

chef1.start()
chef2.start()
chef3.start()
customer1.start()
customer2.start()
customer3.start()
customer4.start()
customer5.start()
customer6.start()
time.sleep(35)
print("今日营业利润为:", cashier)
