pass1 = input("Enter the password that you want: ")
pass2 = input("Please enter the same passord to confirm: ")

if pass1 == pass2:
    print("passwords are equal")
else:
    if pass1.casefold() == pass2.casefold():
      print("please check for cases and try again")
    else:
        print("try again")
