import sqlite3 as db
conn = db.connect("empmanagement2")
cur = conn.cursor()

# #################################################employee table#####################################3
crquery="""create table if not exists employee
                   (  userid varchar(45) primary key,
                       userpass text,
                       usertype text,
                       fullname text,
                       phone text,
                       email text,
                       status text
                    ); """

if cur.execute(crquery):
    print("table created")

inse=f"insert into employee values('E005', 'password' , 'admin' ,'kuldeep', '8512099003','kuldeep@gmail.come','activated')"

if cur.execute(inse):
    print("record inserted")
    conn.commit()
# prospect table
crqry1="""create table if not exists prospect
(
   prospid int primary key,
   prospname varchar(45),
   prospphone varchar(45),
   prospaddress varchar(45),
   interestedmodel varchar(45),
   interestedcolor varchar(45),
   dateofvisit varchar(20),
   priority varchar(45))"""
if cur.execute(crqry1):
    print("table created")

inser=f"insert into prospect values(101,'abhishek','7903934401','patna','BMW','black','20jul2020','high')"
if cur.execute(inser):
    print("prospect inserted")



# #################################################prospect functions############################################
def admin():

        def insertitem():
            prospid=input("enter prospect id")
            prospname=input("enter prospect name")
            prospphone=input("enter prospect phone")
            prospaddress=input("Enter prospect address ")
            interestedmodel=input("enter interested model")
            interestedcolor=input("enter interested model color")
            dateofvisit=input("enter date of visit ")
            priority=input("enter priority type like high or low")

            insqry=f"insert into prospect values({prospid},'{prospname}','{prospphone}','{prospaddress}','{interestedmodel}','{interestedcolor}','{dateofvisit}','{priority}')"
            if cur.execute(insqry):
                print("record inserted")
            conn.commit()
            viewall()


        def deleteitem():
            prospid=input("enter userid to delete record")
            delqry=f"delete from employee where userid={prospid}"
            if cur.execute(delqry):
                print("record deleted")
            conn.commit()
            viewall()


        def searchitem():
            prospid=input("enter userid to search record ")
            searchqry=f"select * from employee where userid={prospid}"
            if cur.execute(searchqry):
                rs=cur.fetchall()
                for i in rs:
                    for j  in i:
                        print(j,end=" ")



        def viewall():
            viewqry="""select * from prospect"""
            cur.execute(viewqry)
            rs=cur.fetchall()
            print(rs)

        choice = input("Select which you want\n1. insert item\n2. Delete item\n3. Search item\n4. View all item\n5.Exit")
        if choice=='1':
            insertitem()
        elif choice=='2':
            deleteitem()
        elif choice=='3':
            searchitem()
        elif choice=='4':
            viewall()
        else:
            exit()





# ##########################################Employee functions#################################################################
def monitor():
        def insertitem():
            userid=input("enter username")
            userpass=input("enter userpass")
            usertype=input("enter usertype")
            fullname=input("full name")
            phone=input("enter phone no")
            email=input("enter email no")
            status=input("enter status ")

            insqry=f"insert into employee values({userid},'{userpass}','{usertype}','{fullname}','{phone}','{email}','{status}')"
            if cur.execute(insqry):
                print("record inserted")
            conn.commit()
            viewall()


        def deleteitem():
            userid=input("enter userid to delete record")
            delqry=f"delete from employee where userid={userid}"
            if cur.execute(delqry):
                print("record deleted")
            conn.commit()
            viewall()


        def searchitem():
            userid=input("enter userid to search record ")
            searchqry=f"select * from employee where userid={userid}"
            if cur.execute(searchqry):
                rs=cur.fetchall()
                for i in rs:
                    for j  in i:
                        print(j,end=" ")



        def viewall():
            viewqry="""select * from employee"""
            cur.execute(viewqry)
            rs=cur.fetchall()
            print(rs)

        choice = input(
            "Select which you want\n1. insert item\n2. Delete item\n3. Search item\n4. View all item\n5.Exit")
        if choice == '1':
            insertitem()
        elif choice == '2':
            deleteitem()
        elif choice == '3':
            searchitem()
        elif choice == '4':
            viewall()
        else:
            exit()
  ##############################################################################################

choice=input("Enter choice\n1.Admin\n2.Monitor")

if choice==1:
    passw=input("enter password")
    if passw=='pass':
        admin()
    else:
        print("wrong password")

else:
    passw=input("Enter password")
    if passw=='pass':
        monitor()
    else:
        print("Wrong password")




