import sqlite3  
class Magazine:
   
    def __init__(self, id, name, category):
        self._id = id
        self._name = name
        self._category = category

    @property
    def id(self):
        return self._id


    @id.setter
    def id(self, id):

        if isinstance(id, int):
            self._id = id
        else:
            raise ValueError("Magazine id must be of type int")


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, name):
      
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError("Name must be a string between 2 and 16 characters")

    @property
    def category(self):
        return self._category


    @category.setter
    def category(self, category):
        
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be a non-empty string")


    def create_magazine(self):
        conn = sqlite3.connect('./database/magazine.db')  
        cursor = conn.cursor()  

        cursor.execute('INSERT INTO magazines (id, name, category) VALUES (?, ?, ?)', 
                       (self._id, self._name, self._category))
        self._id = cursor.lastrowid  
        conn.commit() 
        conn.close()  

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")  
        assert magazine.name == "Tech Weekly"  
        assert magazine.category == "Technology" 

    def __repr__(self):
        return f'<Magazine {self._name}, Category: {self._category}>'