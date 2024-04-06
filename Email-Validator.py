Get_email = input (" Enter Email : ")    #p@p.com  , psv@gmail.com
k=0
j=0
d=0


if len(Get_email)>=6:
    
    if Get_email[0].isalpha():
        
        if ("@"in Get_email) and (Get_email.count("@") == 1):
            
            if (Get_email[-4] == ".") ^ (Get_email[-3] == "."):
                
                for i in Get_email:
                    
                    if i == i.isspace():
                        k=1

                    elif i.isalpha():
                        if i == i.upper():
                            j=1

                    elif i.isdigit():
                        continue

                    elif i=="_" or i=="." or i=="@":
                        continue

                    else:
                        d=1
                        
                if k==1 or j==1 or d==1:
                    print("Wrong Email - has space in email or has upper case or has some another signs")

                else:
                    print("Right Email")
            else:
                print("Wrong Email - more than one dot in email")
        else:
            print("Wrong Email - more than one @ in email")
    else:
        print("Wrong Email - First Letter is not a alphabet in email")
else:
    print("Wrong Email - 1")
