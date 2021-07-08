import sqlite3

# Create connection
conn = sqlite3.connect("my_friends.db")
c = conn.cursor()
# c.execute(
#     "CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
insert_query = '''
INSERT INTO friends VALUES ('jack', 'sprat', 7);
'''
c.execute(insert_query)
# Commit
conn.commit()
conn.close()
