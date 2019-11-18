from PyQt5.QtWidgets import QApplication, QWidget
from item.UI.reactStudy import Ui_ReactStudy
import os, subprocess

cwd = os.getcwd()

class Window(QWidget, Ui_ReactStudy):
    # 判断启动按钮是否可用 #
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def clickStartBtn(self):
        file = open(cwd + '\config.txt', mode='r')
        path = file.read()
        cmd = os.system('cd /d '+ path +' && npm start')
        print(cmd)
        # startPopen = subprocess.Popen('cd /d ' + path + ' && npm start', stdout=subprocess.PIPE,
        #                               stderr=subprocess.STDOUT, shell=True)
        # for startLine in iter(startPopen.stdout.readline, r''):
        #     print(startLine)
        # startPopen.stdout.close()
        # startPopen.wait()

        self.stateColor.setStyleSheet('background-color: rgb(0, 170, 0)')
        self.startBtn.setEnabled(False)

    def clickStopBtn(self):
        stopPopen = subprocess.call('taskkill /f /im node.exe', shell=True)
        if (stopPopen == 0):
            self.msgView.append('进程已停止...')
        else:
            self.msgView.append('进程停止失败...')
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