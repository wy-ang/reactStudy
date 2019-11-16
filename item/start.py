from PyQt5.QtWidgets import QApplication, QWidget
from item.UI.reactStudy import Ui_ReactStudy

class Window(QWidget, Ui_ReactStudy):

    cmdStart = ''
    cmdStop = 'taskkill /f /im node.exe'

    # 判断启动按钮是否可用 #

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def clickStartBtn(self):
        cmdStart = self.pathConfig.toPlainText();
        if cmdStart:
            print(cmdStart)
        else:
            self.msgView.append('请输入路径！！！')
            return False
        self.msgView.append('正在启动进程...')
        self.stateColor.setStyleSheet('background-color: rgb(0, 170, 0)')
        self.startBtn.setEnabled(False)

    def clickStopBtn(self):
        self.msgView.append('进程已停止...')
        self.stateColor.setStyleSheet('background-color: rgb(255, 0, 0)')
        self.startBtn.setEnabled(True)

    def clickRestartBtn(self):
        cmdStart = self.pathConfig.toPlainText();
        if cmdStart:
            print(cmdStart)
        else:
            self.msgView.append('请输入路径！！！')
            return False
        self.msgView.append('正在重启进程...')
        self.stateColor.setStyleSheet('background-color: rgb(0, 170, 0)')
        self.startBtn.setEnabled(False)

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