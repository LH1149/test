# 布局管理是如何将控件放置于窗体上的技术，它的实现有两种基本方式：绝对布局与layout类。
# 1、绝对布局
# 程序员要指定每个控件的像素位置与大小。在使用绝对布局时要知道它的局限：
# 1-控件的尺寸与位置不会随着窗体尺寸的调整而变化
# 2-程序在不同平台上可能会有不同的外观
# 3-改变程序的字体可能会破坏布局
# 4-如果想改变布局，只能重做，这很无聊而且很费时




# # 下面的示例中以绝对坐标来放置控件
# import sys
# from PyQt5.QtWidgets import QWidget, QLabel, QApplication


# class Example(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         lb11 = QLabel("You", self)
#         lb11.move(100, 70)

#         lb12 = QLabel("are", self)
#         lb12.move(100,80)

#         lb13 = QLabel("best", self)
#         lb13.move(100, 90)

#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle("Absolute")
#         self.show()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())






# # BOX layout
# # 布局类提供的布局管理具有更好的灵活性与实用性，它是在窗体上放置控件的首选方式。
# # QHBoxLayout与QVBoxLayout是水平与垂直放置控件的两个基本布局类。
# # 假如要在右下角放置两个按钮，我们要借助于HBoxLayout与VBoxLayout，并设置stretch factor(伸展系数)来创建所需的空白空间。
# import sys
# from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication)


# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         okButton = QPushButton("OK")
#         cancelButton = QPushButton("Cancel")
#         # 这里创建了两个按钮

#         hbox = QHBoxLayout()
#         hbox.addStretch(1)
#         hbox.addWidget(okButton)
#         hbox.addWidget(cancelButton)
#         # 我们创建了一个水平boxlayout并添加了一个伸展系数和两个按钮。stretch方法会在两按钮前面添加一个伸展空间，从而将按钮挤到窗体的右侧。

#         vbox = QVBoxLayout()
#         vbox.addStretch(1)
#         vbox.addLayout(hbox)
#         # 通过将水平布局置于垂直布局内来得到我们需要的布局。垂直布局的伸展系数会将按钮挤到窗体底部。

#         self.setLayout(vbox)
#         # 最后将vbox设为窗体的主布局。
#         self.setGeometry(300, 300, 300, 150)
#         self.setWindowTitle("Buttons")
#         self.show()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())







# # QGridLayout：网格布局是最常用的布局。它会按行列对空间进行切分。我们使用类QGridLayout创建网格布局。 
# import sys
# from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication)


# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         grid = QGridLayout()
#         self.setLayout(grid)
#         # 这里创建了一个QGridLayout实例，并将它设为窗体的布局。

#         names = ["Cls", "Bck", "", "Close",
#                  "7", "8", "9", "/",
#                  "4", "5", "6", "*",
#                  "1", "2", "3", "-",
#                  "0", ".", "=", "+"]
#         # 这些是按钮的标签。

#         positions = [(i,j) for i in range(5) for j in range(4)]
#         # 我们在网格中创建了一系列位置坐标。

#         for position, name in zip(positions, names):
#             if name == "":
#                 continue
#             button = QPushButton(name)
#             grid.addWidget(button, *position)
#             # 通过addWidget()方法将创建的按钮添加到布局中。

#         self.move(300, 150)
#         self.setWindowTitle("Calculator")
#         self.show()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())









# # 一个简单的评论窗体
# # 控件可以在布局中跨行或跨列。正如下面的例子所展示的。
# # 我们创建了一个带有三个Label、两个LineEdit和一个TextEdit的窗体。采用了QGridLayout布局。
# import sys
# from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout,QApplication)


# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         title = QLabel("Title")
#         author = QLabel("Author")
#         review = QLabel("Review")

#         titleEdit = QLineEdit()
#         authorEdit = QLineEdit()
#         reviewEdit = QTextEdit()

#         grid = QGridLayout()
#         grid.setSpacing(10)
#         # 我们创建了一个网格布局并为它设置了控件间距。

#         grid.addWidget(title, 1, 0)
#         grid.addWidget(titleEdit, 1, 1)

#         grid.addWidget(author, 2, 0)
#         grid.addWidget(authorEdit, 2, 1)

#         grid.addWidget(review, 3, 0)
#         grid.addWidget(reviewEdit, 3, 1, 5, 1)
#         # 在添加控件的时候我们可以设置控件跨行或跨列。在例子中我们将reviewEdit控件跨越5行。

#         self.setLayout(grid)

#         self.setGeometry(300, 300, 350, 300)
#         self.setWindowTitle("Review")
#         self.show()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())






# 综合一哈
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QLineEdit, QTextEdit, QHBoxLayout, QVBoxLayout, QGridLayout,QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 1
        # okButton = QPushButton("OK")
        # cancelButton = QPushButton("Cancel")

        # hbox = QHBoxLayout()
        # hbox.addStretch(1)
        # hbox.addWidget(okButton)
        # hbox.addWidget(cancelButton)

        # vbox = QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addLayout(hbox)

        # self.setLayout(vbox)

        # 2
        grid = QGridLayout()
        self.setLayout(grid)

        names = ["Cls", "Back", "", "Close",
                 "7", "8", "9", "/",
                 "4", "5", "6", "*",
                 "1", "2", "3", "-",
                 "0", ".", "=", "+"]

        positions = [(i,j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == "":
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)



        # 3
        title = QLabel("Title")

        titleEdit = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)


        # self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("total")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())