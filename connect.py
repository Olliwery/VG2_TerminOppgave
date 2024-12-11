# from flask import Flask

# import mysql.connector


# def get_db_connection():
#     # Replace these with your actual database details
#     connection = mysql.connector.connect(
#         host="10.2.3.74",  # IP address of your Raspberry Pi
#         user="TerminOppgave2",           # MariaDB username
#         password="TerminOppgave2",   # MariaDB password
#         database="Termin2VG2"  # Your database name
#     )
#     return connection


# # Connect to the database
# mydb = mysql.connector.connect(
#     host="10.2.3.74",  # IP address of your Raspberry Pi
#     user="TerminOppgave2",           # MariaDB username
#     password="TerminOppgave2",   # MariaDB password
#     database="Termin2VG2"  # Your database name
# )

# mycursor = mydb.cursor()

# # Execute a valid SQL query
# mycursor.execute("SELECT * FROM Brukere;")  # Replace 'some_table' with your table name

# # Fetch and print the results
# resultat = mycursor.fetchall()
# print(resultat)
