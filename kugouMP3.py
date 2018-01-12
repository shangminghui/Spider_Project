import requests,re,os,time,parser,html5lib
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib
from urllib import request
from tkinter import *
from selenium.webdriver.common.keys import Keys




def geturl():
    url=txt2.get('0.0',END)
    mp3=dldmp3(url)
    txt3.delete('0.0',END)
    txt3.insert(INSERT,"下载成功！！！")

def dldmp3(url):
    dirver=webdriver.Chrome()
    dirver.get(url)
    time.sleep(3)
    pagesource=dirver.page_source
    bsobj=BeautifulSoup(pagesource,'html5lib')
    music=bsobj.find('div',class_='mainPage').find_all('audio')
    title=bsobj.find('div',class_='songName').find_all('span')
    for t in title:
        songname=t.get_text()
    for m in music:
        # print(mp3['src'])
        if os.path.exists(path):
            flag=0
        else:
            os.makedirs(path)
        os.chdir(path)
        mp3=m['src']
        filename=songname+'.mp3'
        if os.path.exists(filename):
            # flag=0
            print ("此歌曲名已经存在，不需要重新下载")
        else:
            # flag=1
            urllib.request.urlretrieve(mp3,filename)
            print (filename + ">>>下载成功！")
        dirver.close()


if __name__ == '__main__':
    path = 'D:/kugou/Pydownload'
    root = Tk()
    root.title('酷狗音乐下载器')
    txt1 = Text(root, width=60, height=1)
    txt2 = Text(root, width=60, height=5)
    txt3 = Text(root, width=60, height=2)
    label=Label(txt1,text="输入歌曲播放地址(歌曲下载地址为D:/kugou/Pydownload)",width=59, height=1)
    label.pack()
    btn = Button(root, text='下载', command=geturl,width=10, height=4)
    btn.grid(row=1, column=0)
    txt1.grid(row=0, column=1)
    txt2.grid(row=1, column=1)
    txt3.grid(row=2, column=1)
    root.mainloop()




# dirver=webdriver.Chrome()
# dirver.get("http://www.kugou.com")
# assert u"酷狗音乐 - 就是歌多" in dirver.title
# elem=dirver.find_element_by_tag_name("input")
# elem.clear()
# elem.send_keys(u"周杰伦")
# elem.send_keys(Keys.RETURN)
# time.sleep(3)
# assert u"周杰伦." not in dirver.page_source
# dirver.close()