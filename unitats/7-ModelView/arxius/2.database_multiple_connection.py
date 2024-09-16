from PySide6.QtSql import QSqlDatabase

connection1 = QSqlDatabase.addDatabase("QSQLITE", "connection1")
connection1.setDatabaseName("contacts.sqlite")

connection2 = QSqlDatabase.addDatabase("QSQLITE", "connection2")
connection2.setDatabaseName("contacts.sqlite")

database_name1 = connection1.databaseName()
connection_name1 = connection1.connectionName()

database_name2 = connection2.databaseName()
connection_name2 = connection2.connectionName()

print(f"Connectat a {database_name1} a través de {connection_name1}")
print(f"Connectat a {database_name2} a través de {connection_name2}")
