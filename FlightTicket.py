class IDD:
    def jalal(self,idd):
        self.idd=idd
yy=IDD()
class common:
    tflag=10
    pcount=0
    price=3500
    al=[]
    s=0
jd=common()
class cashier:
    psng=2022
    psl=[]
    c=0
class passenger(common):
    def __init__(self,name,age,mailid,phno,status):
        self.name=name
        self.age=age
        self.mailid=mailid
        self.phno=phno
        self.status="Ticket is waiting for confirmation"
    pas=False
def checkavailable():
    if(jd.pcount<jd.tflag):
        j=jd.tflag-jd.pcount
        print("Available tickets are: ",j)
    else:
        print("Ticket not available")
    print("Ticket price is : 3,500")
def amount():
    amt=0
    if(1<=jd.pcount):
        amt=jd.pcount*jd.price
        print("The total fare is:",amt)
def approve():
    if(jd.s==1):
        print("Ticket is already approved")
    else:
        if(jd.pcount<jd.tflag):
            for i in range(len(jd.al)):
                jd.al[i].status="Tickets has been issued successfully"
        else:
            print("Ticket not approved")
def cashlogin():
    while True:
        print("1.approve\n2.issue Ticket\n3.logout")
        n=int(input())
        s=0
        if(n==1):
            print("your ticket is approved enjoy the journey....."),approve()
        elif(n==2):
            if(len(jd.al)==0):
                print("--------Ticket not yet booked--------")
            else:
                print('\n your id is: ',yy.idd)
                for i in range(len(jd.al)):
                    print("Your name is:",jd.al[i].name)
                    print("Your age is:",jd.al[i].age)
                    print("Your mail id is:",jd.al[i].mailid)
                    print("Your Mobile no  is: ",jd.al[i].phno)
                    print("Your status is:",jd.al[i].status)
                amount()
        else:
            break
def pasLogin():
    while True:
        print("1.check availability\n2.Book Ticket\n3.Fare\n4.Passenger Details\n5.Cancel Ticket\n6.Log out")
        n=int(input())
        if n==1:
            checkavailable()
        elif n==2:
            print("How many tickets need to add: ")
            m=0
            m=int(input())
            for i in range(0,m):
                n=input("Name:\n")
                ag=int(input("Age:\n"))
                mail=input("Mail id:\n")
                phno=int(input("Mobile no:\n"))
                status=0
                sithik=passenger(n,ag,mail,phno,status)
                jd.al.append(sithik)
            jd.pcount+=m
        elif n==3:
            print("Ticket count is:",jd.pcount)
            print("Your ticket amount is:",jd.pcount * jd.price)
        elif n==4:
            if(len(jd.al)==0):
                print("--------Ticket not yet booked--------")
            else:
                f=open("passengerdetails.txt","w")
                print("\n Your id is:",yy.idd)
                f.write(str(yy.idd)+"\n")
                for i in range(len(jd.al)):
                    print("Name:",jd.al[i].name)
                    print("Age:",jd.al[i].age)
                    print("Mail id:",jd.al[i].mailid)
                    print("Mobile no: ",jd.al[i].phno)
                    print("Status:",jd.al[i].status)
                    f.write("Name:"+jd.al[i].name+"\n"+"Age:"+str(jd.al[i].age)+"\n"+"Mail id:"+jd.al[i].mailid+"\n"+"Mobile no:"+str(jd.al[i].phno)+"\n"+"Status:"+str(jd.al[i].status)+"\n")
                if(1<=jd.pcount):
                            amt=jd.pcount*jd.price
                            print("Total fare is:",amt)
                f.write("Total fare is: "+str(amt))
        elif n==5:
            m=input("Do you wanna cancel your Ticket? (yes or no): ").lower()
            if(m=="yes"):
                jd.al=[]
                print("Your ticket has been cancelled")
            else:
                print("Your ticket not yet cancelled")
        else:
            break
def __main__():
    print("Hyyy There, welcome to the flight ticket reseration system.")
    while True:
        print("1.Login\n2.Exit")
        a=int(input())
        if a==1:
            while True:
                print("1.Passenger\n2.Cashier\n3.Back")
                b=int(input())
                if b==1:
                    while True:
                        print("1.Signup\n2.Signin\n3.Logout")
                        c=int(input())
                        if c==1:
                            print("To create an account")
                            s1=[]
                            v=input("Enter New Username: ")
                            s1.append(v)
                            yy.jalal(v)
                            s1.append(input("Create password: "))
                            f=1
                            s1.append(cashier.psng)
                            print("Successfully account created......")
                            print("Your Registration Number is Generated: \t",cashier.psng)
                            cashier.psng+=1
                            s1.append(0)
                            s1.append("No Results Found")
                            cashier.psl.append(s1)
                        elif c==2:
                            rg=int(input("Enter Reg No:\n"))
                            ps=input("Enter Password:\n")
                            if rg<2022 or cashier.psng<=rg:
                                print("Passenger not found")
                            else:
                                print("Account successfully logged in......")
                                if cashier.psl[rg-2022][1]==ps:
                                    pasLogin()
                                else:
                                    print("Password Mismatch")
                        else:
                            break
                elif b==2:
                    cashlogin()
                else:
                    break
        else:
            break
__main__()
