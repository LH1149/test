# 1、显示窗体
# import sys
# from PyQt5 import QtWidgets
# #导入了必要的模块。这些基本控件位于PyQt5.QtWidgets模块中。

# app = QtWidgets.QApplication(sys.argv)
# # 每个PyQt5应用程序都需要创建一个application对象。sys.argv是从命令行传入的参数列表。Python脚本可以从shell中运行。这是一种控制脚本启动的方式。

# widget = QtWidgets.QWidget()
# # 控件QWidget是QtPy5中所有UI对象的基类。我们调用了QWidget的默认构造器。默认构造器没有parent参数。没有parent的控件称为窗体(window)。

# widget.resize(250,150)
# # resize()方法用于设置控件的尺寸。它宽250px高150px。widget.move(300, 300)方法将控件移动到坐标为x=300, y=300的位置

# widget.setWindowTitle('simple')
# # 这里设置了窗体的标题。标题在标题栏中显示。

# widget.show()
# # show()方法将控件显示在屏幕上。控件要先在内存中创建，然后在屏幕上显示。

# sys.exit(app.exec_())
# # 最后我们进入了application的主循环。事件处理从这里开始。主循环从窗体系统中接收事件，并将事件分发给控件。在调用exit()方法或主控件销毁时主循环会停止。sys.exit()方法确保可以干净地退出。系统可以感知到程序是如何退出的。
# # 注意exec_()方法的下划线。由于exec是python中的关键字，所以使用exec_()。





# # 2、窗体添加图标
# import sys
# from PyQt5.QtGui import QIcon
# from PyQt5 import QtWidgets
# # setGeometry()设置了控件的位置与尺寸。前两个参数是窗体的x,y坐标，第三个与第四个参数设置了窗体的宽度与高度。
# # 实际上它合并了resize()与move()方法。最后一个方法设置了应用的图标。我们需要创建一个QIcon对象，QIcon接受要显示的图标的路径作为参数。


# class Icon(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         QtWidgets.QWidget.__init__(self, parent)

#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle("Icon")
#         self.setWindowIcon(QIcon("D:/CSR/wallpaper/1.jpg"))


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     icon = Icon()
#     icon.show()
#     sys.exit(app.exec_())





# # 3、tooltip(提示框)的显示
# import sys
# from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
# from PyQt5.QtGui import QFont

# class Example(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         QToolTip.setFont(QFont("Microsoft YaHei", 10))
#         # 这个静态方法为tooltip设置了10px的雅黑字体。
#         self.setToolTip("This is a <b>QWidget</b> widget")
#         # 我们调用setToolTip()方法为控件创建提示消息。消息可以使用富文本格式。

#         btn = QPushButton("Button", self)
#         btn.setToolTip("This is a <b>QPushButon</b> widget")
#         btn.resize(btn.sizeHint())
#         btn.move(50, 50)

#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle("Tooltips")
#         self.show()



# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())



# # 4、窗体的关闭
# import sys
# from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
# from PyQt5.QtCore import QCoreApplication

# # yQt5中的事件处理系统采用signal&slot(信号槽)机制。当我们点击按钮时会发出clicked信号。
# # slot可以是Qt slot或任何Python的callable对象。QCoreApplication包含了主事件循环；它可以处理并分发事件。
# # instance()方法返回它的当前实例。QCoreApplication是由QApplication创建的。clicked信号连接到可以退出程序的quit()方法。
# # 这个过程由两个对象完成：发送者与接收者。发送者是PushButton，接收者是QApplication对象。

# class Example(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):

#         qbtn = QPushButton("Quit", self)
#         qbtn.clicked.connect(QCoreApplication.instance().quit)
#         qbtn.resize(qbtn.sizeHint())
#         qbtn.move(50, 50)

#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle("Quit button")
#         self.show()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())





# # 5、对话框
# import sys
# from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

# class Example(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle("MEssage box")
#         self.show()

#     def closeEvent(self, event):
#         reply = QMessageBox.question(self, "Message", "Are you sure to quit?", QMessageBox.Yes |
#                                      QMessageBox.No, QMessageBox.No) #这里的第二个NO为对话框首选项，即目前首选为NO
#         if reply == QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())





# # 6、窗体居中
# import sys
# from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
# # QtGui.QDesktopWidget提供了关于用户桌面的信息，包括屏幕尺寸。

# class Example(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.resize(250, 150)
#         self.center()
#         # center()方法中包含了窗体居中的代码。

#         self.setWindowTitle('Center')
#         self.show()

#     def center(self):
#         qr = self.frameGeometry()
#         # 得到一个指定了主窗体形状的矩形。
#         cp = QDesktopWidget().availableGeometry().center()
#         # 指出显示器的屏幕分辨率并根据分辨率找出屏幕的中心点。
        
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())
#         # 将窗体的左上角移动到矩形qr的左上角，窗体与矩形重合，从而将窗体置于屏幕中心。


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())






# 7、合并功能--自制
# 窗口显示+窗体添加图标+提示框+窗体关闭+对话框+窗体居中

# (1)导入需要的包
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget)
from PyQt5.QtCore import QCoreApplication

# (2)创建窗体
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont("SansSerif", 10))
        # 设置字体
        self.setToolTip("This is a <b>QWidget</b> widget")
        # 窗体提示语
        # 按键1--提示框
        btn1 = QPushButton("Button1", self)
        btn1.setToolTip("This is a <b>QPushButon</b> widget")
        btn1.resize(btn1.sizeHint())
        btn1.move(50, 50)

        # 按键2--窗口关闭
        btn2 = QPushButton("Quit", self)
        btn2.setToolTip("This is a <b>Quit</b> widget")
        btn2.clicked.connect(QCoreApplication.instance().quit)
        btn2.resize(btn2.sizeHint())
        btn2.move(50, 90)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("犇阳傻子鉴定")
        self.center()
        self.Icon()
        self.show()


    # 对话框
    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Message", "犇阳是傻逼吗?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # 窗体居中
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    # 图标
    def Icon(self):
        self.setWindowIcon(QIcon("D:/CSR/wallpaper/1.jpg"))

# (3)运行主循环
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())