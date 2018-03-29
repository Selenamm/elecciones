peopleList= [{"name":"","age":0,"id": 0,"email":"","typeUser":"", "password":""}]

def menuLogin():
    if len(registred) == 0:
       print("There are no registers")
    else:
        for personas in registred:
            print(personas)
def verificar():       #Metodo para verificar si se encuentra en la lista y que tipo de usuario es.
    id = int(input("ID: "))
    password = (input("Password: "))
    for i in peopleList:
        if i["id"] == id:
            if i["password"] == password:
                if ["typeUser"]== "Administrator":
                    return print("You are logged, you are admninistrator")
                else:
                    return print("You are logged, you are invited")

    print("You are not registrated")

def register(name, age, id, email, typeUser, password):
    newUser = {}
    newUser["name"] = name
    newUser["age"] = age
    newUser["id"] = id
    newUser["email"] = email
    newUser["typeUser"] = typeUser
    newUser["password"] = password
    peopleList.append(newUser)
    print("Successfully Added")
def menuLoginUI():
     print("choose an option \n"
          "1) Login\n"
          "2) Sign in\n")

     option = int(input("Option: "))
     if (option == 1):
        verificar()
        menuLoginUI()
        print("Welcome administrator")
     elif (option == 2):
        name = (input("1) Complete name: "))
        age = int(input("2) Age: "))
        email = (input("3) Email: "))
        id = int(input("4) ID: "))
        password = (input("5) Password:"))
        print("5) Type of user\n"
              "  1) Administrator\n"
              "  2) Invited")
        option = int(input("Option: "))
     if (option == 1):
        typeUser= ("Administrator")
        print("You are adminsitrator")
        register(name, age, id, email, typeUser, password)
        menuLoginUI()
     elif(option==2):
        typeUser=("Invited")
        print ("You are invited")
        register(name, age, id, email, typeUser, password)
     else:
         print("5) Type of user\n"
               "  1) Administrator\n"
               "  2) Invited")
         option = int(input("Option: "))
menuLoginUI()

def optionAdmiInvi():
    if (option == 1):
        print("You are an administrator")
    elif (option == 2):
        print("You are an invited")
    else:
        print("Invalid Option")
        optionAdmiInvi()

menuLoginUI()



