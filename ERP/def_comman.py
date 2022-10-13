import time


def open(driver, url, username, password, s_key):
    driver.get(url)  # 打开网站
    driver.maximize_window()  # 最大化

    # 点击、传值
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("btnSubmit").click()

    # 点击零售出库
    driver.find_element_by_xpath('//span[text()="零售出库"]').click()

    # frame

    driver.switch_to.frame(1)

    # 搜索
    driver.find_element_by_id("searchNumber").send_keys(s_key)
    # 点击搜索
    driver.find_element_by_xpath('//span[text()="查询"]').click()
    time.sleep(2)
    # 打印编号
    num = driver.find_element_by_xpath('//table[@class="datagrid-btable"]//td[@field="number"]//div').text
    return num