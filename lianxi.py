#coding=utf8
from selenium import webdriver
from time import sleep

file_info = open('info.txt','r')

value = file_info.readlines()

file_info.close()

for serch in value:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.baidu.com")
    username = serch.split(',')[0]
    password = serch.split(',')[1]
    print(username,password)

    driver.find_element_by_id('kw').send_keys(serch.split(',')[0])
    driver.find_element_by_id('su').click()
    sleep(5)
    driver.quit()








