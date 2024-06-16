import sqlite3

class DatabaseManager:
    @staticmethod
    def initialize_db(db_path='app_database.db'):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT NOT NULL,
                            email TEXT NOT NULL,
                            password TEXT NOT NULL
                          )''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            author TEXT NOT NULL
                          )''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS borrow_records (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER NOT NULL,
                            book_id INTEGER NOT NULL,
                            borrow_date TEXT NOT NULL,
                            return_date TEXT,
                            FOREIGN KEY (user_id) REFERENCES users(id),
                            FOREIGN KEY (book_id) REFERENCES books(id)
                          )''')

        connection.commit()
        connection.close()
    
    @staticmethod
    def add_object(table, columns, values, db_path='app_database.db'):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        
        columns_str = ', '.join(columns)
        placeholders = ', '.join(['?' for _ in values])
        
        cursor.execute(f'INSERT INTO {table} ({columns_str}) VALUES ({placeholders})', values)
        
        connection.commit()
        connection.close()
    
    @staticmethod
    def delete_object(table, object_id, db_path='app_database.db'):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        
        cursor.execute(f'DELETE FROM {table} WHERE id = ?', (object_id,))
        
        connection.commit()
        connection.close()
    
    @staticmethod
    def update_object(table, object_id, columns, values, db_path='app_database.db'):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        
        set_clause = ', '.join([f'{col} = ?' for col in columns])
        
        cursor.execute(f'UPDATE {table} SET {set_clause} WHERE id = ?', (*values, object_id))
        
        connection.commit()
        connection.close()
    
    @staticmethod
    def fetch_all_objects(table, db_path='app_database.db'):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        
        cursor.execute(f'SELECT * FROM {table}')
        rows = cursor.fetchall()
        
        connection.close()
        return rows
