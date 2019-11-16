# coding:utf-8
import os, sys
import tkinter as tk
import subprocess
import threading

cmdStart = 'cd /d D:\dev\manhole && npm start'
cmdStop = 'taskkill /f /im node.exe'

def start():
    startPopen = subprocess.Popen(cmdStart, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    for startLine in iter(startPopen.stdout.readline, r''):
        t.insert('insert', startLine)
    startPopen.stdout.close()
    startPopen.wait()

def stop():
    stopPopen = subprocess.call(cmdStop, shell=True)
    if(stopPopen==0):
        t.insert('insert', '服务已停止...\n');
    else:
        t.insert('insert', '服务停止失败...\n');
# 解决点击按钮卡死的情况
def thread(func, *args):
    '''将函数打包进线程'''
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()
    # 阻塞--卡死界面！
    # t.join()

root = tk.Tk()  # 主窗口
root.title('reactStudy')  # 窗口标题
root.geometry('500x700')  # 窗口尺寸

t = tk.Text(root)  # 创建文本框，用户可输入内容
t.pack()

tk.Button(root, text='启动',width=15, height=2, command=lambda :thread(start)).pack()
tk.Button(root, text='停止',width=15, height=2, command=lambda :thread(stop)).pack()

#进入消息循环
root.mainloop()