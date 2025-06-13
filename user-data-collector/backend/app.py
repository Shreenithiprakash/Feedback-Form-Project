from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def init_db():
    with sqlite3.connect("db.sqlite3") as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                message TEXT NOT NULL
            )
        ''')
        conn.commit()

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')
    mail = data.get('msg')

    if not name or not mail:
        return jsonify({'message': 'Name and message are required'}), 400

    with sqlite3.connect("db.sqlite3") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, message) VALUES (?, ?)", (name, mail))
        conn.commit()

    return jsonify({'message': 'User data saved successfully'}), 200

@app.route('/users', methods=['GET'])
def users():
    with sqlite3.connect("db.sqlite3") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, message FROM users")
        users = cursor.fetchall()
    return jsonify(users)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
