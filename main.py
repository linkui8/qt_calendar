import sys
import sqlite3

from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel,QMainWindow, QVBoxLayout


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('mainWindow.ui', self)
        self.conn = sqlite3.connect('calendar.db')
        self.confirmButton.clicked.connect(self.clicked)
        self.updateButton.clicked.connect(self.areaUpdate)
        self.titles = None
        self.layout1 = QVBoxLayout()
        self.layout1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.deleteButton.clicked.connect(self.clicked2)


    def clicked(self):
        self.inDate = self.dateInput.text()
        self.inMonth = self.monthInput.text()
        self.inTime = self.timeInput.text()
        self.inEvent = self.eventInput.text()
        curs = self.conn.cursor()
        query_str1 = f"update dates1 set time = '{self.inTime}' where date like '{self.inDate}' and month like '{self.inMonth}';"
        query = curs.execute(query_str1)
        query_str2 = f"update dates1 set event = '{self.inEvent}' where date like '{self.inDate}' and month like '{self.inMonth}';"
        query = curs.execute(query_str2)
        self.conn.commit()
        self.genString = f"Дата: {self.inDate}.{self.inMonth}.2025  Время: {self.inTime}  Событие: {self.inEvent}"
        self.fout = open("events.txt", "w")
        self.fout.write(f"{self.genString} \n")
        self.fout.close()


    def clicked2(self):
        self.inDDate = self.ddateInput.text()
        self.inDMonth = self.dmonthInput.text()
        curs = self.conn.cursor()
        query_str1 = f"update dates1 set event = NULL where date like '{self.inDDate}' and month like '{self.inDMonth}';"
        query = curs.execute(query_str1)
        self.conn.commit()


    def areaUpdate(self):
        curs = self.conn.cursor()
        result = curs.execute("select date, month, day, event, time from dates1 where event is not null;")
        a = 0
        for i in result:
            if a >= 7:
                break
            self.verticalLayout.addWidget(QLabel(f"Дата: {i[0]}.{i[1]}.2025  День недели: {i[2]} \n Время: {i[4]}  Событие: {i[3]}")) #QLabel().setText("Дата: 1.2025  День недели: 1  Время: 1  Событие: 1")
            print(f"Дата: {i[0]}.{i[1]}.2025  День недели: {i[2]}  Время: {i[4]}  Событие: {i[3]}")
            a += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())