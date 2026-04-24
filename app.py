from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS responses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT,
        q1 INTEGER,
        q2 INTEGER,
        q3 INTEGER,
        score INTEGER,
        level TEXT
    )
    ''')

    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():

    company = request.form['company']
    q1 = int(request.form['q1'])
    q2 = int(request.form['q2'])
    q3 = int(request.form['q3'])

    score = q1 + q2 + q3

    if score <=3:
        level="Débutant"
    elif score <=6:
        level="Intermédiaire"
    else:
        level="Avancé"

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("""
    INSERT INTO responses(company,q1,q2,q3,score,level)
    VALUES(?,?,?,?,?,?)
    """,(company,q1,q2,q3,score,level))

    conn.commit()
    conn.close()

    return render_template("result.html",
                           company=company,
                           score=score,
                           level=level)

@app.route('/admin')
def admin():

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT * FROM responses")
    data = c.fetchall()

    conn.close()

    return render_template("admin.html",data=data)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
