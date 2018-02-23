# -*- coding: utf-8-*-
import re
from urllib import request
from bs4 import BeautifulSoup
import time
#这是爬虫的核心操作
def html2text(arurl):
    #head = {}
    #head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
    #req = request.Request(arurl, headers=head)
    res = request.urlopen(arurl)
    htmlstr = res.read()
    #print(htmlstr)
    title = "untitled"
    info = "noinfo"
    text = "nope"
    soup = BeautifulSoup(htmlstr, "lxml")
    title = soup.title.get_text('\n')
    info = soup.em.get_text('')
    text = soup.section.get_text('\n')
    #r=''
    filename = re.sub('[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+','',title)
    with open('E:\\spidersour\\' + info +' ' + filename + '.txt', 'w+', encoding='utf-8') as f:
        f.write(title + '\n' )
        f.write(info + '\n' )
        f.write(text + '\n' )
        f.write('图片链接' + '\n')
        imglist = soup.find_all(name='img')
        i = 0
        for each in imglist:
            if i < 2:
                i += 1
                continue
                #print(each.get('data-src'))
            f.write(each.get('data-src')+ '\n')
            i += 1
            if i > 4:
                break
        print('图片爬取完毕')
        f.close()
    #print(info)
    print(title+'已保存到本地')
    print('==========================================================================================================')

    #print(soup)
if __name__=='__main__':
    try:
        print("开始爬取")
        for line in open('E:\spidersour\list.txt'):
            print("文章地址")
            print(line)
            arurl = line
            html2text(arurl)
            time.sleep(3)
        print("爬取完成")
    except Exception as e:
        print(str(e))
