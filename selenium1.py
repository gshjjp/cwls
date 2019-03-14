#-*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
if __name__ =='__main__':
    for num in range(1,20):
        if num==1:
            get_url = 'http://www.shuaia.net/index.html'
        else:
            get_url='http://www.shuaia.net/index_%d.html'%num

    #get_url = 'http://www.shuaia.net/index.html'
    head = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    req = requests.get(url=get_url,headers=head)
    req.encoding='utf-8'
    html = req.text
    bf = BeautifulSoup(html,'lxml')
    target_url = bf.find_all(class_='item-img')
    #print(target_url)
    list_url = []
    for each in target_url:
        list_url.append(each.img.get('alt')+'='+each.get('href'))
        #print(each.img.get('alt'))
        #print(list_url)
    print(list_url)
    #print(num)

