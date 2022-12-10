import PyPDF2
import maskpass
import sys
import mysql.connector as mys
from getpass import getpass
from tabulate import tabulate

def main():
    print("do you want to")
    print("1. HIRE")
    print("2. TO BE HIRED")
    ch=int(input("enter your choice"))
    while (True):
        if ch==1:
            hire()
        elif ch==2:
            be_hired()
        else:
            print("wrong choice choose again")
            main()

def hire():
    print("1.Do you want to Login?")
    print("2.Do you want to Register?")
    print("3.ANALYTICS AND REPORTING")
    ch=int(input(" What would you like to do?"))
    while (True):
        if ch==1:
            login()
            password()
        elif ch==2:  
            register()
            password()
        elif ch==3:
            analytics_reporting()
        else:
            print("Wrong choice choose again")
            hire()
            

    
def register_hire():#register for the hire
    try:
        com=mys.connect(host="localhost",user="root",passwd="jeffjude",database="register")
        mycursor=con.cursor()
        EMAIL=input("enter your Email id")
        NAME=input("enter your full name")
        PASSWORD=int(input("enter your password"))

        a="insert into employees values('{}','{}','{}')".format(EMAIL,NAME,PASSWORD)

        mycursor.execute(a)
        con.commit()
        print("you have been registered")

    except exception as e:
        print(e)
    finally:
        if con.is_connected():
            mycursor.close()
            con.close()


def password():#password for register
    pwd = maskpass.askpass(prompt="Password:", mask="#")
    print(pwd)
    
def login_hire():
    try:
        com=mys.connect(host="localhost",user="root",passwd="jeffjude",database="register")
        mycursor=con.cursor()
        EMAIL=input("enter your Email id")
        NAME=input("enter your full name")
        PASSWORD=int(input("enter your password"))

        a="insert into employees values('{}','{}','{}',{})".format(EMAIL,NAME,COMPANY,PHNO)

        mycursor.execute(a)
        con.commit()
        print(" WELCOME ")

    except exception as e:
        print(e)
    finally:
        if con.is_connected():
            mycursor.close()
            con.close()
    search()
                  
def search():
    print(" WELCOME TO THE EMPLOYEE RECRUITMENT PLATFORM")
    print("1.would you like to recruit with soft skills as parameter?")
    print("2.would you like to recruit with hard skills as parameter?")
    ch=int(input("enter your choice"))
    if ch==1:
        soft_skills()
    elif ch==2:
        hard_skills()
    else:
        print("wrong choice please enter again")

def soft_skills():
    try:
        print("__________________________________________")
        print("++++++ SOFT SKILLS AVAILABLE NAMELY:++++++")
        print("experience in communications")
        print("experience in teamwork")
        print("experience in problem solving")
        print("experience in time management")
        print("experience in critical thinking")
        print("experience in desicion making")
        print("experience in stress management")
        print("__________________________________________")
        
        con=mys.connect(host="localhost",user="root",passwd="jeffjudev",database="softskills")
        mycursor=con.cursor()
        EMPNO=int(input("enter the employee issued number"))
        q="select * from softskills1 where EMPNO={}".format(EMPNO)
        mycursor.execute(q)
        rows=mycursor.fetchall()

def hard_skills():
        print("__________________________________________")
        print("computer skills")
        print("analytical skills")
        print("Marketing skills")
        print("presentation skills")
        print("management skills")
        print("project management skills")
        print("____________________________________________")

        con=mys.connect(host="localhost",user="root",passwd="jeffjudev",database="hardskills")
        mycursor=con.cursor()
        EMPNO=int(input("enter the employee issued number"))
        q="select * from hardskills1 where EMPNO={}".format(EMPNO)
        mycursor.execute(q)
        rows=mycursor.fetchall()
except exception as e:
    print(e)
        finally:
            if con.is_connected():
                mycursor.close()con.close()



          
    
def be_hired():
    int("2.Do you want to Register?")
    ch=int(input(" What would you like to do?"))
    while (True):
        if ch==1:
            be_hired_login()
        elif ch==2:
            be_hired_register()
        else:
            print("wrong choice")

def be_hired_register():
    try:
        com=mys.connect(host="localhost",user="root",passwd="jeffjude",database="hired")
        mycursor=con.cursor()
        EMAIL=input("enter your Email id")
        NAME=input("enter your full name")
        PASSWORD=int(input("enter your password"))

        a="insert into employee1 values('{}','{}','{}',{})".format(EMAIL,NAME,PASSWORD)

        mycursor.execute(a)
        con.commit()
        print("you have been registered")

    except exception as e:
        print(e)
    finally:
        if con.is_connected():
            mycursor.close()
            con.close()
    
def be_hired_login():
    try:
        com=mys.connect(host="localhost",user="root",passwd="jeffjude",database="hired")
        mycursor=con.cursor()
        EMAIL=input("enter your Email id")
        NAME=input("enter your full name")
        PASSWORD=int(input("enter your password"))

        a="insert into employee1 values('{}','{}','{}',{})".format(EMAIL,NAME,PASSWORD)

        mycursor.execute(a)
        con.commit()
        print(" WELCOME ")

    except exception an e:
        print(e)
    finally:
        if con.is_connected():
            mycursor.close()
            con.close()
    search()

def main_resume():
    print("1. DO You want to view your resume?")
    print("2. D0 you want to edit your resume?")
    print("3. draft a new resume")
    ch=int(input("enter your choice"))
    while (True):
        if ch==1:
            resume()
        elif ch==2:
            edit_resume()
        elif ch==3:
            new_resume()
        else:
            print("wrong choice enter again//")

def new_resume():
    try:
        con=mys.connect(host="localhost",user="root",passwd="jeffjude",database="hired")
        mycursor=con.cursor()
        NAME=input("enter your name")
        DOB=date(input("enter your date of birth ")
        MAIL=input("input your mail")
        PHNO=int(input("enter your phone number"))
        print("-------E D U C A T I O N----------")
        HIGHSCHOOL=input("enter the name of your highschool")
        HIGHERSR=input("enter the details of your highersr school")
        UNDERGRAD=input("enter the college you have completed your undergraduation")
        OTHERS=input("enter any miscellanious data")

        a="insert into resume values('{}','{}','{}',{},'{}','{}','{}','{}')".format(NAME,DOB,MAIL,PHNO,HIGHSCHOOL,HIGHERSR,UNDERGRAD,OTHERS)

        mycursor.execute(a)
        con.commit()
        print("  ")

     except exception as e:
        print(e)
     finally:
         if con.is_connected():
             mycursor.close()
             con.close()   
        
    
def edit_resume():
    try:
        mycon=mys.connect(host="localhost",user="root",passwd="jeffjudev",database="resume")
        mycursor=mycon.cursor()
        PHNO=int(input("enter the PHONE  number"))
        q="select * from resume where PHNO={}".format(PHNO)
        mycursor.execute(q)
        a=mycursor.fetchone()
        if a!=None:
            print(a)
            while(True):        
                print("1.update name")
                print("2.update DOB")
                print("3.update mail")
                print("4.update phno")
                print("5.update highschool")
                print("6.update highersr")
                print("7.update undergrad")
                print("8.others")
                print("9.back to main menu")
                choice=int(input("enter the choice:"))
                if choice==1:
                    NAME=int(input("enter the new pay index"))
                    sql="update resume set NAME={} where PHNO={}".format(NAME,PHNO)
                    mycursor.execute(sql)
                    mycon.commit()
                    print("the record is updated")
                elif choice==2:
                    DOB=input("enter the DOB")
                    sql="update resume set DOB={} where PHNO={}".format(DOB,PHNO)
                    mycursor.execute(sql)
                    mycon.commit()
                    print("the record is updated")
                elif choice==3:
                    MAIL=input("enter the NEW mail id")
                    sql="update resume set MAIL={} where PHNO={}".format(MAIL,PHNO)
                    mycursor.execute(sql)
                    mycon.commit()
                    print("the record is updated")
                elif choice==5:
                    HIGHSCHOOL=input("enter the name of highschool")
                    sql="update resume set HIGHSCHOOL={} where PHNO={}".format(HIGHSCHOOL,PHNO)
                    mycursor.execute(sql)
                    mycon.commit()
                    print("the record is updated")
                elif choice==6:
                    HIGHERSR=input("enter the name of school/college"))
                    sql="update resume set HIGHERSR={} where PHNO={}".format(HIGHRERSR,PHNO)
                    mycursor.execute(sql)
                    mycon.commit()
                    print("the resume is updated")
                elif choice==4:
                    PHNO=int(input("enter THE phone number"))
                    sql="update resume set PHNO='{}' where PHNO='{}'".format(PHNO,PHNO)
                    mycursor.execute(sql)
                    mycon.commit()
                    print("value has been updated")
                elif choice==7:
                    UNDERGRAD=int(input("enter Your undergrad details"))
                    sql="update resume set UNDERGRAD='{}' where PHNO='{}'".format(UNDERGRAD,PHNO)
                    mycursor.execute(sql)
                    mycon.commit()
                    print("value has been updated")
                elif choice==8:
                    OTHERS=int(input("enter any extra details"))
                    sql="update resume set OTHERS'{}' where PHNO='{}'".format(OTHERS,PHNO)
                    mycursor.execute(sql)
                    mycon.commit()
                    print("value has been updated")
                else:
                    print("re enter again")
               
    except Exception as e:
        print(e)
    finally:
        if mycon.is_connected():
            mycursor.close()
            mycon.close()
            
def resume():
    try:
        con=mys.connect(host="localhost",user="root",passwd="jeffjudev",database="resume")
        mycursor=con.cursor()

        
        sql="select * from resume"
        mycursor.execute(sql)
        data=mycursor.fetchall()
        print(tabulate(data,headers=['NAME','DOB','MAIL','PHNO','SALARY','HIGHSCHOOL','HIGHERSR','UNDERGRAD','OTHERS'],tablefmt='fancy_grid'))


    except Exception as e:
            print(e)
    finally:
        if con.is_connected():
            mycursor.close()
            con.close()

def analyitcs_reporting():
    
    
    




















    
