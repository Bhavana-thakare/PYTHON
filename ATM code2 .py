Start=input("Did you started the process?:")
if Start==("yes"):
    print("Welcome!Please insert your card")
    Ins=input("Card ditected:")
    if Ins==("yes"):
        print("Hi,Plese do not remove your card,leave your card inserted during the entire transaction")
        language=input("Select the language:")
        if language==("English")or("hindi")or("marathi"):
            print("Enter the 4 digit ATM pin")
            Pin=int(input("Enter your pin:"))
            if Pin=="9561":
                print("Select the type of transaction")
                Tran=input("enter type of transaction:")
                if Tran==("cash withdrawal")or("Balance enquary"):
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
        else:
            print("Sorry,this language is not available")
    else:
        print("Sorry,your card was not detected")
else:
    print("Error")