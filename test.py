# coding:utf-8
import os, sys
import tkinter as tk
import subprocess
import threading

cmdStart = 'cd /d D:\dev\Xin_RC_front && npm start'
cmdStop = 'cd /d D:\dev\Xin_RC_front && npm stop'
startPopen = subprocess.Popen(cmdStart, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
stopPopen = subprocess.Popen(cmdStop, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

def start():
    for startLine in iter(startPopen.stdout.readline, b''):
        t.insert('insert', startLine)
    startPopen.stdout.close()
    startPopen.wait()

def stop():
    for stopLine in iter(stopPopen.stdout.readline, b''):
        t.insert('insert', stopLine)
    stopPopen.stdout.close()
    stopPopen.wait()

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

root.mainloop()