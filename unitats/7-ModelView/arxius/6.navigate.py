import sys
import os

from PySide6.QtSql import QSqlDatabase, QSqlQuery

connection = QSqlDatabase.addDatabase("QSQLITE")
connection.setDatabaseName(
    os.path.join(os.path.dirname(__file__),
                 "contacts.sqlite")
)

if not connection.open():
    print("Error connectant a la base de dades!",
          f"Database Error: {connection.lastError().databaseText()}")
    sys.exit(1)
else:  # Connected
    query = QSqlQuery()
    if query.exec("SELECT name, job, email FROM contacts"):
        while query.next():
            print(
                f"Nom: {query.value('name')} \tTreball: {query.value('job')} \tCorreu: {query.value('email')}")
    query.finish()
    connection.close()
    print("Connexions disponibles: {}".format(QSqlDatabase.connectionNames()))
    QSqlDatabase.removeDatabase(QSqlDatabase.database().connectionName())
    print("Connexions disponibles: {}".format(QSqlDatabase.connectionNames()))
