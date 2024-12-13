from flask import Flask, render_template, request
import random
import mysql.connector
import sys
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)  # Generates a random key each time the app restarts


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
    username = session.get('username')  # Get the username from the session if logged in
    return render_template('home.html', username=username)


@app.route('/register')
def GoToRegister():
    return render_template('register.html')


from flask import redirect, url_for, session

@app.route('/register_post', methods=['POST'])
def register():
    username = request.form['name']
    email = request.form['email']
    password = request.form['password']

    conn = get_db_connection()
    cursor = conn.cursor()

    # Insert the new user into the database
    query = "INSERT INTO Brukere (username, email, passord) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, email, password))
    conn.commit()

    cursor.close()
    conn.close()

    # Save the username in the session
    session['username'] = username

    # Redirect to the home page
    return redirect(url_for('root'))



@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_post', methods=['POST'])
def login_post():
    username = request.form['name']
    email = request.form['email']
    password = request.form['password']

    conn = get_db_connection()
    cursor = conn.cursor()

    # Check if the user exists in the database
    query = "SELECT * FROM Brukere WHERE username = %s AND email = %s AND passord = %s"
    cursor.execute(query, (username, email, password))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:
        # Save the username in the session
        session['username'] = username

        # Redirect to the home page
        return redirect(url_for('root'))
    else:
        # Show an error message if login fails
        return render_template('login.html', error="Feil brukernavn, e-post eller passord.")


@app.route('/logout')
def logout():
    session.clear()  # Clears all session data
    return redirect(url_for('root'))  # Redirects to the homepage



# Single '/omoss' route
@app.route('/omoss')
def omoss():
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
def kontaktoss():
    return render_template('kontaktoss.html')

@app.route('/snake')
def snake():
    return render_template('snake.html')

@app.route('/Pizza')
def Pizzas():
    num = random.random()
    print(num)
    liste = "Erik, Nai, Oronai"
    return render_template('Pizza.html', sendesInn=num, noeAnnet="Her er det", Baka=liste)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='4500')
