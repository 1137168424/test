from selenium import webdriver
import time

driver = webdriver.Chrome()   # 初始化，选择Chrome
driver.implicitly_wait(10) # 隐式等待，最多等待10s

driver.get("http://erp.lemfix.com/login.html") # 打开网站
driver.maximize_window() # 最大化
# time.sleep(3)#等待，默认为秒
# driver.get("https://www.xidian.edu.cn/?")

# 前进后退刷新
# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)
# driver.refresh()

# 退出
# driver.quit()#关闭驱动 session关闭
# driver.close() # 关闭当前窗口，不会退出会话

# 点击、传值
driver.find_element_by_id("username").send_keys("test123")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("btnSubmit").click()

# xpath
page_text = driver.find_element_by_xpath("//b[text()='柠檬ERP']").text
print("页面标题是：{}".format(page_text))

page_user = driver.find_element_by_xpath('//div[@class="pull-left info"]//p').text
if page_user == '测试用户':
    print("该用户是{}".format(page_user))
else:
    print("不是测试用户")


# 点击零售出库
driver.find_element_by_xpath('//span[text()="零售出库"]').click()

# frame
P_id = driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id")
F_id = P_id + "-frame"

# 1、通过id进行iframe切换
# driver.switch_to.frame(F_id)
# 2、通过xpath进行切换
# driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@id="{}"]'.format(F_id)))
# 3、通过frame下标
driver.switch_to.frame(1)

# 搜索314
driver.find_element_by_id("searchNumber").send_keys("259")
# 点击搜索
driver.find_element_by_xpath('//span[text()="查询"]').click()
time.sleep(2)
# 打印编号
num = driver.find_element_by_xpath('//table[@class="datagrid-btable"]//td[@field="number"]//div').text
print(num)



