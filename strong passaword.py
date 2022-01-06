alphabate=input("enter the alphabate:")
if alphabate>='a'or alphabate<'z':
    print("this is alphabate")
    characters=input("enter the character:")
    if characters=="@"or characters=="#":
        print("this is character")
        number=input("enter the number:")
        if number>="1":
            print(alphabate + characters+str(number))
        else:
            print("this is not a number")
    else:
        print("this is not character")
else:
    print("this is not a alphabate")