# from PyQt5 import QtWidgets
# from PyQt5 import QtGui
#
# app = QtWidgets.QApplication([])
# label = QtWidgets.QLabel()
# pixmap = QtGui.QPixmap('a.jpg')
# label.setPixmap(pixmap)
# label.resize(pixmap.width(), pixmap.height())
# label.show()
# app.exec_()


# ////////////////////
import cv2
from PyQt5 import QtWidgets
from PyQt5 import QtGui

app = QtWidgets.QApplication([])
label = QtWidgets.QLabel()

img = cv2.imread('b.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
h,w,c = img.shape
qImg = QtGui.QImage(img.data, w, h, w*c, QtGui.QImage.Format_RGB888)
pixmap = QtGui.QPixmap.fromImage(qImg)
label.setPixmap(pixmap)
label.resize(pixmap.width(), pixmap.height())
label.show()

app.exec_()


#cv2로 변환해서 이미지를 보여주는 방법
