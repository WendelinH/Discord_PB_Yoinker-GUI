import sys
import requests # pip install requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QImage, QPixmap


url_image = 'https://cdn.discordapp.com/avatars/373208633099681814/838e760018f1c65eacd936de37f9a9b4.png?size=1024'

app = QApplication([])

image = QImage()
image.loadFromData(requests.get(url_image).content)

image_label = QLabel()
image_label.setPixmap(QPixmap(image))
image_label.show()

app.exec_()