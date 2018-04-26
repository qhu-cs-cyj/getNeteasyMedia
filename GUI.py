# -*- coding: UTF-8 -*-
# import urllib
# import urllib2
# import re
import threading
from selenium import webdriver
import pyperclip
from Tkinter import *

data = None
lock = threading.Lock()

def getDataFromNeteasy(url):
    global data
    driver = webdriver.PhantomJS()
    driver.get(url)
    lock.acquire()
    # data=driver.page_source
    data = driver.find_elements_by_tag_name("video")
    # print(type(data))
    if data:
        data = data
    else:
        data = driver.find_element_by_tag_name("audio")
    if data:
        data = data.get_attribute("src")
    else:
        data = "There is no video or audio"
    t2.delete(0.0, END)
    t2.insert('end', data)
    lock.release()
    driver.quit()

def getMedia():
    global data
    # url = "https://c.open.163.com/mob/audio.htm?plid=ADERF24NJ&mid=ADERF24NF"
    url = e.get()
    try:
        _thread = threading.Thread(target=getDataFromNeteasy, args=(url,))
        _thread.setDaemon(True)
        _thread.start()
        # thread.start_new_thread(getDataFromNeteasy,(url))
    except:
        print "Error: unable to start thread"



def copyData():
    pyperclip.copy(data)

rootWindow = Tk()
rootWindow.title("网易云课堂媒体文件提取");
rootWindow.geometry('500x120')

var = StringVar()    # 这时文字变量储存器
label = Label(rootWindow,text="网址(URL)",font=('Arial', 12), width=15, height=2)

e = Entry(rootWindow,width=45)
# t1 = Text(rootWindow,height=2,width=45)
t2 = Text(rootWindow,height=2,width=45)

btn1 = Button(rootWindow,text='获取',width=10,height=1,command=getMedia)
btn2 = Button(rootWindow,text='copy',width=5,height=1,command=copyData)

label.place(x=0,y=10)
e.place(x=120,y=15)
t2.place(x=120,y=60)
btn1.place(x=20,y=60)
btn2.place(x=445,y=60)
rootWindow.mainloop()                 # 进入消息循环

