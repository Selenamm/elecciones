from Progra import PoliticalPartie,Province,Canton#,District


usersList = [{"name":"Dayana","age":17,"id": 123,"email":"fsdfsd","typeUser":"Administrator", "password":"123"}] #Listado de usuarios registrados en el sistema
userLogged = {} #Mantiene los datos del usuario autenticado
territorialDistributionList = []
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
    option = int(input("Choose an option \n"
                       "1) Territorial distribution\n"
                       "2) Administration of political paties\n"
                       "3) Administration of ballots\n"
                       "4) Results\n"
                       "5) Consultation\n"
                       "6) Sing off\n"
                       "Option: "))
    administratorOptionRediret(option)

#redirige segun la opci]on tomada por el administrador
def administratorOptionRediret(option):
    if (option == 1):
       territorialDistributionOptions()
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
# opciones de administracion de distribucipon territorial
def territorialDistributionOptions():
    print("\n\n")
    option = int(input("choose an option \n"
               "1) Manage Province\n"
               "2) Manage Canton\n"
               "3) Manage District\n"
               "4) Back\n"
               "Option: "))
    territorialDistributionOptionRediret(option)

#redirige segun la opcion de distribuci[on territorial
def territorialDistributionOptionRediret(option):
    if (option == 1):
        manageProvince()
    elif (option == 2):
        manageCanton()
    elif (option == 3):
       ''' manageDistrict()'''
    else:
        administratorOptionsUI()

# permite modificar,crear o eliminar provincias
def manageProvince():
    print("\n\n")
    option = int(input("choose an option \n"
                       "1) Create Province\n"
                       "2) Modify Province\n"
                       "3) Delete Province\n"
                       "4) Back\n"
                       "Option: "))

    if (option == 1):
        createProvince()
    elif (option == 2):
        modifyProvince()
    elif (option == 3):
        deleteProvince()
    else:
        territorialDistributionOptions()

# permite crear provincias y agregar los diputados
def createProvince():
    print("\n")
    name = (input("1) Province name: "))
    deputyNumber = int(input("2) Deputy number: "))

    newProvince = Province.Province(name, deputyNumber)
    territorialDistributionList.append(newProvince)

    print("Province add succesfully")
    manageProvince()

# permite modificar la provincia y numero de diputados
def modifyProvince():
    count = 1
    for i in territorialDistributionList:
        print(str(count) + ")" + i.name + "\n")
        count = count + 1
    option = int(input("Choose a Province: "))

    countModify = 1
    for x in territorialDistributionList:
        if (option == countModify):
            name = (input("1) Province name (" + x.name + ") : "))
            deputyNumber = int(input("2) Deputy number(" + str(x.deputyNumber) + ")): "))

            x.name = name
            x.deputyNumber = deputyNumber

        countModify += 1
    print("Province update succesfully")
    manageProvince()

#permite eliminar la provincia deseada
def deleteProvince():
    count = 1
    for i in territorialDistributionList:
        print(str(count) + ")" + i.name + "\n")
        count = count + 1
    option = int(input("Choose a Province: "))

    countDelete = 1
    for x in territorialDistributionList:
        if (option == countDelete):
            territorialDistributionList.pop(countDelete - 1)
        countDelete += 1

    print("Province delete succesfully!")
    manageProvince()

# permite administrar cantones
def manageCanton():
    print("\n\n")
    option = int(input("choose an option \n"
                       "1) Create Canton\n"
                       "2) Modify Canton\n"
                       "3) Delete Canton\n"
                       "4) Back\n"
                       "Option: "))

    if (option == 1):
        createCanton()
    elif (option == 2):
        modifyCanton()
    elif (option == 3):
        '''deleteCanton()'''
    else:
        territorialDistributionOptions()


def createCanton():
    count = 1
    for i in territorialDistributionList:
        print(str(count) + ")" + i.name + "\n")
        count = count + 1
    option = int(input("Choose a Province: "))

    countModify = 1
    for x in territorialDistributionList:
        if (option == countModify):
            name = (input("1) Canton name (" + x.name + ") : "))
            newCanton = Canton.Canton(name)     #crea un objeto del tipo canton
            x.addCanton(newCanton)         #guarda el objeto en la clase provincia

        countModify += 1

    print("Canton add succesfully")
    manageCanton()


def modifyCanton():
    count = 1
    for i in territorialDistributionList:
        print(str(count) + ")" + i.name + "\n")
        count = count + 1
    option = int(input("Choose a Province: "))

    countProvince = 1
    for x in territorialDistributionList:
        if (option == countProvince):

            countCanton = 1
            for y in x.getCantonList():
                print(str(countCanton) + ")" + y.name + "\n")
                countCanton += 1
            optionCanton = int(input("Choose a Canton: "))

            countCantonModify = 1
            for z in x.getCantonList():
                if(optionCanton == countCantonModify):
                    name = input("Canton name("+z.name+"): ")
                countCantonModify += 1

        countProvince += 1


    print("Canton update succesfully")
    manageCanton()

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


