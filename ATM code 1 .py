print("'..Welcome to SBI bank..'")
balance=50000
Start=input("Did you started the process?:")
if Start==("yes"):
    print("Welcome!Please insert your card")
    Ins=input("Card ditected:")
    if Ins==("yes"):
        print("Hi,Plese do not remove your card,leave your card inserted during the entire transaction")
        language=input("Enter the language engilsh, hindi:")
        if language==("english"):
            print("Enter the 4 digit the pin")
            Pin=int(input("Enter the Pin:"))
            if Pin==9561:
                print("Select the type of transaction")
                Tran=input("enter type of transaction 1. cash withdrawal 2. balance enquary:")
                if Tran==("cash withdrawal"):
                    print("Select type of account")
                    Type=input("Enter type of account:")
                    if Type==("current account")or("saving account"):
                        print("Enter the withdrawal amount")
                        Amount=int(input("Enter the amount:"))
                        if Amount<=2000:
                            print("Collect your cash")
                            Num=input("Did you colleced your cash?:")
                            if Num==("yes"):
                                print("Take a printed receipt, if needed")
                            else:
                                print("No,i dident collected my cash")
                        else:
                            print("Not sufficient balance")
                    else:
                        print("this type is not detected")
                else:
                    print("this transaction was not detected")
            else:
                print("Wrong pin")   
        elif language ==("hindi"):
            print("4 digit ka pin enter karo")
            Pin=int(input("Enter the pin:"))
            if Pin==9561:
                print("Transaction ka type chune")
                Tran=input("transaction ka type chune:")
                if Tran==("cash withdrawal"):
                    print("Account ka type chune")
                    Type=input("Account ka type enter kare:")
                    if Type==("current account"):
                        print("withdrawal amount dale")
                        Amount=int(input("amount dale:"))
                        if Amount<=2000:
                            print("Cash jama kar le")
                            Num=input("Aapne cash jama kr liya?:")
                            if Num==("yes"):
                                print("agar jarurat ho to receipt jama kr le")
                            else:
                                print("abhi cash jama nahi hue")
                        else:
                            print("itne cash uplabdh nahi he")
                    else:
                        print("ye type nahi mila")
                else:
                    print("ye transaction nahi mila")
            else:
                print("Pin galat hai")
        else:
            print("ye language ulabd nahi he")
    else:
        print("Sorry,aapka card ditect nahi hua")
else:
    print("Galat")
