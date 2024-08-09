from PyQt5.QtWidgets import QApplication
from ui import LoginPage

def main():
    app = QApplication([])
    login = LoginPage()
    login.show()
    app.exec_()

if __name__ == "__main__":
    main()
    # pass