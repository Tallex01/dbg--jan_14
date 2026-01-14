import sqlite3 

conn = sqlite3.connect('my_database.db')

cursor = conn.cursor()
                                # IF NOT EXISTS --> precaution if we rerun
query = """
    DELETE FROM points WHERE id = 4;
"""

cursor.execute(query)
conn.commit()
conn.close()