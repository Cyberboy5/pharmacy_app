from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout
)

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from classes import *
from core import *

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.showMaximized()
        self.setStyleSheet("""
            font-size: 30px
        """)

        self.initUI()
    
    def initUI(self):
        self.v_box = QVBoxLayout()

        
        self.logo_label = QLabel(self)
        self.logo_pixmap = QPixmap('logo.png')
        self.logo_pixmap = self.logo_pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation) 
        self.logo_label.setPixmap(self.logo_pixmap)
        self.logo_label.setAlignment(Qt.AlignCenter)
        
        self.login_input = Edit()
        self.login_input.setPlaceholderText("Login kiriting...")  

        self.password_input = Edit()
        self.password_input.setPlaceholderText("Parolingizni kiriting...")  
        self.password_input.setEchoMode(QLineEdit.Password)

        self.info_label = QLabel()

        self.login_btn = Button("Login")
        self.login_btn.clicked.connect(self.open_customer_page)
        self.registration_btn = Button("Registration")
        self.registration_btn.clicked.connect(self.registr)

        self.hbox=QHBoxLayout()
        self.admin_label=QLabel()
        self.admin_label.setText("Agar siz admin bolsangiz shu yerni bosing ->")
        self.admin_label.setFixedSize(400,25)
        self.admin_label.setStyleSheet("font-size: 15px")
        
        self.admin_btn=Button("Admin paneliga o'tish")
        self.admin_btn.setFixedSize(200,25)
        self.admin_btn.setStyleSheet("font-size: 15px")
        self.admin_btn.clicked.connect(self.open_adminpage)
        
        self.hbox.addWidget(self.admin_label, 6, Qt.AlignRight)
        self.hbox.addWidget(self.admin_btn, 0, Qt.AlignRight)

        self.v_box.addStretch(20)
        self.v_box.addWidget(self.logo_label, 0, Qt.AlignCenter) 
        self.v_box.addStretch(20) 
        self.v_box.addWidget(self.login_input, 0, Qt.AlignCenter)
        self.v_box.addWidget(self.password_input, 0, Qt.AlignCenter)
        self.v_box.addWidget(self.info_label, 0, Qt.AlignCenter)
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.login_btn, 0, Qt.AlignCenter)
        self.v_box.addWidget(self.registration_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(50)
        self.v_box.addLayout(self.hbox)

        self.setLayout(self.v_box)


    def open_customer_page(self):
        self.close()
        login = self.login_input.text()
        password = self.password_input.text()
        user = {
            'login' : login,
            'password' : password
        }
        self.customer_page = Customer(user)

    def registr(self):
        self.close()
        self.registration = RegistrationPage()

    def open_adminpage(self):
        self.close()
        self.admin_page=AdminPage()

class AdminPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.showMaximized()
        self.setStyleSheet("""
            font-size: 30px
        """)

        self.initUI()
    
    def initUI(self):
        self.v_box = QVBoxLayout()

        self.logo_label = QLabel(self)
        self.logo_pixmap = QPixmap('logo.png')
        self.logo_pixmap = self.logo_pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation) 
        self.logo_label.setPixmap(self.logo_pixmap)
        self.logo_label.setAlignment(Qt.AlignCenter)
        
        self.login_input = Edit()
        self.login_input.setPlaceholderText("Login kiriting...")  

        self.password_input = Edit()
        self.password_input.setPlaceholderText("Parolingizni kiriting...")  
        self.password_input.setEchoMode(QLineEdit.Password)

        self.info_label = QLabel()

        self.login_btn = Button("Login")
        self.login_btn.clicked.connect(self.open_customer_page)
        self.registration_btn = Button("Registration")
        self.registration_btn.clicked.connect(self.registr)
        
        self.v_box.addStretch(20)
        self.v_box.addWidget(self.logo_label, 0, Qt.AlignCenter) 
        self.v_box.addStretch(20) 
        self.v_box.addWidget(self.login_input, 0, Qt.AlignCenter)
        self.v_box.addWidget(self.password_input, 0, Qt.AlignCenter)
        self.v_box.addWidget(self.info_label, 0, Qt.AlignCenter)
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.login_btn, 0, Qt.AlignCenter)
        self.v_box.addWidget(self.registration_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(50)
        
        self.setLayout(self.v_box)
        self.show()


    def open_customer_page(self):
        self.close()
        login = self.login_input.text()
        password = self.password_input.text()
        user = {
            'login' : login,
            'password' : password
        }
        self.customer_page = Customer(user)

    def registr(self):
        self.close()
        self.registration = RegistrationPage()




class Customer(QWidget):
    def __init__(self, user):
        self.user = user
        super().__init__()
        self.setWindowTitle("Admin")
        self.showMaximized()
        self.setStyleSheet("""
            font-size: 30px
        """)

        self.initUI()
    
    def initUI(self):
        self.v_box = QVBoxLayout()

        self.update_user_btn = Button('Update user')
        self.delete_user_btn = Button('Delete user')
        self.show_users_btn = Button('Show users')

        self.update_user_btn.clicked.connect(self.open_update_page)
        self.delete_user_btn.clicked.connect(self.close_page)
        self.show_users_btn.clicked.connect(self.show_users)

        self.v_box.addStretch(100)
        self.v_box.addWidget(self.update_user_btn, 0, Qt.AlignCenter)
        self.v_box.addWidget(self.delete_user_btn, 0, Qt.AlignCenter)
        self.v_box.addWidget(self.show_users_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(100)
        
        self.setLayout(self.v_box) 
        self.show()

    def open_update_page(self):
        self.core = Database()
        _id = self.core.get_user_id(self.user)
        print(_id)
        self.close()
        self.upg = UpdatePage(_id)

    def close_page(self):
        # user dalete
        self.close()

    def show_users(self):
        pass

class UpdatePage(QWidget):
    def __init__(self, id = ''):
        super().__init__()
        self.setWindowTitle("Update")
        self.showMaximized()
        self.setStyleSheet("""
            font-size: 30px
        """)

        self.initUI()
    
    def initUI(self):
        self.v_box = QVBoxLayout()

        self.name_input = Edit()
        self.login_input = Edit()
        self.password_input = Edit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.info_label = QLabel()

        self.save_btn = Button("Save user")
        self.save_btn.clicked.connect(self.update_user)

        self.v_box.addStretch(80)
        self.v_box.addWidget(self.name_input, 0, Qt.AlignCenter)
        self.v_box.addWidget(self.login_input, 0, Qt.AlignCenter)
        self.v_box.addWidget(self.password_input, 0, Qt.AlignCenter)
        self.v_box.addWidget(self.info_label, 0, Qt.AlignCenter)
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.save_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(40)

        self.setLayout(self.v_box)
        self.show()

    def update_user(self):
        pass

class RegistrationPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registration")
        self.showMaximized()
        self.setStyleSheet("""
            font-size: 30px
        """)

        self.initUI()
    
    def initUI(self):
        self.v_box = QVBoxLayout()

        self.name_input = Edit()
        self.login_input = Edit()
        self.password_input = Edit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.info_label = QLabel()

        self.save_btn = Button("Save user")
        self.save_btn.clicked.connect(self.create_user)

        self.v_box.addStretch(80)
        self.v_box.addWidget(self.name_input, 0, Qt.AlignCenter)
        self.v_box.addWidget(self.login_input, 0, Qt.AlignCenter)
        self.v_box.addWidget(self.password_input, 0, Qt.AlignCenter)
        self.v_box.addWidget(self.info_label, 0, Qt.AlignCenter)
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.save_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(40)

        self.setLayout(self.v_box)
        self.show()

    def create_user(self):
        self.core = Database()
        name = self.name_input.text()
        login = self.login_input.text()
        password= self.password_input.text()
        user = {
            'name' : name,
            'login' : login,
            'password': password
        } 
        err = self.core.insert_user(user)
        if err:
            self.info_label.setText(err)

        
if __name__ == "__main__":
    app = QApplication([])
    login = LoginPage()
    login.show()
    app.exec_()