import bcrypt
import os

from pytestqt.qt_compat import qt_api

from PySide6.QtWidgets import QDialog
from PySide6.QtSql import QSqlDatabase, QSqlQuery

from main import CreateUserDialog


def test_login(qtbot):
    database_path = 'test_users.db'
    login = CreateUserDialog(database_path)    
    qtbot.addWidget(login)

    # Omple els camps de text
    user = 'user3'
    qtbot.keyClicks(login.user, user)
    password = 'password3'
    qtbot.keyClicks(login.password, password)

    login.create_database()

    login.btn_create.click()

    if login.db.open():
        query = QSqlQuery()
        query.prepare("SELECT user, password FROM users WHERE user = ?")
        query.addBindValue(user)
        query.exec()
        query.next()
        user_db = query.value(0)
        hashed_password_db = query.value(1)
            
        # assert bcrypt.checkpw(password_db.encode('utf-8'), hashed_password.encode('utf-8')):
        assert user_db == user
        assert bcrypt.checkpw(password.encode('utf-8'), hashed_password_db.encode('utf-8'))

    os.remove(database_path)
