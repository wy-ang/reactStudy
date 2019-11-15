# -*- coding: utf-8 -*-

# 导入需要的包和模块
import sys
from PyQt5.QtWidgets import qApp, QMainWindow, QPushButton, QApplication, QWidget, QLabel
from Init import Window

# # 创建应用程序对象
app = QApplication(sys.argv)
# # 操作控件

# ## 读取样式
with open('styles.qss') as style:
    qApp.setStyleSheet(style.read())

# ## 创建控件
window = Window()

label = QLabel(window)
label.setText('测试')

button = QPushButton(window)
button.setText('启动')
button.setProperty('attr', 'open')
button.move(100, 100)

button = QPushButton(window)
button.setText('关闭')
button.setProperty('attr', 'close')
button.move(200, 100)

# 展示控件
window.show()
# # 应用程序的执行，进入到消息循环
sys.exit(app.exec())