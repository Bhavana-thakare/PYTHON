print("..Welcome to Gmail..'")
print("Open your gmail and go to setting")
print("tap on 'add anohter account'")
Device=input("select the device:")
if Device=="google":
    print("you selected google to make your gmail Id")
    print("cheking information")
    print("Draw your pattern")
    User=input("process you want to do:")
    if User=="sign in":
        print("Use your google account")
        Email=input("enter Email or phone number:")
        if Email=="bhavnathakare03@gmail.com":
            print("Ok this is correct email or phone number")
            Pass=input("enter the passwoard")
            if Pass=="bhavna18":
                print("correct password")
                print("You are in.")
            else:
                print("wrong password")
        else:
            print("wrong email")
    elif User=="creat new account":
        print("Creating new gmail account")
        Creat=input("Enter to why you want to make id:")
        if Creat=="for myself":
            print("You have to fell the information")
            Name1=input("Enter your first name:")
            Name2=input("Enter your last name:")
            if Name1=="Bhavana"and Name2=="thakare":
                print("you correctly entered your name")
                Birth_date=int(input("Enter your birth date:"))
                if Birth_date>=1 and Birth_date<=30:
                    print("correct date")
                    Birth_month=int(input("Enter the month:"))
                    if Birth_month>=1 and Birth_month<=12:
                        print("Month is correct")
                        Birth_year=int(input("Enter the year:"))
                        if Birth_year>=0 and Birth_year<=2021:
                            print("year is correct")
                            Gender=input("Enter the Gender:")
                            if Gender=="female" or "male" or "Other":
                                print("verifying your information")
                                print("Select any one gmail address or make your own gmail address")
                                address=input("Enter the gmail address:")
                                if address=="bhavnathakare03@gmail.com":
                                    print("correct gmail")
                                    print("Make your confirm password")
                                    Pass=int(input("Enter the password:"))
                                    alph=input("Enter the alphabate:")
                                    if alph=="bhavna":
                                        print("alphabate was added to password")
                                        spch=input("Enter the Special character:")
                                        if spch=="@" or spch=="#" or spch=="*" or spch=="$":
                                            print("Special character was added to password")
                                            Numr=int(input("Enter the numbers:"))
                                            if Numr>=0 and Numr<=9:
                                                print("Number was added in password")
                                                print("it is strong password")
                                                Ver=input("Did you complted your login:")
                                                if Ver=="yes":
                                                    print("Verify your gmail address....")
                                                    print("you are done")
                                                    print("Thank you so much")
                                                else:
                                                    print("something went wrong")
                                            else :
                                                print("It is not a number")
                                        else:
                                            print("It is not special character")
                                    else:
                                        print("It is not alphabate")
                                else:
                                    print("wrong gmail")
                            else:
                                print("Something wrong")
                        else:
                            print("something wrong")
                    else:
                        print("Something wrong")
                else:
                    print("Something wrong")
            else:
                print("Wrong name")
        elif Creat=="To manage my business":
            print("you have to make id for business work")
            Name1=input("Enter your first name:")
            Name2=input("Enter your last name:")
            if Name1=="Bhavana"and Name2=="thakare":
                print("you correctly entered your name")
                Birth_date=int(input("Enter your birth date:"))
                if Birth_date>=1 and Birth_date<=30:
                    print("correct date")
                    Birth_month=int(input("Enter the month:"))
                    if Birth_month>=1 and Birth_month<=12:
                        print("Month is correct")
                        Birth_year=int(input("Enter the year:"))
                        if Birth_year>=0 and Birth_year<=2021:
                            print("year is correct")
                            Gender=input("Enter the Gender:")
                            if Gender=="female" or "male" or "Other":
                                print("verifying your information")
                                print("Select any one gmail address or make your own gmail address")
                                address=input("Enter the email address or creat one email address")
                                if address=="bhavanathakare20@navgurukul.com":
                                    print("Correct email address")
                                    Pass=int(input("Enter the password:"))
                                    alph=input("Enter the alphabate:")
                                    if alph<="A"and alph>="Z" or alph<="a"and alph>="b":
                                        print("alphabate was added to password")
                                        spch=int(input("Enter the Special character:"))
                                        if spch=="@" or spch=="#" or spch=="*" or spch=="$":
                                            print("Special character was added to password")
                                            Numr=int(input("Enter the numbers:"))
                                            if Numr<=0 and Numr>=9:
                                                print("Number was added in password")
                                                print("it is strong password")
                                                Ver=input("Did you complted your login")
                                                if Ver=="yes":
                                                    print("Verify your gmail address....")
                                                    print("you are done")
                                                    print("Thank you so much")
                                                else:
                                                    print("something went wrong")
                                            else :
                                                print("It is not a number")
                                        else:
                                            print("It is not special character")
                                    else:
                                        print("It is not alphabate")
                                else:
                                    print("wrong gmail")
                            else:
                                print("Something wrong")
                        else:
                            print("something wrong")
                    else:
                        print("Something wrong")
                else:
                    print("Something wrong")
            else:
                print("Wrong name")
        else:
            print("Something is wrong")
    else:
        print("Something is wrong")
else:
    print("Error")
                                    
            