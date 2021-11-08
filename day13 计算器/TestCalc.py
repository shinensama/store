"""
    unittest:单元测试框架

    1.子类继承TestCase
    2.写测试用例:testXxxxx
    任务1：
        使用邮件发送测试报告
        温馨提示：用户名，密码（smtp授权码开通即可。）
    任务2：执行减法，乘法，除法，测试用例。并生成测试报告。
"""
from Calc import Calc
from unittest import TestCase


class TestCalc1(TestCase):

    def testAdd1(self):
        #
        a = 6
        b = 5
        s = 10

        calc = Calc()
        sum = calc.add(a, b)

        self.assertEqual(s, sum)

    def testAdd2(self):
        #
        a = -6
        b = -5
        s = -11

        calc = Calc()
        sum = calc.add(a, b)

        self.assertEqual(s, sum)

    def testAdd3(self):
        #
        a = -6
        b = 5
        s = -1

        calc = Calc()
        sum = calc.add(a, b)

        self.assertEqual(s, sum)

    def testAdd4(self):
        #
        a = 6
        b = -5
        s = 1

        calc = Calc()
        sum = calc.add(a, b)

        self.assertEqual(s, sum)


class TestCalc2(TestCase):

    def testMinus1(self):
        #
        a = 6
        b = 5
        s = 10

        calc = Calc()
        sum = calc.minus(a, b)

        self.assertEqual(s, sum)

    def testMinus2(self):
        #
        a = -6
        b = -5
        s = -11

        calc = Calc()
        sum = calc.minus(a, b)

        self.assertEqual(s, sum)

    def testMinus3(self):
        #
        a = -6
        b = 5
        s = -1

        calc = Calc()
        sum = calc.minus(a, b)

        self.assertEqual(s, sum)

    def testMinus4(self):
        #
        a = 6
        b = -5
        s = 1

        calc = Calc()
        sum = calc.minus(a, b)

        self.assertEqual(s, sum)


class TestCalc3(TestCase):

    def testMulti1(self):
        #
        a = 6
        b = 5
        s = 10

        calc = Calc()
        sum = calc.multi(a, b)

        self.assertEqual(s, sum)

    def testMulti2(self):
        #
        a = -6
        b = -5
        s = -11

        calc = Calc()
        sum = calc.multi(a, b)

        self.assertEqual(s, sum)

    def testMulti3(self):
        #
        a = -6
        b = 5
        s = -1

        calc = Calc()
        sum = calc.multi(a, b)

        self.assertEqual(s, sum)

    def testMulti4(self):
        #
        a = 6
        b = -5
        s = 1

        calc = Calc()
        sum = calc.multi(a, b)

        self.assertEqual(s, sum)


class TestCalc4(TestCase):

    def testDevision1(self):
        #
        a = 6
        b = 5
        s = 10

        calc = Calc()
        sum = calc.devision(a, b)

        self.assertEqual(s, sum)

    def testDevision2(self):
        #
        a = -6
        b = -5
        s = -11

        calc = Calc()
        sum = calc.devision(a, b)

        self.assertEqual(s, sum)

    def testDevision3(self):
        #
        a = -6
        b = 5
        s = -1

        calc = Calc()
        sum = calc.devision(a, b)

        self.assertEqual(s, sum)

    def testDevision4(self):
        #
        a = 6
        b = -5
        s = 1

        calc = Calc()
        sum = calc.devision(a, b)

        self.assertEqual(s, sum)
