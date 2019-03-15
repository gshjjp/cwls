#coding=utf8
from selenium import webdriver
from time import sleep
import csv


my_file = 'info.csv'
out = open(my_file,'r')
data = csv.reader(out,dialect='excel')
for line in data:

    for i in (0,1):
        print(line[i])
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("https://www.baidu.com")
        driver.find_element_by_id('kw').send_keys(line[i])
        driver.find_element_by_id('su').click()
        sleep(5)
        driver.quit()

out.close()












