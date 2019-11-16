# -*- coding: utf-8 -*-

# 导入需要的包和模块
import sys
from \
    PyQt5.QtWidgets \
    import \
    qApp, \
    QWidget,\
    QPushButton, \
    QApplication, \
    QLabel, \
    QTextEdit, \
    QVBoxLayout,\
    QHBoxLayout


cmdStart = 'cd /d D:\dev\manhole && npm start'
cmdStop = 'taskkill /f /im node.exe'

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('reactStudy')
        self.resize(395, 330)

# # 创建应用程序对象
app = QApplication(sys.argv)
# # 操作控件

# ## 读取样式
with open('styles.qss') as style:
    qApp.setStyleSheet(style.read())

# ## 创建控件
window = Window()

msg = QTextEdit(window)
msg.setEnabled(False)

openBtn = QPushButton(window)
openBtn.setText('启动')
openBtn.setProperty('attr', 'open')

def clickOpenBtn():
    msg.insertPlainText('正在启动服务...\n')
    openBtn.setStyleSheet('background-color:#ccc;border-color:#eee;color:#999')
    runStateBg.setStyleSheet('background-color:green;')
    openBtn.setEnabled(False)
openBtn.pressed.connect(clickOpenBtn)

closeBtn = QPushButton(window)
closeBtn.setText('停止')
closeBtn.setProperty('attr', 'close')

def clickCloseBtn():
    msg.insertPlainText('服务已停止...\n')
    openBtn.setStyleSheet('background-color:#FFF;border-color:#02b96c;color:#02b96c')
    runStateBg.setStyleSheet('background-color:#F00;')
    openBtn.setEnabled(True)
closeBtn.pressed.connect(clickCloseBtn)

butGroupLayout = QHBoxLayout()
butGroupLayout.addWidget(openBtn)
butGroupLayout.addWidget(closeBtn)

runStateText = QLabel(window)
runStateText.setText('node:')
runStateBg = QLabel(window)
runStateBg.setProperty('attr', 'state')
runStateEmpty = QLabel(window)

labelGroupLayout = QHBoxLayout()
labelGroupLayout.addWidget(runStateText)
labelGroupLayout.addWidget(runStateBg)
labelGroupLayout.addWidget(runStateEmpty)
labelGroupLayout.setStretchFactor(runStateText, 2)
labelGroupLayout.setStretchFactor(runStateBg, 1)
labelGroupLayout.setStretchFactor(runStateEmpty, 2)

updateBtn = QPushButton(window)
updateBtn.setText('更新')
updateBtn.setProperty('attr', 'update')

topLayout = QHBoxLayout()
topLayout.addLayout(labelGroupLayout)
topLayout.addLayout(butGroupLayout)

botLayout = QHBoxLayout()
botLayout.addWidget(msg)
botLayout.addWidget(updateBtn)



h_layout = QVBoxLayout()
h_layout.addLayout(topLayout)
h_layout.addLayout(botLayout)

window.setLayout(h_layout)

# 展示控件
window.show()
# # 应用程序的执行，进入到消息循环
sys.exit(app.exec())