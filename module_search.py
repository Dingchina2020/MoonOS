#!/usr/bin/env python
# -*- coding: utf-8 -*-


# url解析 vip视频播放地址的模块 做url加密的
from urllib import parse
import tkinter as tk
import webbrowser
import urllib.parse


class APP:
    # 魔术方法
    # 初始化用的
    def __init__(self, width=500, height=300):
        self.w = width
        self.h = height
        self.title = '百度搜索'
        # 软件名
        self.root = tk.Tk(className=self.title)

        # vip视频播放地址 StringVar() 定义字符串变量
        self.url = tk.StringVar()

        # 定义选择哪个播放源
        self.v = tk.IntVar()

        # 默认为1
        self.v.set(1)

        # Frame空间
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)

        # 控件内容设置
        group = tk.Label(frame_1, text='目前仅支持百度搜索', padx=10, pady=10)
        tb = tk.Radiobutton(frame_1, text='百度', variable=self.v, value=1, width=10, height=3)
        lable = tk.Label(frame_2, text='请输入查找内容：')

        # 输入框声明
        entry = tk.Entry(frame_2, textvariable=self.url, highlightcolor='cyan', highlightthickness=1, width=35)
        play = tk.Button(frame_2, text='查找', font=('楷体', 12), fg='Purple', width=2, height=1, command=self.video_play)

        # 控件布局 显示控件在你的软件上
        frame_1.pack()
        frame_2.pack()

        # 确定控件的位置 wow 行 column 列
        group.grid(row=0, column=0)
        tb.grid(row=0, column=1)
        lable.grid(row=0, column=0)
        entry.grid(row=0, column=1)

        # ipadx x方向的外部填充 ipady y方向的内部填充
        play.grid(row=0, column=3, ipadx=10, ipady=10)

    def video_play(self):
        # 拿到用户输入的视频网址
        ip = self.url.get()

        # 视频连接加密
        ip = parse.quote_plus(ip)
        port = f'https://baidu.com/s?wd={ip}'

        # 用浏览器打开网址
        webbrowser.open(port)

    # 启动GUI程序的函数
    def loop(self):
        self.root.resizable(True, True)
        self.root.mainloop()


if __name__ == "__main__":
    app = APP()
    app.loop()
