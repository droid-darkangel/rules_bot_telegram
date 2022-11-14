import sqlite3

db = sqlite3.connect('rules.db')
sql = db.cursor()


sql.execute("""CREATE TABLE IF NOT EXISTS rul(
    group_id TEXT,
    rules TEXT
)""")
db.commit()
