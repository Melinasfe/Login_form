import sqlite3
def create_database():
    conn=sqlite3.connect('C:/my/user_database.db')
    c=conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (email TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()
    conn.close()

def add_user(email,password):
    conn=sqlite3.connect('C:/my/user_database.db')
    c=conn.cursor()
    c.execute('INSERT INTO users(email,password) VALUES (?,?)',(email,password))
    conn.commit()
    conn.close()

def check_user(email,password):
    conn=sqlite3.connect('C:/my/user_database.db')
    c=conn.cursor()
    c.execute('SELECT * FROM users WHERE email=? AND password=?',(email,password))
    result=c.fetchone()
    conn.close()
    return result

def email_exists(email):
      conn=sqlite3.connect('C:/my/user_database.db')
      c=conn.cursor()
      c.execute('SELECT * FROM users WHERE email=?',(email,))
      result=c.fetchone()
      conn.close()
      return result
