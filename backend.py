import sqlite3

def connect():
    conn=sqlite3.connect('music.db')
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS music (id INTEGER PRIMARY KEY, title text, artiste text, year text, genre text)')
    conn.commit()
    conn.close()

def insert(title, artiste, year, genre):
    conn=sqlite3.connect('music.db')
    cur=conn.cursor()
    cur.execute('INSERT INTO music VALUES (NULL,?,?,?,?)',(title, artiste, year, genre))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect('music.db')
    cur=conn.cursor()
    cur.execute('SELECT * from music')
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title='', artiste='', year='', genre=''):
    conn=sqlite3.connect('music.db')
    cur=conn.cursor()
    cur.execute('SELECT * from music where title=? OR artiste=? OR year=? OR genre=?',(title, artiste, year, genre))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect('music.db')
    cur=conn.cursor()
    cur.execute('DELETE FROM music where id=?',(id,))
    conn.commit()
    conn.close

def update(id,title, artiste, year, genre):
    conn=sqlite3.connect('music.db')
    cur=conn.cursor()
    cur.execute('UPDATE music SET title=?, artiste=?, year=?, genre=? where id=?',(title, artiste, year, genre, id))
    conn.commit()
    conn.close


connect()
# insert('ap', 'am', 1954, 24534)
# search(1953)
# delete(4)
# print(view())