from PySide6.QtSql import QSqlDatabase

connection = QSqlDatabase.addDatabase("QSQLITE")
connection.setDatabaseName("contacts.sqlite")
database_name = connection.databaseName()
connection_name = connection.connectionName()

print(database_name, connection_name)
