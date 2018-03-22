registred = [{}]#list of registered people
def menuLogin():
    if len(registred) == 0:
       print("There are no registers")
    else:
        for personas in registred:
            print(personas)

def registerPeople(name, age, iD, email, authority):
    register.append(name, age, iD, email, authority)

def menuLoginUI():
    print("choose an option \n"
          "1) Login\n"
          "2) Sign in\n"
          "3) ver lista")
    option = int(input("Option: "))
    if (option == 1):
        iD = int(input("ID: "))
        password = (input("Password: "))

    elif (option == 2):
         name = (input("1) Complete name: "))
         age = int(input("2) Age: "))
         email = (input("3) Email: "))
         ID = int(input("4) ID: "))
         print("5) Type of user\n"
               "  1) Administrator\n"
               "  2) Invited")
         option = int(input("Option: "))
         def optionAdmiInvi():
             if (option == 1):
                 print("You are an administrator")
             elif (option == 2):
                 print("You are an invited")
             else:
                 print("Invalid Option")
             optionAdmiInvi()

    elif (option == 3):
        menuLogin()

    else:
       print("Incorrect option \n"
              "Select another option")
       menuLoginUI()

menuLoginUI()