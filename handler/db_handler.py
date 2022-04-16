import sqlite3
import os.path

from PyQt5 import QtWidgets


def login(login, password, signal):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "users.db")
    msg = QtWidgets.QMessageBox()

    with sqlite3.connect(db_path) as db:
        cur = db.cursor()

        cur.execute(f'SELECT * FROM user WHERE login="{login}";')
        value = cur.fetchall()

        if value != [] and value[0][2] == password:
            signal.emit(value)
        else:
            msg.setWindowTitle("Ошибка!")
            msg.setText("Такого пользователя не существует.")
            msg.exec_()

            signal.emit([])

        cur.close()
    db.close()
    return value


def reg(login, password, signal):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "users.db")
    msg = QtWidgets.QMessageBox()

    with sqlite3.connect(db_path) as db:
        cur = db.cursor()

        cur.execute(f'SELECT * FROM user WHERE login="{login}";')
        value = cur.fetchall()

        if value != []:
            msg.setWindowTitle("Ошибка!")
            msg.setText("Такой пользователь уже существует.")
            msg.exec_()

            signal.emit([])
        else:
            cur.execute(f'INSERT INTO user (login, password) VALUES ("{login}", "{password}");')
            msg.setWindowTitle("Регистрация")
            msg.setText("Регистрация прошла успешно!")
            msg.exec_()

            signal.emit(value)

        db.commit()
        cur.close()
    db.close()
