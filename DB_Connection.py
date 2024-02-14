import sqlite3

# Define a function to create a context manager for database connections
class DatabaseConnection:
    def __init__(self, database):
        self.database = database

    def __enter__(self):
        self.connection = sqlite3.connect(self.database)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()

# Example usage
database_file = 'example.db'

# Using the context manager to establish a database connection
with DatabaseConnection(database_file) as connection:
    cursor = connection.cursor()

    # Execute SQL queries or perform database operations
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
    cursor.execute('INSERT INTO users (name) VALUES (?)', ('John',))
    cursor.execute('INSERT INTO users (name) VALUES (?)', ('Alice',))

    # Commit the changes
    connection.commit()

# The database connection is automatically closed when exiting the 'with' block

