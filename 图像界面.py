#-*- coding:utf-8 -*-
#使用Python内置的库tkinter来编写GUI界面
from tkinter import *
from tkinter import messagebox
#从Frame派生一个Application类，Appleication是所有Widget的父容器
class Application(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.grid()
        self.createWidgets()
#在GUI中，每个Button、Label、输入框等，都是一个Widget。Frame则是可以容纳其他Widget的Widget
# ，所有的Widget组合起来就是一棵树。
    def createWidgets(self):
        #创建一个Label
        self.helloLabel = Label(self, text = 'hello,world!')
        self.helloLabel.grid()

        self.nameInput = Entry(self)
        self.nameInput.grid()

        #创建一个Button
        self.quitButton = Button(self,text = 'ensure',command = self.hello)
        self.quitButton.grid()
        self.quitButton = Button(self, text='quit', command=self.quit)
        self.quitButton.grid()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('messageinfo','hello %s'% name)

app = Application()
#设置窗口标题
app.master.title("The first python GUI code of \'hello, world!\'")
#主消息循环
app.mainloop()