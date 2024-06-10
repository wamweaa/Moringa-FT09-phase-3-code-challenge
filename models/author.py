import sqlite3

class Author:
    def __init__(self, id, name):
        self._id = id
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self._id = id
        else:
            raise ValueError("Author id must be of type int")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if hasattr(self, '_name'):
            raise AttributeError("Cannot change the name after the author is instantiated.")
        elif isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be of type str and non-empty.")

    def create_author(self):
        conn = sqlite3.connect('./database/magazine.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (self._name,))
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()

    @staticmethod
    def test_author_creation():
        author = Author(1, "John Doe")
        assert author.name == "John Doe"
        assert author.id == 1
        return "Author creation test passed."

    def __repr__(self):
        return f'<Author {self._name}>'
