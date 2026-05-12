from flask import Flask, render_template, jsonify, request
import sqlite3

app = Flask(__name__)

def init_db():
    """Create the database and emails table if it doesn't exist"""
    conn = sqlite3.connect('comball.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            date TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    """Save email to database"""
    email = request.json.get('email')
    if not email:
        return jsonify({'success': False, 'message': 'No email provided'})
    
    try:
        conn = sqlite3.connect('comball.db')
        c = conn.cursor()
        c.execute('INSERT INTO emails (email) VALUES (?)', (email,))
        conn.commit()
        conn.close()
        return jsonify({'success': True, 'message': 'Thanks! We will notify you when we launch 🎉'})
    except sqlite3.IntegrityError:
        return jsonify({'success': False, 'message': 'This email is already registered!'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)