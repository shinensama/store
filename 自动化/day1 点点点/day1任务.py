from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 京东
driver = webdriver.Chrome()
driver.maximize_window()
# driver.get('https://www.jd.com')
# driver.find_element(By.XPATH, "//*[@id='key']").send_keys("PS5")
# driver.find_element(By.XPATH, "//*[@aria-label='搜索' and @clstag='h|keycount|head|search_a']").click()
# time.sleep(3)
# driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[1]/div[1]/div[1]/div[3]/ul/li[1]/div[1]/div[3]/a').click()
# time.sleep(3)
# handles = driver.window_handles
# for handle in handles:
#     if handle != driver.current_window_handle:
#         driver.close()
#         driver.switch_to.window(handle)
# driver.find_element(By.XPATH, "//*[@id='InitCartUrl']").click()
# time.sleep(2)
#
# # 苏宁
# driver.get("https://www.suning.com")
# driver.find_element(By.XPATH, "//*[@id='searchKeywords']").send_keys("Switch")
# driver.find_element(By.XPATH, "//*[@id='searchSubmit']").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "/html/body/div[10]/div/ul/li[2]/div/div/div[1]/div/a").click()
# handles = driver.window_handles
# for handle in handles:
#     if handle != driver.current_window_handle:
#         driver.close()
#         driver.switch_to.window(handle)
# driver.find_element(By.XPATH, "//*[@id='addCart']").click()

# B站
driver.get("https://www.bilibili.com")
driver.find_element(By.XPATH, "//*[@x-webkit-grammar='builtin:translate']").send_keys("BV1EP4y1j7kV")
driver.find_element(By.XPATH, "//*[@class='nav-search-btn-text' or @class='bilifont bili-icon_dingdao_sousuo nav-search-submit']").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/ul/li[1]/div/div[1]/a").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[2])
driver.find_element(By.XPATH, "//*[@class='van-icon-videodetails_like']").click()
time.sleep(2)
driver.quit()
