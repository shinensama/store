# 工具
import pymysql

host = "localhost"
user = "root"
password = "123456"
database = "bank"


class Dbutils:
    # 增，删，改
    def update(self, sql, param):
        con = pymysql.connect(host=host, user=user, password=password, database=database)
        cursor = con.cursor()

        cursor.execute(sql, param)

        con.commit()

        cursor.close()
        con.close()

    # 查
    def select(self, sql, param, mode="all", size=1):
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
