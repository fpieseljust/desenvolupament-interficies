import sys
import os

from PySide6.QtSql import QSqlDatabase, QSqlQuery

# Create the connection
connection = QSqlDatabase.addDatabase("QSQLITE")
connection.setDatabaseName(
    os.path.join(os.path.dirname(__file__),
                 "contacts.sqlite"))

# Open the connection
if not connection.open():
    print("Database Error: %s" % connection.lastError().databaseText())
    sys.exit(1)

# Create a query and execute it right away using .exec()
createTableQuery = QSqlQuery()
t = createTableQuery.exec(
    """
    CREATE TABLE contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        name VARCHAR(40) NOT NULL,
        job VARCHAR(50),
        email VARCHAR(40) NOT NULL
    )
    """
)

print(connection.tables())
