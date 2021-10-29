# 工具
import re

import pymysql

host = "localhost"
user = "root"
password = "123456"
database = "2020销售数据"


# 新建表
def create(param):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()

    sql = "create table %s月(日期 varchar(50), 服装名称 VARCHAR(50), 单件价格 float(10,2), 本月库存数量 int, 日销售量 int)"
    param1 = [param]
    cursor.execute(sql, param1)

    con.commit()

    cursor.close()
    con.close()


# 查询表是否存在
def table_exists(table_name):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    sql = "show tables;"
    cursor.execute(sql)
    tables = [cursor.fetchall()]
    con.commit()

    cursor.close()
    con.close()
    table_list = re.findall('(\'.*?\')', str(tables))
    table_list = [re.sub("'", '', each) for each in table_list]
    if table_name in table_list:
        return 1  # 存在返回1
    else:
        return 0


# 增，删，改
def update(sql, param):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()

    cursor.execute(sql, param)

    con.commit()

    cursor.close()
    con.close()


# 查
def select(sql, param, mode="all", size=1):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()

    cursor.execute(sql, param)
    # 提取数据
    if mode == "one":
        return cursor.fetchone()
    elif mode == "all":
        return cursor.fetchall()
    elif mode == "many":
        return cursor.fetchmany(size)

    con.commit()

    cursor.close()
    con.close()
