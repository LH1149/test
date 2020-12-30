# 我们将在这部分教程中创建菜单与工具栏。一个菜单就是位于菜单栏中的一组命令。应用的工具栏放置了带有按钮的常用命令
# 1、主窗体：QMainWindow类提供了一个主程序窗体。通过它可以创建带有状态栏、工具栏与菜单栏的传统应用程序。

# # 2、状态栏：状态栏是用于显示状态信息的控件。
# import sys
# from PyQt5.QtWidgets import QMainWindow, QApplication
# # 可以通过QMainWindow创建状态栏控件。

# class Example(QMainWindow):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         # 我们需要调用QtGui.QMainWindow的statusBar()方法来创建状态栏。
#         # 第一次调用该方法会创建一个状态栏对象，之后的调用都会返回这个状态栏对象。showMessage()会将消息展示在状态栏。
#         self.statusBar().showMessage("Ready")
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle("Statusbar")
#         self.show()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())



# # 3、菜单栏：是GUI程序的标配。它是一组位于不同菜单内的命令集。
# # （Mac系统会以不同的方式处理菜单栏，但添加menubar.setNativeMenuBar(False)这行代码后可以得到一致的结果。）
# import sys
# from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
# from PyQt5.QtGui import QIcon


# class Example(QMainWindow):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         exitAction = QAction(QIcon("D:/CSR/wallpaper/1.jpg"), "&Exit", self)
#         exitAction.setShortcut("Ctrl+Q")
#         exitAction.setStatusTip("Exit application")
#         # QAction是菜单栏、工具栏或自定义快捷键中可以执行的动作的抽象表示。
#         # 上面这三行代码创建了一个带有特定图标与‘Exit’标签的动作，而且还为这个动作定义了一个快捷键。
#         # 第三个代码为这个动作设置了状态提示，当鼠标悬停在这个菜单项上时状态提示会显示在状态栏。
#         exitAction.triggered.connect(qApp.quit)
#         # 当点击这个动作时会发出triggered信号。这个信号连接到了QApplication的quit()方法。从而使程序停止。

#         self.statusBar()

#         menubar = self.menuBar()
#         fileMenu = menubar.addMenu("&File")
#         fileMenu.addAction(exitAction)
#         # menuBar()方法会创建一个菜单栏。我们在菜单栏中创建了一个file菜单并为其添加了exitAction。

#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle("Menubar")
#         self.setWindowIcon(QIcon("D:/CSR/wallpaper/2.jpg"))
#         self.show()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())






# # 4、工具栏:为常用命令提供了快速的访问方式。
# import sys
# from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
# from PyQt5.QtGui import QIcon


# class Example(QMainWindow):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         exitAction = QAction(QIcon("D:/CSR/wallpaper/1.jpg"), "Exit", self)
#         exitAction.setShortcut("Ctrl+Q")
#         exitAction.triggered.connect(qApp.quit)
#         # 与上面菜单栏示例类似，我们创建了一个QAction对象。
#         # 这个对象也有标签、图标和快捷键。QtGui.QMainWindow的quit()方法与triggered信号相连。

#         self.toolbar = self.addToolBar("Exit")
#         self.toolbar.addAction(exitAction)
#         # 这里我们创建了一个工具栏并在其中添加了一个QAction对象。

#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle("Toolbar")
#         self.setWindowIcon(QIcon("D:/CSR/wallpaper/2.jpg"))
#         self.show()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())






# 5、组装起来
# (1)导入包
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

# (2)主窗体

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 状态栏
        self.statusBar().showMessage("Ready")
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Statusbar")

        # 菜单栏
        exitAction = QAction(QIcon("D:/CSR/wallpaper/1.jpg"), "&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit application")
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(exitAction)

        # 工具栏
        self.toolbar = self.addToolBar("Exit")
        self.toolbar.addAction(exitAction)
        self.setWindowIcon(QIcon("D:/CSR/wallpaper/2.jpg"))

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


        

