#coding=utf-8
import urllib
import urllib2
#import sp
#import shipin1
from urllib2 import Request,urlopen
from urllib2 import URLError,HTTPError
from bs4 import BeautifulSoup
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')



def getHtml(url):

    page=urllib.urlopen(url)
    html=page.read()
    return html
def getMp4(html):
    #r=r"href='(.*?)'"
    #<li class="list_item current" id="g00242a7jyn" tl="5648" data-title="狼人星球第三集：女王淘汰战，谁将首个淘汰？">
#<span class="_base_title" title="狼人星球第三集：女王淘汰战，谁将首个淘汰？">狼人星球第三集：女王淘汰战，谁将首个淘汰？</span>
    r=r'<span class="_base_title" title="(.*?)"'
    #re_swf = re.compile('<div class="rank-item"><div class="num">(.*?)</div><div class="content clearfix"><a href=".*?" target="_blank"><div class="preview"><img data-img="" src="(.*?)webp" loaded="loaded" style="opacity: 1;"></div></a>')
##
    #r = r'<h1 class="video_title" title="(.*?)"'
   # re_swf=re.compile(r)
    swfList=re.findall(r,html)

    if swfList:
        return swfList[0]

    else:
        print('none')


#print('https://v.qq.com/x/page/h03425k44l2.html\\\\n \\\\https://v.qq.com/x/cover/dn7fdvf2q62wfka/m0345brcwdk.html\\\\n \\\\http://v.qq.com/cover/2/2iqrhqekbtgwp1s.html?vid=c01350046ds')

#web = shipin1.urllist

#web = raw_input('请输入网址:')

#web = "https://v.qq.com/x/page/h03425k44l2.html"

#lists=['https://v.qq.com/x/cover/pl52h7b4j4dn3nl.html','https://v.qq.com/x/cover/pl52h7b4j4dn3nl.html','https://v.qq.com/x/cover/k1zmlg3oyhf0r9w.html']

#--------------爬取页面--------------
url = 'https://v.qq.com/x/cover/bv226axbgi84w4z/w0534qnxd49.html'
#'https://v.qq.com/x/cover/pl52h7b4j4dn3nl.html'#  https://v.qq.com/x/cover/pl52h7b4j4dn3nl.htmlhttps://v.qq.com/x/cover/k1zmlg3oyhf0r9w.html https://v.qq.com/x/cover/k1zmlg3oyhf0r9w/f0532pim6v9.html
#lol https://v.qq.com/x/cover/cycfbucy203qzue/q0178gq5vnc.html      http://v.qq.com/vplus/loltv    https://v.qq.com/x/cover/srzo8wzskebws7w/n03709cqgh7.html  https://v.qq.com/x/cover/szld8cxwkeiaen8/t0518su192b.html
##   https://v.qq.com/x/cover/b0d77zix7bly6ct/u0510a2uoe3.html(0810)  https://v.qq.com/x/page/b0527fce7qk.html

page = urllib.urlopen(url).read()

#r=r'href="https://v.qq.com/x/cover(.*?)html"'
r=r'href="/x/cover(.*?)html"'
#/x/cover/66fiuuwpgkumphj/n00230900f5.html
urllists = re.findall(r,page)
#print urllists
for urllist1 in urllists:
    urllist = "https://v.qq.com/x/cover"+urllist1+"html"
    html=getHtml(urllist)
    title = getMp4(html)

    title1 = title.decode("utf8")

    web = urllist

    if re.search(r'vid=',web):
        patten =re.compile(r'vid=(.*)')
        vid=patten.findall(web)
        vid=vid[0]
        print(vid)

    else:
        newurl = (web.split("/")[-1])
        vid =newurl.replace('.html', ' ')
    #从视频页面找出vid

    getinfo='http://vv.video.qq.com/getinfo?vids={vid}&otype=xlm&defaultfmt=fhd'.format(vid=vid.strip())
    def getpage(url):
        req = Request(url)
        user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit'
        req.add_header('User-Agent', user_agent)
        try:
            response = urlopen(url)
        except HTTPError as e:
            print('The server couldn\\\\t fulfill the request.')
            print('Error code:', e.code)
        except URLError as e:
            print('We failed to reach a server.')
            print('Reason:', e.reason)
        html = response.read().decode('utf-8')
        return(html)
    #打开网页的函数

    a = getpage(getinfo)

    soup = BeautifulSoup(a, "html.parser")
    for e1 in soup.find_all('url'):
        ippattent = re.compile(r"((?:(2[0-4]\d)|(25[0-5])|([01]?\d\d?))\.){3}(?:(2[0-4]\d)|(255[0-5])|([01]?\d\d?))")
        if re.search(ippattent,e1.get_text()):
            ip=(e1.get_text())
    for e2 in soup.find_all('id'):
        idpattent = re.compile(r"\d{5}")
        if re.search(idpattent,e2.get_text()):
        #id = ()
            id=e2.get_text()
    filename = vid.strip()+'.p'+id[2:]+'.1.mp4'
    #找到ID和拼接FILENAME

    getkey='http://vv.video.qq.com/getkey?format={id}&otype=xml&vt=150&vid={vid}&ran=0%2E9477521511726081\&charge=0&filename={filename}&platform=11'.format(id=id,vid=vid.strip(),filename=filename)
    #利用getinfo中的信息拼接getkey网址
    b = getpage(getkey)

    key=(re.findall(r'<key>(.*)<\/key>',b))

    videourl=ip+filename+'?'+'vkey='+key[0]

    print('视频播放地址 '+videourl)

    content_stream = urllib2.urlopen(videourl)
    print("----")
    content = content_stream.read()
    print("++++")
    vF = open("E:\\shipin_wz\\%s.mp4" % title1,'wb')
    print("===")
    vF.write(content)
    print(">>>>")
    vF.close()
    content_stream.close()


#urllib.urlretrieve(videourl)

#https://v.qq.com/x/page/a03994w71py.html
#https://v.qq.com/x/cover/66fiuuwpgkumphj.html
