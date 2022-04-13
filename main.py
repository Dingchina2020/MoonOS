#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python 3
# @Author: ahqo

"""
writeen by ahqo
data: Dec. 12th,2021
license BSD 3-Clause "New" or "Revised" License
"""
import tkinter
from tkinter import *
import logging.config
from logging.handlers import RotatingFileHandler
import os
import time
import wx
from wx.html2 import WebView
from module_search import *
from module_vip import *

# Configure file
logging.config.fileConfig('logs/logging.config')
logger = logging.getLogger("LOGGING")

logger.info("[INFO] 程序版本：MoonOS v.1.0.0")
logger.info("[INFO] 加载界面...")
time.sleep(0.0034)
logger.info("[INFO] 加载完成！")

'''定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大0.1M'''
Rthandler = RotatingFileHandler('logs/external_file.log', maxBytes=0.1 * 1024 * 1024, backupCount=5)

Rthandler.setLevel(logging.INFO)
Rthandler.setLevel(logging.ERROR)
logging.basicConfig(
    format='asctime:        %(asctime)s \n'
           'filename_line:  %(filename)s_[line:%(lineno)d] \n'
           'level:          %(levelname)s \n'
           'message:        %(message)s \n',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='./logs/external_file.log',
    filemode='a')  # 如果模式为'a'，则为续写（不会抹掉之前的log）
logging.getLogger('').addHandler(Rthandler)
# 日志记录区
# =======================================
# 界面区
'''None'''
# 加载动画
# ---------------------------------------
# 主程序


root = Tk()
root.title(" MoonOS v.1.0.0")
root.geometry("1280x800")
root.iconbitmap(r"photos/icon.ico")
photo = PhotoImage(file="photos/bg.png")
background_label = Label(root, image=photo)
background_label.pack()

'''
The window is centered by obtaining the screen size of the current device.
'''
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
ww = 1024
wh = 800
x = (sw - ww) / 2
y = (sh - wh) / 2
root.geometry("%dx%d+%d+%d" % (ww, wh, x, y))


def videovipcrack():
    logger.info("[INFO] 打开vip破解助手")
    vip_vip = Vip()
    vip_vip.loop()


def search():
    logger.info("[INFO] 打开百度")
    app = APP()
    app.loop()


def neizhiliulanqi():
    class MyHtmlFrame(wx.Frame):
        def __init__(self, parent, title):
            wx.Frame.__init__(self, parent, -1, title, size=(1024, 768))
            web_view = WebView.New(self)
            web_view.LoadURL("https://www.baidu.com/")

    logger.info("[INFO] 打开内置浏览器")
    app = wx.App()
    frm = MyHtmlFrame(None, "Moon网页浏览器")
    frm.Show()
    app.MainLoop()


def gettime():
    timestr = time.strftime("%H:%M:%S")  # 获取当前的时间并转化为字符串
    lb.configure(text=timestr)
    root.after(1000, gettime)  # 每隔1s调用函数gettime自身获取时间


def computer():
    logger.info("[INFO] 打开Computer")
    top = Toplevel()
    top.title('Computer')

    v1 = StringVar()
    e1 = Entry(top, textvariable=v1, width=10)
    e1.grid(row=1, column=0, padx=1, pady=1)

    Button(top, text='------------------\n------------------', width=60, height=5).grid(row=1, column=1, padx=1, pady=1)

    ww_1 = 600
    wh_1 = 400
    x_1 = (sw - ww) / 2
    y_1 = (sh - wh) / 2
    top.geometry("%dx%d+%d+%d" % (ww_1, wh_1, x_1, y_1))


def quitif():
    logger.info("[INFO] 退出...")
    root.quit()


def takeoff():
    logger.info("[INFO] 关机...")
    os.system('shutdown /s /t 0')


def aboutwriter():
    logger.info("[INFO] 打开ABOUT_WRITER")
    top = Toplevel()
    top.title('关于作者')
    top.geometry("680x400")

    l_1 = Label(top, text='About the author:', font=('Arial', 28), width=30, height=2)
    l_1.pack()
    l_2 = Label(top, text='Ding Li', font=('Copperplate Gothic Bold', 12), width=30, height=2)
    l_2.pack()
    l_3 = Label(top, text='----A middle school student,contact Python in 2020', font=('Eras Medium ITC', 12), height=2)
    l_3.pack()
    l_4 = Label(top, text='Made by Ding Li', font=('Meiryo', 18), height=2)
    l_4.pack()
    l_5 = Label(top, text='Note:Independently produced by Ding Li', font=('Meiryo', 10), height=2)
    l_5.pack()

    v1 = StringVar()
    e1 = Entry(top, textvariable=v1, width=10)
    e1.grid(row=1, column=0, padx=1, pady=1)

    ww_1 = 600
    wh_1 = 400
    x_1 = (sw - ww) / 2
    y_1 = (sh - wh) / 2
    top.geometry("%dx%d+%d+%d" % (ww_1, wh_1, x_1, y_1))


pic_1 = PhotoImage(file=r"photos/computer.png")
exe_computer = Button(root, image=pic_1, command=computer)
exe_computer.place(x=45, y=60)

pic_2 = PhotoImage(file=r"photos/exit.png")

exe_TakeOff = Button(root, text='关机', padx=11, pady=11, command=takeoff)
exe_TakeOff.place(x=100, y=680)

exe_quitif = Button(root, text='退出', image=pic_2, command=quitif)
exe_quitif.place(x=45, y=680)

exe_aboutwriter = Button(root, text='关于作者', padx=11, pady=11, command=aboutwriter)
exe_aboutwriter.place(x=900, y=680)

exe_liulanqi = Button(root, text='百度', padx=11, pady=11, command=neizhiliulanqi)
exe_liulanqi.place(x=45, y=110)

exe_search = Button(root, text='浏览器', padx=11, pady=11, command=search)
exe_search.place(x=45, y=160)

exe_vip = Button(root, text='vip视频破解助手', padx=11, pady=11, command=videovipcrack)
exe_vip.place(x=45, y=210)

lb = tkinter.Label(root, text='', font=("黑体", 40))
lb.place(x=420, y=400)
gettime()


root.mainloop()
