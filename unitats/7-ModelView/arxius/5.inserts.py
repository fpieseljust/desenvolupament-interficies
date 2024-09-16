import sys
import os

from PySide6.QtSql import QSqlDatabase, QSqlQuery

# Create the connection
con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName(
    os.path.join(os.path.dirname(__file__),
                 "contacts.sqlite"))

# Open the connection
if not con.open():
    print("Database Error: %s" % con.lastError().databaseText())
    sys.exit(1)

# Create a query and execute it right away using .exec()
createTableQuery = QSqlQuery()
createTableQuery.exec(
    """
    CREATE TABLE contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        name VARCHAR(40) NOT NULL,
        job VARCHAR(50),
        email VARCHAR(40) NOT NULL
    )
    """
)

insertDataQuery = QSqlQuery()
# Estil OBDC
prepared = insertDataQuery.prepare(
    """
    INSERT INTO contacts (
        name,
        job,
        email
    )
    VALUES (?, ?, ?)
    """
)

if prepared:
    data = [
        ("Lara", "Senior Web Developer", "lara@example.com"),
        ("David", "Project Manager", "david@example.com")
    ]
    # Inserció amb addBindValue
    for name, job, email in data:
        insertDataQuery.addBindValue(name)
        insertDataQuery.addBindValue(job)
        insertDataQuery.addBindValue(email)
        insertDataQuery.exec()

insertDataQuery = QSqlQuery()
# Estil Oracle
prepared = insertDataQuery.prepare(
    """
    INSERT INTO contacts (
        name,
        job,
        email
    )
    VALUES (:name, :job, :email)
    """
)

if prepared:
    data = [
        ("Davinia", "Data Analyst", "davinia@example.com"),
        ("Juli", "Senior Python Developer", "juli@example.com")
    ]

    for name, job, email in data:
        insertDataQuery.bindValue(2, email)  # Inserció per posició
        insertDataQuery.bindValue(":job", job)  # Inserció amb placeholder
        insertDataQuery.bindValue(":name", name)
        insertDataQuery.exec()
