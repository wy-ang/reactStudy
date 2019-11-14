# -*- coding: utf-8 -*-

"""
PyQt5 tutorial

In this example, we determine the event sender
object.

author: py40.com
last edited: 2017年3月
"""

# 导入需要的包和模块
import sys
from PyQt5.QtWidgets import qApp, QMainWindow, QPushButton, QApplication, QWidget, QLabel
from Init import Window

# # 创建应用程序对象
app = QApplication(sys.argv)
# # 操作控件

# ## 创建控件
window = Window()
# 展示控件
window.show()
# # 应用程序的执行，进入到消息循环
sys.exit(app.exec())