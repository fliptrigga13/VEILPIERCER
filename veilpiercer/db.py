import sqlite3
def get_db_connection(db_path="nexus_mind.db"):
    return sqlite3.connect(db_path)

