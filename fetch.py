import sqlite3 

conn = sqlite3.connect('my_database.db')

cursor = conn.cursor()
                                # IF NOT EXISTS --> precaution if we rerun
query = """
    SELECT *
    FROM points;
"""

cursor.execute(query)
result = cursor.fetchall()   # might not want to look at all data in query

conn.close()

print(result)