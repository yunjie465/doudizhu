import urllib.request
import tkinter
import tkinter.messagebox
from tkinter import ttk
import os

# 基本布局
window = tkinter.Tk()
window.title('斗地主工具')
window.geometry('300x250')

# 窗口图标
window.iconbitmap('v6.ico')

# 下拉框选择服务器
id_tishi = tkinter.Label(window, text='服务器', width=8, height=1)
id_tishi.place(x=10, y=10, anchor='nw')
server_choose = ttk.Combobox(window,width="18")
server_choose["value"] = ("外测1(47.102.143.13)", "外测2(47.103.129.2)")
server_choose.current(0)
server_choose.place(x=70, y=10, anchor='nw')

#账号提示和输入框
id_tishi = tkinter.Label(window, text='账号', width=8, height=1)
id_tishi.place(x=10, y=40, anchor='nw')
id_input = tkinter.Entry(window)
id_input.place(x=70, y=40, anchor='nw')

#物品ID和输入框
item_tishi = tkinter.Label(window, text='物品ID', width=8, height=1)
item_tishi.place(x=10, y=70, anchor='nw')
item_input = tkinter.Entry(window)
item_input.place(x=70, y=70, anchor='nw')

#数量和输入框
number_tishi = tkinter.Label(window, text='数量(整数)', width=8, height=1)
number_tishi.place(x=10, y=100, anchor='nw')
number_input = tkinter.Entry(window,width="14")
number_input.place(x=70, y=100, anchor='nw')
# 下拉框选择数量单位
addunit_choose = ttk.Combobox(window)
addunit_choose["value"] = ("个", "万","亿")
addunit_choose.current(0)
addunit_choose.place(x=175, y=100, anchor='nw',width="40")

# 添加道具
def add_item():
    server = server_choose.get()
    #服务器判断
    if server == "外测1(XXX)":
        server = 'XXX'
    elif server == "外测2(XXX)":
        server = 'XXX'
    #单位判断
    id = id_input.get()
    item = item_input.get()
    number = number_input.get()
    addunit=addunit_choose.get()
    if addunit=="个":
        url = (server + id + ',' + item + ',' + number)
    elif addunit == "万":
        url = (server + id + ',' + item + ',' + number+'0000')
    elif addunit == "亿":
        url = (server + id + ',' + item + ',' + number+'00000000')
    #request请求
    urllib.request.urlopen(url)
    tkinter.messagebox.showinfo('提示', '操作成功')


# 关闭服务器
def close_server():
    server = server_choose.get()
    if server == "外测1":
        server_close = 'XXX'
    elif server == "外测2":
        server_close = 'XXX'
    urllib.request.urlopen(server_close)
    tkinter.messagebox.showinfo('提示', '服务器' + server + '关闭成功')


# 抓取日志
def pull_log():
    pull=os.system("adb pull sdcard/Android/data/com.panda.hycm/files/log.txt .\log\log.txt")
    if pull==1:
        tkinter.messagebox.showinfo('提示', '抓取失败\n手机未连接或无log文件')
    elif pull==0:
        tkinter.messagebox.showinfo('提示', '抓取成功')


# 添加道具按钮
b = tkinter.Button(window, text='添加物品', width='8', height='2', command=add_item).place(x=70, y=130, anchor='nw')
# 关闭服务器按钮
c = tkinter.Button(window, text='关闭服务器', width='8', height='2', command=close_server).place(x=150, y=130, anchor='nw')
# pull日志
d = tkinter.Button(window, text='抓取斗地主日志', width='15', height='2', command=pull_log).place(x=70, y=180, anchor='nw')

window.mainloop()  # 显示窗口