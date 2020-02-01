import sys
from PyQt5 import QtWidgets,QtQuick,QtCore,QtGui
from PyQt5.QtWidgets import QMessageBox,QFileDialog
from PIL import Image,ImageQt
import design
from PyQt5.QtGui import QIcon
import os 
import cv2


base_style =" cursor:pointer;\
    border-style: outset;\
    border-width: 2px;\
    border-radius: 10px;\
    border-color: beige;\
    font: bold 14px;\
    min-width: 10em;\
    padding: 6px;\
	max-height: 80px;\
    background-color:"


class App(QtWidgets.QMainWindow,design.Ui_MainWindow):
	img = None
	path = None

	#=======================
	#Init method and linking buttons to the functions
	#=======================
	def __init__(self):
		super(App, self).__init__()
		self.setupUi(self)
		self.selectBtn.clicked.connect(self.chooseButtonClick)
		self.statBtn.clicked.connect(self.getStat)
		self.scanBtn.clicked.connect(self.scanPhoto)


	#=========================
	#Getting image to scan
	#=========================
	def getImage(self):
		try:
			self.path = QFileDialog.getOpenFileName(self,'Choose image','Desktop','Image files (*.png *.jpg)')[0]
			print(path)
			self.img = Image.open(path)
			thumb = self.img.thumbnail((170,170))
			self.selectLbl.setPixmap(QtGui.QPixmap.fromImage(ImageQt.ImageQt(thumb)))
			self.selectBtn.setStyleSheet(base_style + "red;color:white;")
			self.scanBtn.setStyleSheet(base_style + "green;color:white;")
			self.selectBtn.setText("Скасувати вибір")
			cvimg = cv2.imread(path)
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
            eyes = eyeCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.3,
                    minNeighbors=3,      
                    minSize=(30, 30)
                    )
            if len(eyes) != 1:
            	QMessageBox.warning(self,"Dr.Aid","Something went wrong...")
            	self.clearAll()
		except:
			  QMessageBox.warning(self,"Dr.Aid","Something went wrong...")


	#========================
	#Scan photo
	#========================
	def scanPhoto(self):
		if self.img == None:
			QMessageBox.warning(self,"Dr.Aid","Something went wrong...")
			return None
	#============================#
	#                            #
	#    WRITE TOMORROW!!!       #
	#                            #
	#============================#
		cvimg = cv2.imread(self.path)
		maxw,maxd,color = 0,0,""
	    colors = {((20,19,8),(210,165,126)):"blue",((6,23,66),(53,58,103)):"brown", ((22,25,30),(169,164,144)):"grey"}
	    for i in colors:
	        hsv_min = np.array(i[0], np.uint8)
	        hsv_max = np.array(i[1], np.uint8)
	        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
	        thresh = cv2.inRange(hsv, hsv_min, hsv_max)
	        image = Image.fromarray(cv2.cvtColor(thresh,cv2.COLOR_BGR2RGB))
	        b,w = 0,0
	        for row in thresh:
	            for pixel in row:
	                if pixel==255:
	                    w+=1
	                else:
	                    b+=1
	        if w>maxw:
	            maxw = w
	            color = colors[i]
	            maxd = i
	        print("White: ", w,"Black: ",b,"color",colors[i])
	    print("Eye color: ",color)
	    hsv_min = np.array(maxd[0], np.uint8)
	    hsv_max = np.array(maxd[1], np.uint8)
	    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
	    thresh = cv2.inRange(hsv, hsv_min, hsv_max)
	    showimage = Image.fromarray(cv2.cvtColor(thresh,cv2.COLOR_BGR2RGB))    
	    showimage.thumbnail((170,170))
		self.selectLbl.setPixmap(QtGui.QPixmap.fromImage(ImageQt.ImageQt(showimage))))     
		self.reztextLbl.setText("Eye color: "+color)

	#=========================
	#Clear all fields 
	#=========================
	def clearAll(self):
	#	print(2)
		img = None
		self.selectLbl.setPixmap(QtGui.QPixmap.fromImage(ImageQt.ImageQt(Image.open("white.png"))))
		self.rezultLbl.setPixmap(QtGui.QPixmap.fromImage(ImageQt.ImageQt(Image.open("white.png"))))
		self.selectBtn.setText("Виберіть фотографію")
		self.selectBtn.setStyleSheet(base_style + "green;color:white;")
		self.scanBtn.setStyleSheet(base_style +"red;color:white;")
		self.reztextLbl.setText("")



	#=========================
	#Choosing function after clicking a button
	#=========================
	def chooseButtonClick(self):
		print("I am clicked!!!")
		if self.selectBtn.text() == "Виберіть фотографію":
			self.getImage()
		else:
			self.clearAll()
		#self.pushButton.setStyleSheet(base_style + ("red" if self.pushButton.text() =="Скасувати вибір" else "green") + ";color:white;")




	#======================
	#Get statistics	
	#======================
	def getStat(self):
		QMessageBox.warning(self,"Dr.Aid","In developing...")








def main():
	app = QtWidgets.QApplication(sys.argv)
	window = App()
	window.show()
	app.exec_()


if __name__ == "__main__":
	main()
