from flask import Flask, render_template
import random
import mysql.connector
import sys

app = Flask(__name__)

# Add the path for importing the connection function if needed
sys.path.append('C:/Users/Yong/Documents/GitHub/VG2_TerminOppgave/TerminOppgaveVG2')

# Database connection function
def get_db_connection():
    connection = mysql.connector.connect(
        host="10.2.3.238",  # IP address of your Raspberry Pi
        user="TerminOppgave2",           # MariaDB username
        password="TerminOppgave2",   # MariaDB password
        database="Termin2VG2"  # Your database name
    )
    return connection

# Define routes
@app.route('/')
def root():
    return render_template('home.html')

@app.route('/loginregister')
def red():
    return render_template('loginregister.html')

# Single '/omoss' route
@app.route('/omoss')
def blue():
    # Get a database connection
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    # Query the database
    cursor.execute("SELECT * FROM Brukere")  # Replace 'Brukere' with your actual table name
    result = cursor.fetchall()  # Fetch all results

    cursor.close()
    db_connection.close()

    # Pass the data to the template
    return render_template('omoss.html', data=result)

@app.route('/kontaktoss')
def green():
    return render_template('kontaktoss.html')

@app.route('/snake')
def snake():
    return render_template('snake.html')

@app.route('/cookies')
def data():
    num = random.random()
    print(num)
    liste = "Erik, Nai, Oronai"
    return render_template('cookies.html', sendesInn=num, noeAnnet="Her er det", Baka=liste)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='4500')
