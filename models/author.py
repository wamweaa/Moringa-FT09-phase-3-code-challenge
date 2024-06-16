import sqlite3  # Import the SQLite3 module to interact with the SQLite database

# Class to represent an Author
class Author:
    # Initialize the Author instance with name
    def __init__(self, name):
        # Check if the provided name is a non-empty string
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name  # Set the author's name
        self._id = None  # The ID will be assigned by the database

    # Property to get the author's ID
    @property
    def id(self):
        return self._id

    # Setter to set the author's ID
    @id.setter
    def id(self, id):
        # Ensure the ID is an integer
        if isinstance(id, int):
            self._id = id
        else:
            raise ValueError("Author id must be of type int")

    # Property to get the author's name
    @property
    def name(self):
        return self._name

    # Setter to set the author's name (only allowed if name is not already set)
    @name.setter
    def name(self, name):
        # Check if the name is already set
        if hasattr(self, '_name'):
            raise AttributeError("Cannot change the name after the author is instantiated.")
        # Ensure the name is a non-empty string
        elif isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be of type str and non-empty.")

    # Method to create the author in the database
    def create_author(self):
        conn = sqlite3.connect('./database/magazine.db')  # Connect to the database
        cursor = conn.cursor()  # Create a cursor object to interact with the database

        # Insert the author's name into the authors table
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (self._name,))
        self._id = cursor.lastrowid  # Get the ID of the newly inserted author
        conn.commit()  # Commit the transaction
        conn.close()  # Close the database connection

    # Method to test author creation
    def test_author_creation(self):
        author = Author("John Doe")  # Only pass the name argument
        assert author.name == "John Doe"  # Check if the name is set correctly

    # String representation of the Author instance
    def __repr__(self):
        return f'<Author {self._name}>'