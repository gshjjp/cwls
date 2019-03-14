# -*- coding: UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup

if __name__ == "__main__":
    target_url = "https://www.biqukan.com/1_1094/5403177.html"
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    dl_req = request.Request(url=target_url,headers=head)
    dl_res = request.urlopen(dl_req)
    dl_html = dl_res.read().decode('gbk','ignore')

    soup_texts = BeautifulSoup(dl_html,'lxml')
    texts = soup_texts.find_all('div id="content" class_="showtxt"')
    soup_text = BeautifulSoup(str(texts).replace('','\n'),'lxml')
    #soup_text1 = soup_text.replace_with('\xa0','')
    print(soup_text.div.get_text.replace('\xa0',''))
    #print(soup_text1)


