import sqlite3
conn = sqlite3.connect(r'C:\Users\fyou1\nexus-ultra\nexus_mind.db')
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table'")
print('Tables:', c.fetchall())
c.execute('PRAGMA table_info(memories)')
print('Schema:', c.fetchall())
conn.close()
