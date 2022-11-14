import sqlite3

db = sqlite3.connect('rules.db')
sql = db.cursor()


sql.execute("""CREATE TABLE IF NOT EXISTS rul(
    group_id TEXT,
    rules TEXT
)""")
db.commit()


db_admins = sqlite3.connect('admins.db')
sql_admins = db_admins.cursor()

sql_admins.execute("""CREATE TABLE IF NOT EXISTS admins(
    user_id TEXT,
    group_admin TEXT
)""")
db.commit()