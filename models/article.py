import sqlite3

def get_db_connection():
    return sqlite3.connect('/home/charity/Development/Phase-3/Moringa-FT09-phase-3-code-challenge/database/magazine.db')

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    @property
    def author(self):
        return self._get_related_name('authors', self.author_id)

    @property
    def magazine(self):
        return self._get_related_name('magazines', self.magazine_id)

    def _get_related_name(self, table, related_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f'SELECT name FROM {table} WHERE id = ?', (related_id,))
            result = cursor.fetchone()
        return result[0] if result else None

    @classmethod
    def find_by_id(cls, article_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM articles WHERE id = ?', (article_id,))
            row = cursor.fetchone()
        if row:
            return cls(*row)
        return None
