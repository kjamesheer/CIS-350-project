# -*- coding: utf-8 -*-
# drink_recipes/database.py

"""This module provides a database connection."""

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase
from PyQt5 import QtSql

def createDB():
    """Create and open a database connection."""
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName('drinks_test.db')

    if not connection.open():
        QMessageBox.warning(
            None,
            "RP Contact",
            f"Database Error: {connection.lastError().text()}",
        )
        return False

    query = QtSql.QSqlQuery()

    query.exec("create table mixertable(id int primary key, "
               "name varchar(40), type varchar(40))")

    return True

createDB()
