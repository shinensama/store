# 总销售量
grossSales = (10+60+43+63+63+120+72+69+35+140+90+24+45+25+60+129+10+43+63+60+63+60+58+140+48+43+57+10+63+78)
# 羽绒服总销量
downCoat = (10+69+140+10+10)
# 牛仔裤总销量
jeans = (60+72+35+90+60+60+140)
# 风衣总销量
windCoat = (43+25+43+60+43+78)
# 皮草总销量
fur = (63+24+63+57)
# T恤总销量
tShirt = (63+45+129+63+58+48+63)
# 衬衫总销量
shirt = (120)

# 总销售额
list1 = [253.6,86.3,96.8,135.9,65.8,49.3]
list2 = [downCoat,jeans,windCoat,fur,tShirt,shirt]

sum = 0
for i in range(6):
    test1 = list1[i]
    test2 = list2[i]
    result = list1[i] * list2[i]
    sum += result

print("总销售额:",sum)
# 平均每日销售数量
print("平均每日销售数量：",(grossSales/30))
print("羽绒服月销量占比：",(downCoat/grossSales))
print("牛仔裤月销量占比：",(jeans/grossSales))
print("风衣月销量占比：",(windCoat/grossSales))
print("皮草月销量占比：",(fur/grossSales))
print("T恤月销量占比：",(tShirt/grossSales))
print("衬衫月销量占比：",(shirt/grossSales))

