Inform=input("mame of the hostel informed:")
if  Inform==("cource"):
    print("software engineering diploma")
    Exam=input("to take a exam:")
    if Exam==("algebra paper"):
        print("paper submit")
        Result=input("show result:")
        if Result==("35/40")or("36/40")or("37/40")or("38/40")or("39/40")or("40"):
            print("Pass")
            Interview=input("to take a interview:")
            if Interview ==("1st english interview"):
                print("interviwed in english")
                Result=input("show result:")
                if Result==("pass"):
                    print("pass")or ("fail")
                    Interview=input("2nd interview:")
                    if Interview == ("2nd algebra interview"):
                        print("interviewed in algebra")
                        Result=input("show result:")
                        if Result == ("pass"):
                            print("Pass")
                        Interview =input("3rd interview:")
                        if Interview ==("3rd cultural interview"):
                            print("interviewed in cultural")
                            Result=input("show result:")
                            if Result ==("pass"):
                                print("Pass")
                                Email=input("an email will appear:")
                                if Email==("email arrived"):
                                    print("Email arrived")
                                    Join=input("navgurukul called:")
                                    if Join==("joining"):
                                        print("join the navgurukul")
                                    else:
                                        print("not joining")
                                else:
                                    print("email not arrived")
                            else:
                                print("fail")
                        else:
                            print("not interviewed in cultural")
                    else:
                        print("fail")
                else:
                    print("not interviewed in algebra")
            else:
                print("fail")
        else:
            print("not interview in english")
    else:
        print("fail")
else:
    print("not submit")
    