print("Starting app")
from flask import Flask, request, render_template
import mysql.connector

print("Imports done")
app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Codexx@22',
    'database': 'collage'
}

print("App created")

@app.route('/')
def show_form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    email = request.form['email']
    password = request.form['password']
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO submissions (email, password) VALUES (%s, %s)", (email, password))
    conn.commit()
    cursor.close()
    conn.close()
    
    return "Thanks! Your info was saved!"

print("Routes defined")

if __name__ == '__main__':
    print("Starting Flask")
    app.run(debug=True)