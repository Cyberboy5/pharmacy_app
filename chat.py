import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

class ProductButton(QPushButton):
    def __init__(self, image_path, name, price, description):
        super().__init__()

        # Tugma kattaligini sozlash
        self.setFixedSize(200, 250)

        # Tugma ichidagi layout
        self.layout = QVBoxLayout()
        
        # Mahsulot rasmi
        self.image_label = QLabel(self)
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            pixmap = QPixmap("logo.png")  # Muqobil rasm yo'li
        self.image_label.setPixmap(pixmap.scaled(150, 150))
        self.layout.addWidget(self.image_label)
        
        # Mahsulot nomi
        self.name_label = QLabel(name)
        self.name_label.setFont(QFont("Arial", 12, QFont.Bold))
        self.name_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.name_label)
        
        # Mahsulot narxi
        self.price_label = QLabel(price)
        self.price_label.setFont(QFont("Arial", 10))
        self.price_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.price_label)

        # Tugma ustidagi layoutni o'rnatish
        self.setLayout(self.layout)
        
        # Tugma uchun ma'lumot
        self.description = description
    
    def show_info(self):
        print(f"Mahsulot nomi: {self.name_label.text()}")
        print(f"Narxi: {self.price_label.text()}")
        print(f"Ma'lumot: {self.description}")

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dori kartochkalari")
        self.setGeometry(100, 100, 800, 400)

        # Asosiy markaziy vidjetni yaratish
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Umumiy layout yaratish
        main_layout = QHBoxLayout(central_widget)

        # Mahsulot kartalari
        products = [
            {"image_path": "image1.png", "name": "ЭССЕНЦИАЛЕ ФОРТЕ Н", "price": "42900 сум", "description": "ЭССЕНЦИАЛЕ haqida batafsil..."},
            {"image_path": "image2.png", "name": "ЭЛЕВИТ ПРОНАТАЛЬ", "price": "112000 сум", "description": "ЭЛЕВИТ haqida batafsil..."},
            {"image_path": "image3.png", "name": "ВИФЕРОН", "price": "75300 сум", "description": "ВИФЕРОН haqida batafsil..."},
            {"image_path": "image4.png", "name": "КОДЕЛАК БРОНХО", "price": "26000 сум", "description": "КОДЕЛАК haqida batafsil..."},
            {"image_path": "image5.png", "name": "АРБИДОЛ", "price": "87000 сум", "description": "АРБИДОЛ haqida batafsil..."}
        ]
        
        for product in products:
            button = ProductButton(product["image_path"], product["name"], product["price"], product["description"])
            button.clicked.connect(button.show_info)  # Tugma bosilganda ma'lumotlarni chiqarish
            main_layout.addWidget(button)

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
