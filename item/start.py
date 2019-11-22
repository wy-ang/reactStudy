# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QWidget
from item.UI.reactStudy import Ui_ReactStudy
from PyQt5.QtCore import QThread, pyqtSignal
import os, subprocess

cwd = os.getcwd()
pathList = []
cmdList = []

class startAddItemthread(QThread):
    # 定义线程需要用到的信号
    startItem = pyqtSignal()
    def __init__(self):
        super().__init__()

    '''
    @description: 执行线程相关代码
    '''
    def run(self):
        # 执行bash命令
        file = open(cwd + '\config.txt', mode='r')
        try:
            while True:
                line = file.readline()
                if line:
                    if 'ItemPath ' in line:
                        item = line.split('ItemPath ')
                        pathList.append(item[1])
                else:
                    break
        finally:
            file.close()
        pathStr = 'cd /d ' + eval("".join(pathList)) + ' && npm start';

        startPopen = subprocess.Popen(pathStr, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        while True:
            data = startPopen.stdout.readline()
            if data != b'':
                print(data)

        startPopen.stdout.close()
        startPopen.wait()

        # cmd = os.system(pathStr)
        # print(cmd)
        # 发送信号
        self.startItem.emit()

class Window(QWidget, Ui_ReactStudy):
    # 判断启动按钮是否可用 #
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 绑定按钮槽函数
        self.startBtn.clicked.connect(self.clickStartBtn)
        # 声明线程实例
        self.startItemThread = startAddItemthread()

    '''
    @description: 点击开始按钮，启动线程
    '''
    def clickStartBtn(self):
        # 启动线程
        self.startItemThread.start()
        self.startBtn.setEnabled(False)
        self.msgView.append('正在启动进程...')
        self.stateColor.setStyleSheet('background-color: rgb(0, 170, 0)')

    def clickStopBtn(self):
        stopPopen = subprocess.call('taskkill /f /im node.exe', shell=True)
        if (stopPopen == 0):
            self.msgView.append('进程已停止...')
        else:
            self.msgView.append('没有运行中的进程...')
        self.stateColor.setStyleSheet('background-color: rgb(255, 0, 0)')
        self.startBtn.setEnabled(True)

    def clickRestartBtn(self):
        self.msgView.append('正在重启进程...')
        self.stateColor.setStyleSheet('background-color: rgb(0, 170, 0)')
        self.startBtn.setEnabled(False)

    def clickPathConfigBtn(self):
        os.startfile(cwd + '\config.txt')

    def clickUpdateBtn(self):
        print('更新')
    def clickBuildBtn(self):
        print('构建')

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv);
    window = Window();
    window.show()
    sys.exit(app.exec_())

    # file = open(cwd + '\config.txt', mode='r')
    # try:
    #     while True:
    #         line = file.readline()
    #         if line:
    #             if 'ItemPath ' in line:
    #                 item = line.split('ItemPath ')
    #                 self.msgView.append(item[1])
    #         else:
    #             break
    # finally:
    #     file.close()
    # path = config.split('ItemPath ')
    # self.msgView.append(path)
    # cmd = os.system('cd /d '+ path +' && npm start')
    # print(cmd)
    # startPopen = subprocess.Popen('cd /d ' + path + ' && npm start', stdout=subprocess.PIPE,
    #                               stderr=subprocess.STDOUT, shell=True)
    # for startLine in iter(startPopen.stdout.readline, r''):
    #     print(startLine)
    # startPopen.stdout.close()
    # startPopen.wait()