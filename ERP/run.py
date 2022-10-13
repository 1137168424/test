from selenium import webdriver
from .import def_comman
from .import test_data


url = test_data.url[0]
username = test_data.username[0]
password = test_data.password[0]
s_key = test_data.s_key[0]

driver = webdriver.Chrome()   # 初始化，选择Chrome
driver.implicitly_wait(10) # 隐式等待，最多等待10s

n = def_comman.open(driver=driver,url=url,username=username,password=password,s_key=s_key)
print(n)