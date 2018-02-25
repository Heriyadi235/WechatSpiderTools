# -*- coding: utf-8-*-
import re
from urllib import request
from bs4 import BeautifulSoup
import time
import os
#这是爬虫的核心操作
def html2text(arurl):
    #head = {}
    #head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
    #req = request.Request(arurl, headers=head)
    res = request.urlopen(arurl)
    htmlstr = res.read()
    #print(htmlstr)
    soup = BeautifulSoup(htmlstr, "lxml")
    title = soup.title.get_text('\n')
    #print(title)
    info = soup.em.get_text('')
    #print(info)
    text=''
    #text = soup.section.get_text('\n')#第一个BUG
    #改抓这个标签试试<div class="rich_media_content " id="js_content">
    a=soup.find_all('div',{'class':'rich_media_content '})
    #a=soup.find_all('section')
    for i in a:
        text = text + i.get_text('\n')
    '''
    for content in soup.find_all(name = 'div'):
        if content.get('class')==['rich_media_content ']:
            text = text + content.get_text() + '\n'#在txt中，要用"\r\n"才能换行，get_text()用来获取标签内里面的文本内容，"strip=True"能去除文本内容前后多余的空格
    '''
    #textlist = soup.find_all(name='section')
    #for each in textlist:
        #print(each.get('data-src'))
        #print(each.get('data-src'))
        #f.write(each.get('data-src')+ '\n')
    #print(text)
    #r=''
    #print('text:' + text)
    filename = re.sub('[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+','',title)
    #print('手动断点')
    #with open('E:\\spidersour\\' + info + filename + '.txt', 'w+', encoding='utf-8') as f:
    os.makedirs('E:\\spidersour\\results\\'+filename)
    with open('E:\\spidersour\\results\\'+filename+"\\" + info +' '+ filename + '.txt', 'w+', encoding='utf-8') as f:
        f.write(title + '\n' )
        f.write(info + '\n' )
        f.write(text + '\n' )
        #f.write('图片链接' + '\n')
        #f.write(arurl + '\n' )
        #图片这要重写
        imglist = soup.find_all(name='img')

        for i in imglist:
                #print(each.get('data-src'))
            #f.write(str(i.get('data-src'))+ '\n')
            #num = 0
            img_data = str(i.get('data-src'))

            #print('手动断点')
            #print(img_data)
            if img_data == 'None':
                continue
                #判断图片类型
            if img_data[4] == 's':
                img_type = img_data[28:31]
            else:
                img_type = img_data[27:30]
            #print(img_type)
            #保存到文件夹
            response = request.urlopen(img_data)
            img = response.read()

            with open('E:\\spidersour\\results\\'+filename+"\\"+img_data[81:90]+"."+str(img_type), 'wb') as pic:
                pic.write(img)
            #num += 1
        print('图片爬取完毕')
        f.write('原文链接' + '\n')
        f.write(arurl + '\n')
        f.close()
        #print('手动断点')
    #print(info)
    print('文章' + title + ' 已保存到本地')
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
            time.sleep(1)
        print("爬取完成")
    except Exception as e:
        print(str(e))
