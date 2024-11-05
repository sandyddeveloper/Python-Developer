import mysql.connector # for connecting Sql

conf = {'host':'localhost',
                'port': 3306,
                'user': 'root',
                'password': 'root123',
                'database': 'CURD'
                } 

def insertStudent(a, b, c , d, e , f):
        config = conf#deatils about database

        cnx = mysql.connector.connect(**config) # connect the  
        # Create a cursor object
        cursor = cnx.cursor()
        sql = f"insert into StudentWeb5 values({a},'{b}',{c},'{d}', '{e}', '{f}')"    
        print(sql)
        cursor.execute(sql)    
        cnx.commit() # for saving the data
        cursor.close()
        
insertStudent(2, "SANDY4", 9345933866, "no77, guduvancheriui", '2003-12-18', '2024-11-20' )

def readStudents(a):
        config = conf

        cnx = mysql.connector.connect(**config) # connect the  
        # Create a cursor object
        cursor = cnx.cursor()
        sql = f"select * from StudentWeb5 where id = {a}"    
        print(sql)
        cursor.execute(sql)    
        # cnx.commit() # for saving the data
        # cursor.close()
        for a in cursor.fetchall():
            print(a)
# readStudents(2)

def readStudents():
        config = conf

        cnx = mysql.connector.connect(**config) # connect the  
        # Create a cursor object
        cursor = cnx.cursor()
        sql = f"select * from StudentWeb2"    
        print(sql)
        cursor.execute(sql)    
        # cnx.commit() # for saving the data
        # cursor.close()
        for a in cursor.fetchall():
            print(a)
# readStudents()

def deleteStudents(a):
        config = conf

        cnx = mysql.connector.connect(**config) # connect the  
        # Create a cursor object
        cursor = cnx.cursor()
        sql = f"delete  from StudentWeb5 where id = {a}"    
        print(sql)
        cursor.execute(sql)    
        cnx.commit() # for saving the data
        cursor.close()
# deleteStudents(2)
        

