# -*- coding: utf-8 -*-
import os, subprocess
from PyQt5.QtWidgets import QApplication, QWidget
from item.UI.reactStudy import Ui_ReactStudy
from PyQt5.QtCore import QThread, pyqtSignal
# from item.watchFile import FileEventHandler

# 获取当前工作目录
cwd = os.getcwd()
# 项目路径
pathList = []
cmdList = []

class startAddItemthread(QThread):
    # 定义线程需要用到的信号
    startItem = pyqtSignal()
    def __init__(self):
        super(startAddItemthread, self).__init__()
        self.isStart = True
    '''
    @description: 执行线程相关代码
    '''
    def run(self):
        if self.isStart:
            # 清空原有路径
            pathList = []
            # 读取路径配置文件
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

            # 启动node进程
            for list in pathList:
                pathStr = 'cd /d ' + eval("".join(list)) + ' && npm start -d'
                subprocess.Popen(pathStr, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            # 发送信号
            self.startItem.emit()
            self.sleep(1)

class Window(QWidget, Ui_ReactStudy):
    # 判断启动按钮是否可用 #
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 绑定按钮槽函数
        self.startBtn.clicked.connect(self.clickStartBtn)
        self.stopBtn.clicked.connect(self.clickStopBtn)
        # 声明线程实例
        self.startItemThread = startAddItemthread()

    '''
    @description: 点击开始按钮，启动线程
    '''
    def clickStartBtn(self):
        # 启动线程
        self.startItemThread.isStart = True
        self.startItemThread.start()
        self.stateColor.setStyleSheet('background-color: rgb(0, 170, 0)')
        self.startBtn.setEnabled(False)
        self.msgView.append('正在启动进程...')

    def clickStopBtn(self):
        # 结束线程
        self.startItemThread.isStart = False
        # 结束node进程
        stopPopen = subprocess.call('taskkill /f /im node.exe', shell=True)
        if (stopPopen == 0):
            self.msgView.append('进程已停止...')
        else:
            self.msgView.append('没有运行中的进程...')
        self.stateColor.setStyleSheet('background-color: rgb(255, 0, 0)')
        self.startBtn.setEnabled(True)

    def clickRestartBtn(self):
        # 重启进程
        self.startItemThread.isStart = True
        self.startItemThread.start()
        self.stateColor.setStyleSheet('background-color: rgb(0, 170, 0)')
        self.startBtn.setEnabled(False)
        self.msgView.append('正在重启进程...')

    def clickPathConfigBtn(self):
        # 打开路径配置文件
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
    #                 pathList.append(item[1])
    #         else:
    #             break
    # finally:
    #     file.close()
    #pathStr = 'cd /d ' + eval("".join(pathList)) + ' && npm start -d';
    # cmd = os.system(pathStr)
    # print(cmd)
    # startPopen = subprocess.Popen(pathStr, stdout=subprocess.PIPE,
    #                               stderr=subprocess.STDOUT, shell=True)
    # for line in iter(startPopen.stdout.readline, b''):
    #     print(line)
    #     cmdList.append(line)
    #     print(cmdList)
    # startPopen.stdout.close()
    # startPopen.wait()
