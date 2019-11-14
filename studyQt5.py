# -*- coding: utf-8 -*-

"""
PyQt5 tutorial

In this example, we determine the event sender
object.

author: py40.com
last edited: 2017年3月
"""

# 导入需要的包和模块
import sys  # 内建系统模块
# qApp 全局变量 type: QApplication
from PyQt5.QtWidgets import qApp, QMainWindow, QPushButton, QApplication, QWidget, QLabel

# # 创建应用程序对象
# ## sys.argv 当通过命令行执行这个程序的时候，可以设定一种功能（接受命令行传递的参数，来执行不同的业务逻辑）
app = QApplication(sys.argv)

# # 操作控件

# ## 创建控件
# 控件如果没有父控件，系统会自动把它当作顶层控件（窗口）
# 并且系统会自动设置图标，标题，最大化，最小化，关闭等特性
window = QWidget()
# ## 设置控件
window.setWindowTitle('社会我洋哥，人狠话不多')
window.resize(300, 500)
# 将控件添加到顶层控件
label = QLabel(window)
label.setText('hello world')
label.move(120, 220)

# 展示控件
# 刚创建一个控件后，如果该控件没有父控件，默认不会被展示，需要手动调用show()才会显示
window.show()

# # 应用程序的执行，进入到消息循环
# ## sys.exit()退出（返回退出码）
# ## app.exec() 让程序开始执行，并且进入到消息循环（无限循环），用来检测整个程序所接收到的用户的交互信息等
sys.exit(app.exec())