import mysql.connector


f = open("./alx_book_store.sql")

sql_query = f.read()


mydb = mysql.connector.connect(
    host  = "localhost",
    user = "amine",
    password= "password"
)


try:
    mydb.connect()

    curssor = mydb.cursor()

    curssor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    curssor.execute(sql_query) 

    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error  : 
    print("cannot connect to database ")
