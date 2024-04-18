import unittest
import os
import sqlite3

class TestLiquorDatabaseFile(unittest.TestCase):
    def test_database_existence(self):
        # Test whether the database file exists and is a valid SQLite database
        database_file = 'Liquor_Database.db'
        if not os.path.isfile(database_file):
            self.fail(f"{database_file} does not exist")

        try:
            conn = sqlite3.connect(database_file)
            cursor = conn.cursor()

            # Try executing a simple query to check if the file is a valid SQLite database
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' LIMIT 1")
            #This query checks if the first table inside the database is retrievable
            #if the table data is not retrievable then it wouldnt be a database structure
            conn.close()
        except (sqlite3.OperationalError, sqlite3.DatabaseError):
            self.fail(f"{database_file} is not a valid SQLite database")

if __name__ == '__main__':
    unittest.main()




