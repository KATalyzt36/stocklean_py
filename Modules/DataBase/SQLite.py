import sqlite3

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def create_table(self):
        try:
            self.cursor.execute(
                'CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, item_id INTEGER NOT NULL UNIQUE, item_name VARCHAR(100) NOT NULL, item_quantity INTEGER NOT NULL, item_price DECIMAL(10, 2) NOT NULL, item_card_price DECIMAL(10, 2) NOT NULL, provider VARCHAR(100) NOT NULL);')
        except sqlite3.Error as e:
            print(f"Error en create_table: {e}")
        finally:
            self.conn.commit()

    def get_all_values(self):
        self.cursor.execute('SELECT * FROM items')
        result = self.cursor.fetchall()
        if result:
            return result
        return False

    def get_value_from(self, item_id: int):
        self.cursor.execute('SELECT * FROM items WHERE item_id = ?', (item_id,))
        result = self.cursor.fetchall()
        if result:
            return result
        return False

    def create_item(self, item_id: int, item_name: str, item_quantity: int, item_price: int, provider: str):
        item_card_price = item_price * 1.1
        try:
            self.cursor.execute(
                'INSERT OR IGNORE INTO items (item_id, item_name, item_quantity, item_price, item_card_price, provider) VALUES (?, ?, ?, ?, ?, ?)',
                (item_id, item_name, item_quantity, item_price, item_card_price, provider))
        except sqlite3.Error as e:
            print(f'Error create_item:: {e}')
        finally:
            self.conn.commit()

    def update_values(self, item_id: int, item_name: str, item_quantity: int, item_price: int, provider: str):
        item_card_price = item_price * 1.1
        try:
            self.cursor.execute(
                'UPDATE items SET item_id = ?, item_name = ?, item_quantity = ?, item_price = ?, item_card_price = ?, provider = ? WHERE item_id = ?',
                (item_id, item_name, item_quantity, item_price, item_card_price, item_id, provider))
        except sqlite3.Error as e:
            print(f'Error update_values:: {e}')
        finally:
            self.conn.commit()

    def clear_item(self, item_id: int):
        try:
            self.cursor.execute('DELETE FROM items WHERE item_id = ?', (item_id,))
        except sqlite3.Error as e:
            print(f'Error clear_item:: {e}')
        finally:
            self.conn.commit()

    def clear_table(self):
        try:
            self.cursor.execute('DELETE FROM items;')
        except sqlite3.Error as e:
            print(f'Error clear_table:: {e}')
        finally:
            self.conn.commit()

