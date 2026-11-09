from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('marketplace.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS items (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        description TEXT NOT NULL,
                        price REAL,
                        location TEXT,
                        posted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        approved INTEGER DEFAULT 0
                    )''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM items WHERE approved = 1 ORDER BY posted_at DESC').fetchall()
    conn.close()
    return render_template('index.html', items=items)

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        price = request.form['price']
        location = request.form['location']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO items (title, description, price, location) VALUES (?, ?, ?, ?)',
                     (title, description, price, location))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('post.html')

@app.route('/admin')
def admin():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM items ORDER BY posted_at DESC').fetchall()
    conn.close()
    return render_template('admin.html', items=items)

@app.route('/approve/<int:item_id>')
def approve(item_id):
    conn = get_db_connection()
    conn.execute('UPDATE items SET approved = 1 WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('admin'))

@app.route('/reject/<int:item_id>')
def reject(item_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM items WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)