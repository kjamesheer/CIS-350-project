# -*- coding: utf-8 -*-
# drink_recipes/database.py

"""This module provides a database connection."""

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def create_connection(database_name):
    """Create and open a database connection."""
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(database_name)
    if not connection.open():
        QMessageBox.warning(
            None,
            "Drink Recipes",
            f"Database Error: {connection.lastError().text()}",
        )
        return False
    return True

def _create_ingredient_table():
    """Create the ingredient table."""
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(""" CREATE TABLE ingredient_types (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name VARCHAR(40) NOT NULL,
            type VARCHAR(40) NOT NULL
        )
    """)

def _create_liquor_table():
    """Create the liquor table."""
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(""" CREATE TABLE liquor (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name VARCHAR(40) NOT NULL,
            type VARCHAR(40) NOT NULL,
            description TEXT
        )
    """)

def _create_mixer_table():
    """Create the mixer table."""
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(""" CREATE TABLE mixer (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name VARCHAR(40) NOT NULL,
            type VARCHAR(40) NOT NULL,
            description TEXT
        )
    """)

def _create_garnish_table():
    """Create the garnish table."""
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(""" CREATE TABLE garnish (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name VARCHAR(40) NOT NULL,
            type VARCHAR(40) NOT NULL,
            description TEXT
        )
    """)

def _create_glass_table():
    """Create the glass table."""
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(""" CREATE TABLE glass (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name VARCHAR(40) NOT NULL,
            type VARCHAR(40) NOT NULL,
            description TEXT
        )
    """)