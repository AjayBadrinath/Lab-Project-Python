def createdb(dbase,password):
    import mysql.connector as c
    db=c.connect(host='localhost',user='root',passwd=password)
    cursor=db.cursor()
    try:
        cursor.execute("create database {};".format(dbase))
        return "success"

    except Exception as e:
        return "Failure"
def showdb(password):
    import mysql.connector as c
    db=c.connect(host='localhost',user='root',passwd=password)
    cursor=db.cursor()
    cursor.execute("show databases;")
    l=[]
    for i in cursor:
        l.append(i)
    return l

def createtable(password,dbase,tname,cols):
    import mysql.connector as c
    db=c.connect(host='localhost',user='root',passwd=password,database=str(dbase))
    cursor=db.cursor()
    try:
        cursor.execute("create table {} {};".format(tname,cols))
        return "Done"
    except:
        return "False"

def struct(password,dbase,tname):
    import mysql.connector as c
    db=c.connect(host='localhost',user='root',passwd=password,database=str(dbase))
    cursor=db.cursor()
    cursor.execute("desc %s"%tname)
    x=['Field','Type','Null','Key','Default','Extra']
    r=cursor.fetchall()
    l=[]
    for i in r:
        l.append(i)
    return l,x
    
def insert(password,dbase,tname,cols,values):
    import mysql.connector as c
    db=c.connect(host='localhost',user='root',passwd=password,database=str(dbase))
    cursor=db.cursor()
    try:
        cursor.execute("INSERT INTO {}{}VALUES{}  ").format(tname,cols,values)
        return True
    except:
        return "Error"
def update(val,password,dbase,tname,cols,condition):
    import mysql.connector as c
    db=c.connect(host='localhost',user='root',passwd=password,database=str(dbase))
    cursor=db.cursor()
    for i in range(0,val):
        try:
            x="UPDATE {} set {} where {};".format(tname,cols,condition)
            cursor.execute()
            x=cursor.rowcount
        except:
            print("Error")

def fetch(password,dbase,tname,cols,condition):
    import mysql.connector as c
    try:
        db=c.connect(host='localhost',user='root',passwd=password,database=str(dbase))
        cursor=db.cursor()
        cursor.execute("select {} from {} {};".format(cols,tname,condition))
        res=cursor.fetchall()
        l=[]
        cols=[]
        
        for i in res:
            l+=i
        cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='{}' ORDER BY ORDINAL_POSITION;".format(str(tname)))
        cols=cursor.fetchall()
        return cols,l
    except:
       return " Error"

def delt(passwd,dbase,tname,cols,values):
    import mysql.connector as c
    db=c.connect(host='localhost',user='root',passwd=password,database=str(dbase))
    cursor=db.cursor()
    cursor.execute("Delete from {} where {}={}".format(tname,cols,values))
def dropdb(dname,dbase,password):
    import mysql.connector as c
    db=c.connect(host='localhost',user='root',passwd=password,database=str(dbase))
    cursor=db.cursor()
    try:
        cursor.execute("drop database{};".format(dname))
        return True
    except:
        return False
def alteradd(passwd,dbase,tname,):
    import mysql.connector as c
    db=c.connect(host='localhost',user='root',passwd=password,database=str(dbase))
    cursor=db.cursor()
    try:
        cursor.execute("Alter table {} add {}{} {}".format())
        return True
    except:
        return False


    
    
    
