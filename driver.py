import func as f
from prettytable import PrettyTable
import getpass
def menu():
    try:
        a=int(input("1.Create Database\n2.Show Databases \n3.Create Table\n 4.structure of table \n5.Alter Table\n6.Insert value in the table\n7.update table\n8.Delete database\n9Alter table\n10.Delete inside table"))

        passwd=input("Enter your my sql database password")
        dbase=input("Enter the name of the database")
        if a==1:
            
            
            y=input("Enter DataBase name")
            ret=f.createdb(y,passwd)
            if ret=="success":
                print("Your Database Has been Created successfully")
                print("----"*30)
                menu()
            else:
                print("Database Creation Unsuccessful")
        elif a==2:
            x=PrettyTable()
            x.field_names=["DATABASES"]
            p=f.showdb(passwd)
            for i in p:
                x.add_row(list(i))
            print(x)
            menu()
        elif a==3:
            global l
            w=input("Enter Database Name")
            tname=input("Enter the name of the table to create")
            l=[]
            cnt=int(input("Enter the no of columns to create"))
            for i in range(0,cnt):
                q=input("Enter column Name")
                data=input("Enter Datatype of the col")
                width=input("Enter width of column")
                constr=input("Enter column constraint if any else enter space")
                l+=[q+" "+data+"("+width+")"+constr]
            print(l)
            a="("
            for i in l:
                a+=i+","
            a+=")"
            k=""
            k+=a[0:-2]
            k+=")"
            
            b=f.createtable(passwd,w,tname,k)
            if b =="Done":
                print("The table ",tname,"has been created")
                menu()
            else:
                print("Table creation unsuccessful")
                menu()
        elif a==4:
            dbase=input("enter database name")
            tname=input("Enter table name")
            x1=f.struct(passwd,dbase,tname)
            x2=PrettyTable()
            x2.field_names=x1[-1]
            for i in x1[0]:
                x2.add_row(i)
            print(x2)
            menu()
                    
        elif a==5:
            tname=input("Enter the name of the table")
            count=int(input("Enter the no of values to insert"))
            colmn=[]
            value=[]
            for i in range(0,count):
                clm=input("Enter column name")
                value1=input("Enter the value")
                colmn+=[clm]
                value+=[value1]
                print(colmn,value)
            if f.insert(passwd,dbase,tname,str(tuple(colmn)),str(tuple(value)))==True:
                print("Insert successful")
                menu()
            else:
                print("Not successful")
                menu()
        elif a==6:
            #update table
            tname=input("Enter the table name ")
            col=input("Enter column you want to change")
            condition=input("Enter the condition")
            a=f.update(passwd,dbase,tname,col,condition)
            if a=="Succcess":
                print("Table has been updated")
                menu()
            else:
                print("Error updating")
                menu()

        elif a==7:
            #show data
            tname=input("Enter the table name ")
            colcnt=input("Enter no of columns to enter<type all for all the columns")
            k=""
            if int(colcnt)>0:
                for i in range(0,int(colcnt)):
                    colname=input("Enter the column name ")
                    k+=colname+","
                    if i==int(colcnt)-1:
                        k=k[0:len(k)-1]
                cols=k
                
            else:
                cols="*"
            tname=input("enter table name")
            condition=input("Enter the filter required if any")
            fetched=f.fetch(passwd,dbase,tname,cols,condition)
            colname=[]
            for i in fetched[0]:
                colname+=list(i)
              
            x3=PrettyTable()
            x3.fieldnames=[colname]
            for i in fetched[-1]:
                x3.add_row(i)
            print(x3)
            menu()
        elif a==8:
            dbase=input("Enter database to delete")
            if f.dropdb==True:
                print("Success")
                menu()
            else:
                print("Cannot delete")
                menu()
        elif a==9:
            tname=input("ENter the table to edit")
            cnd=input("Enter cconditon prefixed by add/modify/change")
            alterdd(passwd,dbase,tname,cnd)
            print("Success")
            menu()
        elif a==10:
            tname=input("Enter table name")
            cnd=input("Enter condition")
            f.delt(passwd,dbase,tname,cond)
            print("Done")
            menu()
                                    
    except Exception as e:
        print("Please enter your Correct Password")
        menu()
menu()              
    
