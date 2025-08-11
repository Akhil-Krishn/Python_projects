try:
    import mysql.connector as mc

    con = mc.connect( host = "localhost" , user = "root" , password = "password" )

    cur = con.cursor()

    # name = input("Enter databse name: ") # can be arbritary or inputable
    name = "Focus"
    cur.execute("create database " + name)
    print("created database " + name +  " succesfully")
    first_time = True
except:
    first_time = False