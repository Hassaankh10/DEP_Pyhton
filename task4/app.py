from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is the task 4 on my DEP Internship'

@app.route('/create')
def create_DB():
    try:
        conn = sqlite3.connect('task4db.sqlite')
        curr = conn.cursor()
        curr.execute('DROP TABLE IF EXISTS User')
        curr.execute('''CREATE TABLE User (
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        name TEXT UNIQUE
                    )''')
        conn.commit()
        return 'Database Created'
    except sqlite3.Error as e:
        return f'An error occurred: {e}'
    finally:
        conn.close()

@app.route('/update/<string:name>')
def update_db(name):
    try:
        conn = sqlite3.connect('task4db.sqlite')
        curr = conn.cursor()
        curr.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
        conn.commit()
        return 'Database Updated'
    except sqlite3.Error as e:
        return f'An error occurred: {e}'
    finally:
        conn.close()

@app.route('/delete')
def delete_db():
    try:
        conn = sqlite3.connect('task4db.sqlite')
        curr = conn.cursor()
        curr.execute('DELETE FROM User')
        conn.commit()
        return 'Deleted Successfully'
    except:
        return 'Deletion Failed'

@app.route('/read')
def read():
    try:
        conn = sqlite3.connect('task4db.sqlite')
        curr = conn.cursor()
        curr.execute('SELECT id, name FROM User') 
        results = curr.fetchall()
        conn.commit()
        table = "<table><tr><th>ID</th><th>Name</th></tr>"
        for result in results:
            table += "<tr><td>{}</td><td>{}</td></tr>".format(result[0], result[1])
        table += "</table>"
        return table
    except:
        return 'Reading Failed'

if __name__ == '__main__':
    app.run(debug=True)
