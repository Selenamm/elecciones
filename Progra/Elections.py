from Progra import PoliticalPartie

usersList = [{"name":"Dayana","age":17,"id": 123,"email":"fsdfsd","typeUser":"Administrator", "password":"123"}] #Listado de usuarios registrados en el sistema
userLogged = {} #Mantiene los datos del usuario autenticado
politicalList = []# lista de partidos politicos


#Despliegua la interfaz de registro para los usuarios nuevos
def registerUI():
    print("\n")
    name = (input("1) Complete name: "))
    age = int(input("2) Age: "))
    email = (input("3) Email: "))
    id = int(input("4) ID: "))
    password = (input("5) Password:"))

    #Obtiene el tipo de usuario y lo almacena en una variable local
    typeUser = registerUserTypeUI()

    #Registra al usuario en la lista
    registerUser(name,age,email,id,password,typeUser)


#Interfaz que obtiene y retorna el tipo de usuario que desea registrarse
def registerUserTypeUI():
    print("\n")
    print("Type of user:\n"
          "  1) Administrator\n"
          "  2) Invited")
    option = int(input("Option: "))

    if (option == 1):
        return "Administrator"
        menuLoginUI()
    elif option == 2:
        return "Invited"
    else:
        return "Unknow"


#Almacena los registro en el diccionario
def registerUser(name,age,email,id,password,typeUser):
    newUser = {}
    newUser["name"] = name
    newUser["age"] = age
    newUser["email"] = email
    newUser["id"] = id
    newUser["password"] = password
    newUser["typeUser"] = typeUser
    usersList.append(newUser)

#Interfaz que obtiene el id y contraseña del usuario previamente registrado
def loginUI():
    print("\n")
    id = int(input("ID: "))
    password = str(input("Password: "))
    loginUser(id,password)

#Logea al usuario en el sistema
def loginUser(id,password):
    for i in usersList:
        if i["id"] == id:
            if i["password"] == password:
                redirectUserAutenticate(i)
            else:
                print("Wrong Credentials")
    #print("You are not registrated")

#Redirecciona a un usuario auntenticado al menu
def redirectUserAutenticate(user):
    print("Welcome " + user["name"] + " you are now logged. (" + user["typeUser"] + ")")
    if user["typeUser"] == "Administrator":
        administratorOptionsUI()
    elif user["typeUser"] == "Invited":
        invitedOptionsUI()

#Inicializa todo el programa
def main():

    run_program = True

    while(run_program):
        print("\n\n")
        option = int(input("choose an option \n"
              "1) Login\n"
              "2) Sign in\n"
              "3) exit\n"
              "Option: "))
        if(option == 1):
            loginUI()
        elif option == 2:
            registerUI()
        elif option == 3:
            run_program = False

#Opciones del Administrador
def administratorOptionsUI():
    print("\n\n")
    option = int(input("choose an option \n"
                       "1) Distribución Territorial\n"
                       "2) Administración de partidos políticos\n"
                       "3) Administracion de papeletas\n"
                       "4) Resultados\n"
                       "5) Consultas\n"
                       "6) Cerrar Secion\n"
                       "Option: "))
    administratorOptionRediret(option)

#redirige segun la opci]on tomada por el administrador
def administratorOptionRediret(option):
    if (option == 1):
       ''' #redirigir a distribucion territorial'''
    elif (option == 2):
        politicalPartiesOptions()
    elif (option == 3):
      ''' # redirigir a administracion de papeletas'''
    elif (option == 4):
        '''# redirigir a resultados'''
    elif (option == 5):
        '''# redirigir a consultas'''
    else:
        main()

#opciones de administracion de partidos politicos
def politicalPartiesOptions():
    print("\n\n")
    option = int(input("choose an option \n"
               "1) Crear partido\n"
               "2) Modificar partido\n"
               "3) Eliminar partido\n"
               "4) Back\n"
               "Option: "))
    politicalPartiesOptionRediret(option)

#redirige segun la opcion de partidos politicos
def politicalPartiesOptionRediret(option):
    if (option == 1):
        addPoliticalPartie()
    elif (option == 2):
        modifyPoliticalPartie()
    elif (option == 3):
        deletePoliticalPartie()
    else:
        administratorOptionsUI()

# Anade un nuevo partido politico a la lista
def addPoliticalPartie():
    print("\n")
    name = (input("1) Political name: "))
    foundationYear = int(input("2) Year foundation: "))
    color = (input("3) Colors: "))
    ideologicalCurrent = input("4) Ideological current: ")


    newPoliticalPartie = PoliticalPartie.PoliticalPartie(name,foundationYear,color,ideologicalCurrent)
    politicalList.append(newPoliticalPartie)

    print("Political partie add succesfully")
    politicalPartiesOptions()

#modifica los partidos registrados
def modifyPoliticalPartie():
    count = 1
    for i in politicalList:
        print(str(count) + ")"+ i.name + "\n")
        count = count + 1
    option = int(input("choose a partie: "))

    countModify = 1
    for x in politicalList:
        if (option == countModify):
            name = (input("1) Political name ("+x.name+") : "))
            foundationYear = int(input("2) Year foundation("+str(x.foundationYear)+")): "))
            color = (input("3) Colors("+x.color+"): "))
            ideologicalCurrent = input("4) Ideological current("+x.ideologicalCurrent+"): ")

            x.name = name
            x.foundationYear = foundationYear
            x.color = color
            x.ideologicalCurrent = ideologicalCurrent

        countModify +=1
    print("Political partie update succesfully")
    politicalPartiesOptions()

#elimina los partidos politicos
def deletePoliticalPartie():
    count = 1
    for i in politicalList:
        print(str(count) + ")" + i.name + "\n")
        count = count + 1
    option = int(input("choose a partie: "))

    countDelete = 1
    for x in politicalList:
        if (option == countDelete):
            politicalList.pop( countDelete - 1)
        countDelete += 1

    print("Partie delete succesfully!")
    politicalPartiesOptions()

#Opciones del invitado
def invitedOptionsUI():
    option = int(input("choose an option \n"
               "1) Consultas\n"
               "2) Cerrar Secion"))

    #inicializa el programa
main()


'''def printUsersList():
    for i in usersList:
        print(i)

printUsersList()

main()
'''


