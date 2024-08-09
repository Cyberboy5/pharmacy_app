from PyQt5.QtWidgets import (
    QLineEdit,
    QPushButton
)

class Button(QPushButton):
    def __init__(self, text = ''):
        super().__init__(text)
        self.setFixedSize(350,50)

class Edit(QLineEdit):
    def __init__(self, text = ''):
        super().__init__(text)
        self.setFixedSize(350,50)

