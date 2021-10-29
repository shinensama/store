import xlrd
from dbutils import create
from dbutils import table_exists
from dbutils import update
from dbutils import select

wb = xlrd.open_workbook(filename=r"C:\Users\20680\Desktop\python自动化测试\Python\day9\2020年每个月的销售情况.xlsx",
                        encoding_override=True)
# 选项卡数量
wb_len = len(wb.sheets())

for i in range(wb_len):
    table_exists_param = str(i+1) + "月"
    time = table_exists(table_exists_param)
    if time == 0:
        create(i+1)
    st = wb.sheet_by_index(i)
    rows = st.nrows
    for j in range(1, rows):
        date = st.row_values(j)
        sql1 = "select * from %s月 where 日期 = %s"
        param1 = [i+1, date[0]]
        date2 = select(sql1, param1)
        if len(date2) == 0:
            sql = "insert into %s月 value(%s, %s, %s, %s, %s)"
            param = [i+1, date[0], date[1], date[2], date[3], date[4]]
            update(sql, param)


