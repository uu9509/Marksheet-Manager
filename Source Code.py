import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem

import sqlite3

 

conn = sqlite3.connect('marksheet.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS marks (name TEXT, math INTEGER, science INTEGER, english INTEGER, total INTEGER, percentage FLOAT)''')

 

class Marksheet(QWidget):

    def __init__(self):

        super().__init__()

 

        self.initUI()

 

    def initUI(self):

        # Labels

        self.name_label = QLabel("Name:", self)

        self.name_label.move(10, 10)

 

        self.math_label = QLabel("Math:", self)

        self.math_label.move(10, 40)

 

        self.science_label = QLabel("Science:", self)

        self.science_label.move(10, 70)

 

        self.english_label = QLabel("English:", self)

        self.english_label.move(10, 100)

 

        # Line Edits

        self.name_edit = QLineEdit(self)

        self.name_edit.move(70, 10)

 

        self.math_edit = QLineEdit(self)

        self.math_edit.move(70, 40)

 

        self.science_edit = QLineEdit(self)

        self.science_edit.move(70, 70)

 

        self.english_edit = QLineEdit(self)

        self.english_edit.move(70, 100)

 

        # Button

        self.add_button = QPushButton('Add', self)

        self.add_button.move(10, 140)

        self.add_button.clicked.connect(self.add_marks)

 

        # Table

        self.table = QTableWidget(self)

        self.table.setGeometry(200, 10, 480, 380)

        self.table.setColumnCount(6)

        self.table.setHorizontalHeaderLabels(['Name', 'Math', 'Science', 'English', 'Total', 'Percentage'])

 

        # Window

        self.setGeometry(100, 100, 700, 400)

        self.setWindowTitle('Marksheet')

        self.show()

 

    def add_marks(self):

        name = self.name_edit.text()

        math = int(self.math_edit.text())

        science = int(self.science_edit.text())

        english = int(self.english_edit.text())

        total = math + science + english

        percentage = round(total / 3, 2)

 

        c = conn.cursor()

        c.execute("INSERT INTO marks VALUES (?, ?, ?, ?, ?, ?)", (name, math, science, english, total, percentage))

        conn.commit()

 

        row_count = self.table.rowCount()

        self.table.insertRow(row_count)

        self.table.setItem(row_count, 0, QTableWidgetItem(name))

        self.table.setItem(row_count, 1, QTableWidgetItem(str(math)))

        self.table.setItem(row_count, 2, QTableWidgetItem(str(science)))

        self.table.setItem(row_count, 3, QTableWidgetItem(str(english)))

        self.table.setItem(row_count, 4, QTableWidgetItem(str(total)))

        self.table.setItem(row_count, 5, QTableWidgetItem(str(percentage)))

 

if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = Marksheet()

    sys.exit(app.exec_())

conn = sqlite3.connect('marksheet.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS marks (name TEXT, math INTEGER, science INTEGER, english INTEGER, total INTEGER, percentage FLOAT)''')

c.execute("INSERT INTO marks VALUES (?, ?, ?, ?, ?, ?)", ('John', 90, 85, 95, 270, 90.0))

c.execute("INSERT INTO marks VALUES (?, ?, ?, ?, ?, ?)", ('Alice', 80, 75, 85, 240, 80.0))

c.execute("INSERT INTO marks VALUES (?, ?, ?, ?, ?, ?)", ('Bob', 70, 65, 75, 210, 70.0))

c.execute("INSERT INTO marks VALUES (?, ?, ?, ?, ?, ?)", ('John', 60, 55, 65, 180, 60.0))

conn.commit()

c.execute("SELECT * FROM marks")

rows = c.fetchall()

for row in rows:

    print(row)

c.execute("UPDATE marks SET math = ? WHERE name = ?", (95, 'John'))

conn.commit()

c.execute("DELETE FROM marks WHERE name = ?", ('James',))

conn.commit()