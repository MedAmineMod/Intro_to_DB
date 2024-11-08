import mysql.connector


f = open("./alx_book_store.sql")

sql_query = f.read()


mydb = mysql.connector.connect(
    host  = "localhost",
    user = "amine",
    password= "password"
)

if (mydb.is_connected() ==  True ):
    
    print("Database 'alx_book_store' created successfully!")

    curssor = mydb.cursor()
    curssor.execute(sql_query)

else : 

    print("cannot connect to database")
