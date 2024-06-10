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
        conn = get_db_connection() 
        cursor = conn.cursor() 
        cursor.execute('SELECT name FROM authors WHERE id = ?', (self.author_id,))  
        author_name = cursor.fetchone()[0] if cursor.fetchone() else None  
        conn.close()  
        return author_name  

    
    @property
    def magazine(self):
        conn = get_db_connection()  
        cursor = conn.cursor() 
        cursor.execute('SELECT name FROM magazines WHERE id = ?', (self.magazine_id,))  
        magazine_name = cursor.fetchone()[0] if cursor.fetchone() else None 
        conn.close()
        return magazine_name  
    
    
    @classmethod
    def find_by_id(cls, article_id):
        conn = get_db_connection()
        cursor = conn.cursor() 
        cursor.execute('SELECT * FROM articles WHERE id = ?', (article_id,))  
        row = cursor.fetchone()  
        conn.close()  
        if row:
            return cls(*row)  
        return None  