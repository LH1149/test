# 事件与信号
# 所有的GUI程序都是事件驱动的。
# 事件主要由用户触发，但也可能有其他触发方式：例如网络连接、window manager或定时器。当我们调用QApplication的exec_()方法时会使程序进入主循环。
# PyQt5有一个独特的signal&slot(信号槽)机制来处理事件。信号槽用于对象间的通信。
# signal在某一特定事件发生时被触发，slot可以是任何callable对象。当signal触发时会调用与之相连的slot。



# # Signals & slots：这是一个演示PyQt5信号槽的简单示例。
# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication)


# class Example(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         lcd = QLCDNumber(self)
#         sld = QSlider(Qt.Horizontal, self)

#         vbox = QVBoxLayout()
#         vbox.addWidget(lcd)
#         vbox.addWidget(sld)

#         self.setLayout(vbox)
#         sld.valueChanged.connect(lcd.display)
#         # 在这里我们将滑动条的valueChanged信号连接到lcd的display插槽。
#         # sender是发出信号的对象。receiver是接收信号的对象。slot(插槽)是对信号做出反应的方法。

#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle("Signal & slott")
#         self.show()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())





# # 在PyQt5中常通过重新实现事件处理器来处理事件。
# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QWidget, QApplication


# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle("Event handler")
#         self.show()

#     def keyPressEvent(self, e):
#         if e.key() == Qt.Key_Escape:
#             self.close()
#     # 我们按下Escape键会使程序退出。


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())






# # 有时需要知道信号是由哪个控件发起的。对此PyQt5提供了sender()方法。
# import sys
# from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         btn1 = QPushButton("Button 1", self)
#         btn1.move(30, 50)

#         btn2 = QPushButton("Button 2", self)
#         btn2.move(150, 50)

#         btn1.clicked.connect(self.buttonClicked)
#         btn2.clicked.connect(self.buttonClicked)
#         # 两个按钮连接到了同一个插槽。

#         self.statusBar()

#         self.setGeometry(300, 300, 290, 150)
#         self.setWindowTitle("Event sender")
#         self.show()

#     def buttonClicked(self):
#         sender = self.sender()
#         self.statusBar().showMessage(sender.text() + " was pressed")
#         # 我们通过调用sender()方法来判断信号源， 并将其名称显示在窗体的状态栏中。


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())








# 通过QObject创建的对象可以发出信号。下面的示例演示了如何发出自定义信号。
# 我们创建了一个名为closeApp的信号。这个信号会在按下鼠标时触发，它连接着QMainWindow的close()插槽。
import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):
    closeApp = pyqtSignal()
    # 信号closeApp是Communicate的类属性，它由pyqtSignal()创建。

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        # 自定义信号closeApp连接着QMainWindow的close()插槽。

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle("Emit signal")
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()
        # 当在窗体上点击鼠标时会触发closeApp信号，使程序退出。


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())