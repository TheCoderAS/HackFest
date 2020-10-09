import pymysql as db
conn=db.connect("localhost","root","","showroom")
cur = conn.cursor()

# #################################################prospect functions############################################
def monitor():

        def insertitem1():
            prospId=input("enter prospect id")
            prospName=input("enter prospect name")
            prospPhone=input("enter prospect phone")
            prospAddress=input("Enter prospect address ")
            interestedModel=input("enter interested model")
            interestedColor=input("enter interested model color")
            dateOfVisit=input("enter date of visit ")
            dayOfVisit=input("enter day of visit")
            bookingAmount=input("enter amount")
            gender=input("enter your Gender")
            incomeGroup=input("enter your income group")
            priority=input("enter priority type like high or low")
            purcharsemode=input("enter your purchese mode")

            insqry=f"insert into prospect values('{prospId}','{prospName}','{prospPhone}','{prospAddress}','{interestedModel}','{interestedColor}','{dateOfVisit}','{dayOfVisit}','{bookingAmount}','{gender}','{incomeGroup}','{priority}','{purcharsemode}')"
            if cur.execute(insqry):
                print("record inserted")
            conn.commit()
            viewall1()


        def deleteitem1():
            prospid=input("enter prospId to delete record")
            delqry=f"delete from prospect where prospId={prospid}"
            if cur.execute(delqry):
                print("record deleted")
            conn.commit()
            viewall1()


        def searchitem1():
            prospid=input("enter prospId  to search record ")
            searchqry=f"select * from prospect where prospId={prospid}"
            cur.execute(searchqry)
            rs=cur.fetchall()
            for i in rs:
                for j in i:
                    print(j,end=" ")





        def viewall1():
            viewqry="""select * from prospect"""
            cur.execute(viewqry)
            rs=cur.fetchall()
            print(rs)

        def viewall2():
            viewqry="""select * from carsale"""
            cur.execute(viewqry)
            rs=cur.fetchall()
            print(rs)

        while True:
            choice = input("Select which you want\n1. insert in prospect\n2. Delete from prospect\n3. Search prospect\n4. View prospect \n5. view carsale\n6. Exit")
            if choice=='1':
                insertitem1()
            elif choice=='2':
                deleteitem1()
            elif choice=='3':
                searchitem1()
            elif choice=='4':
                viewall1()
            elif choice=='5':
                viewall2()
            else:
                exit()





# ##########################################Employee functions#################################################################
def admin():
        def insertitem():
            userName=input("enter userName")
            userPass=input("enter userpass")
            userType=input("enter usertype")
            fullName=input("full name")
            gender=input("enter your gender")
            phone=input("enter phone no")
            email=input("enter email no")
            status=input("enter status ")

            insqry=f"insert into employee values('{userName}','{userPass}','{userType}','{fullName}','{gender}','{phone}','{email}','{status}')"
            if cur.execute(insqry):
                print("record inserted")
            conn.commit()
            viewall()


        def deleteitem():
            userid=input("enter userName to delete record")
            delqry=f"delete from employee where userName={userid}"
            if cur.execute(delqry):
                print("record deleted")
            conn.commit()
            viewall()


        def searchitem():
            userid=input("enter userName to search record ")
            searchqry=f"select * from employee where userName={userid}"
            cur.execute(searchqry)
            rs=cur.fetchall()
            for i in rs:
                for j in i:
                     print(j, end=" ")

        def view_model():
            viewqry="""select * from carmodels"""
            cur.execute(viewqry)
            rs=cur.fetchall()
            print(rs)

        def viewall():
            viewqry="""select * from employee"""
            cur.execute(viewqry)
            rs=cur.fetchall()
            print(rs)

        def viewall2():
            viewqry="""select * from carsale"""
            cur.execute(viewqry)
            rs=cur.fetchall()
            print(rs)

        while True:
            choice = input(
                "Select which you want\n1. insert employees\n2. Delete employees\n3. Search employees\n4. View employees\n5. view car model\n6. view carsale\n7.Exit")
            if choice == '1':
                insertitem()
            elif choice == '2':
                deleteitem()
            elif choice == '3':
                searchitem()
            elif choice == '4':
                viewall()
            elif choice =='5':
                view_model()
            elif choice =='6':
                viewall2()
            else:
                exit()
  ##############################################################################################
while True:
    choice=input("Enter choice\n1.Admin\n2.Monitor")
    if choice=='1':
        admin()
    else:
        monitor()
cur.close()
conn.close()

