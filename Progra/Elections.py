usersList = [{"name":"Dayana","age":"17","id": "1","email":"fsdfsd","typeUser":"Administrator", "password":"1"}] #Listado de usuarios registrados en el sistema
userLogged = {} #Mantiene los datos del usuario autenticado
territorialDistributionList = []
politicalList = []# lista de partidos politicos


#Despliegua la interfaz de registro para los usuarios nuevos
def registerUI():
    print("\nUser register")
    name = (input("1) Complete name: "))
    age = (input(str("2) Age: ")))
    email = (input("3) Email: "))
    id = (input(str("4) ID: ")))
    password = (input(str("5) Password:")))

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
    option = (input(str("Option: ")))

    if (option == "1"):
        return "Administrator"
        menuLoginUI()
    elif option == "2":
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
    print("\nLog in")
    id = (input(str("ID: ")))
    password = (input(str("Password: ")))
    loginUser(id,password)

#Logea al usuario en el sistema
def loginUser(id,password):
    for i in usersList:
        if i["id"] == id:
            if i["password"] == password:
                redirectUserAutenticate(i)
            else:
                print("Wrong Credentials")

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
        print("        Welcome to the national election system!  \n    ")
        print("Do you already have an account? log in. If not register.")
        option = (input(str("Choose an option to perform \n"
                            "1) Login\n"
                            "2) Sign in\n"
                            "3) exit\n"
                            "Option: ")))
        if(option == "1"):
            loginUI()
        elif option == "2":
            registerUI()
        elif option == "3":
            run_program = False


#Opciones del Administrador
def administratorOptionsUI():
    print("\n")
    option = (input(str("Welcome to the administrator's menu. What do you want to make? \n"
                       "1) Territorial distribution\n"
                       "2) Administration of political paties\n"
                       "3) Administration of ballots\n"
                       "4) Results\n"
                       "5) Consultation\n"
                       "6) Sing off\n"
                       "Option: ")))
    administratorOptionRediret(option)

#redirige segun la opci]on tomada por el administrador
def administratorOptionRediret(option):
    if (option == "1"):
       territorialDistributionOptions()
    elif (option == "2"):
        politicalPartiesOptions()
    elif (option == "3"):
        typeBallots()
    elif (option == "4"):
        '''# redirigir a resultados'''
    elif (option == "5"):
        '''# redirigir a consultas'''
    elif (option == "6"):
        main()
    else:
        print("Wrong option. Try again.")
        administratorOptionsUI()

# opciones de administracion de distribucipon territorial
def territorialDistributionOptions():
    print("\n")
    option = (input(str("What do you want to manage? \n"
               "1) Manage Province\n"
               "2) Manage Canton\n"
               "3) Manage District\n"
               "4) Back\n"
               "Option: ")))
    territorialDistributionOptionRediret(option)

#redirige segun la opcion de distribuci[on territorial
def territorialDistributionOptionRediret(option):
    if (option == "1"):
        manageProvince()
    elif (option == "2"):
        manageCanton()
    elif (option == "3"):
       manageDistrict()
    elif (option == "4"):
        administratorOptionsUI()
    else:
        territorialDistributionOptions()

# permite modificar,crear o eliminar provincias
def manageProvince():
    print("\n")
    option = (input(str("What do you want to do in provincial administration? \n"
                       "1) Create Province\n"
                       "2) Modify Province\n"
                       "3) Delete Province\n"
                       "4) Back\n"
                       "Option: ")))

    manageProvinceRedirect(option)

#redirije las opciones de crear, modificar y eliminar provivias
def manageProvinceRedirect(option):
    if (option == "1"):
        createProvince()
    elif (option == "2"):
        modifyProvince()
    elif (option == "3"):
        deleteProvince()
    elif (option == "4"):
        territorialDistributionOptions()
    else:
        manageProvince()

# permite crear provincias y agregar los diputados
def createProvince():
    print("\n Enter data to create a province")
    name = (input("1) Province name: "))
    deputyNumber = input(str("2) Deputy number: "))

    newProvince(name,deputyNumber)

    print("Province  created successfully!")
    manageProvince()

#Diccionario de provincia
def newProvince(name,deputyNumber):
    newProvince = {}
    newProvince["name"] = name
    newProvince["deputyNumber"] = deputyNumber

    territorialDistributionList.append(newProvince)

# permite modificar la provincia y numero de diputados
def modifyProvince():
    option = input("\nWhat do you want to change in the province?\n"
                   "1)Name Province\n"
                   "2)Deputy Number\n"
                   "3)Back\n"
                   "Chooose your option: ")
    print("\nProvince created:")
    if option == "1":
        for i in territorialDistributionList:
            name= i["name"]
            print (name)
        option = (input("Name Province: "))

        print("\n")
        for y in territorialDistributionList:
            if y["name"] == option:
                newName = input("New Name: ")
                y["name"] = newName
                print("Name province update succesfully")

    elif option == "2":
        for i in territorialDistributionList:
            name = i["name"]
            deputyNumber = i["deputyNumber"]
            print(name,deputyNumber)
        option = (input(str("Name province: ")))

        print("\n")
        for y in territorialDistributionList:
            if y["name"] == option:
                newNum = (input("New number of Diputies: "))
                y["deputyNumber"] = newNum
                print("Number of deputies update succesfully")


    elif option == "3":
        manageProvince()

    else:
        print("Invalid option, try again")
        modifyProvince()


    manageProvince()

#permite eliminar la provincia deseada
def deleteProvince():
    for i in territorialDistributionList:
        name = i["name"]
        print(name)
    option = (input(str("Name of province you want to delete: ")))

    print("\n")
    for y in territorialDistributionList:
        if (y["name"] == option):
            territorialDistributionList.remove(y)


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
        deleteCanton()
    else:
        territorialDistributionOptions()

#permite crear cantones
def createCanton():
    for i in territorialDistributionList:
        province = i["name"]
        print(province)
    option = input(str("Choose a province:"))

    for x in territorialDistributionList:
        if x["name"] ==option:
            nameCanton = (input(str("Name Canton: ")))
            x["name"] = nameCanton
            print("Name canton add succesfully")
        else:
            print("The province does not exist, try again.")
            addCanton(nameCanton)
        print(nameCanton)
    manageCanton()
def addCanton(nameCanton):
    newCanton={}
    newCanton["nameCanton"]=nameCanton
    territorialDistributionList.append(newCanton)

def modifyCanton():
    option = input("What do you want to change in the province?\n"
                   "1)Name Province\n"
                   "2)Deputy Number\n"
                   "3)Back\n"
                   "Chooose your option: ")

    if option == "1":
        for i in territorialDistributionList:
            name = i["name"]
            print(name)
            option = (input("Name Province: "))

        for y in territorialDistributionList:
            if y["name"] == option:
                newName = input("New Name: ")
                y["name"] = newName
                print("Name province update succesfully")
            else:
                print("The province does not exist, try again.")
                return modifyProvince()

    elif option == "2":
        for i in territorialDistributionList:
            deputyNumber = i["deputyNumber"]
            print(deputyNumber)
            option = (input(str("Number of deputies: ")))

        for y in territorialDistributionList:
            if y["deputyNumber"] == option:
                newNum = (input("New number of Diputies: "))
                y["deputyNumber"] = newNum
                print("Number of deputies update succesfully")

            else:
                print("The number of deputies does not exist, try again.")
                return modifyProvince()

    elif option == "3":
        manageProvince()

    else:
        print("Invalid option, try again")
        modifyProvince()

    manageProvince()

#PErmite eliminar los cantones
def deleteCanton():
    count = 1
    for i in territorialDistributionList:
        print(str(count) + ")" + i.name + "\n")
        count = count + 1
    option = int(input("Choose a Province: "))

    countProvince = 1
    for x in territorialDistributionList:
        if (option == countProvince):
            countProvince += 1

        countCanton = 1
        for y in x.getCantonList:
            print(str(countCanton) + ")" + y.name + "\n")
            countCanton += 1
        optionCanton = int(input("Choose a Canton: "))

        countCanton1 = 1
        for x in y.getCantonList:
            if (option == countCanton1):
                    countProvince += 1

            countCantonDelete = 1
            for z in x.getCantonList():
                if (optionCanton == countCantonDelete):
                    Canton.pop(countCantonDelete - 1)
                countCantonDelete +=1


    print("Canton delete succesfully!")
    manageCanton()


#Permite agregar distritos
def manageDistrict():
    print("\n\n")
    option = int(input("choose an option \n"
                       "1) Create District\n"
                       "2) Modify District\n"
                       "3) Delete District\n"
                       "4) Back\n"
                       "Option: "))

    if (option == 1):
        createDistrict()
    elif (option == 2):
        '''modifyDistrict()'''
    elif (option == 3):
        '''deleteDistrict()'''
    else:
        territorialDistributionOptions()


#Permite crear distritos
def createDistrict():
    count = 1
    for i in territorialDistributionList:
        print(str(count) + ")" + i.name + "\n")
        count +=1
    option = int(input("Choose a Province: "))

    countProvince = 1
    for x in territorialDistributionList:
        if (option == countProvince):
            countProvince += 1

            countCanton = 1
            for y in x.getCantonList():
                print(str(countCanton) + ")" + y.name + "\n")
                countCanton += 1
            optionCanton = int(input("Choose a Canton: "))

            countCanton1 = 1
            for r in y.getCantonList:
                if (option == countCanton1):
                    countCanton1 += 1

                    countDistrict = 1
                    for z in r.DistrictList:
                        if (option == countDistrict):
                            name = (input("1) District name (" + z.name + ") : "))
                            newDistrict = District.District(name)  # crea un objeto del tipo distrito
                            z.addDistrict(newDistrict)  # guarda el objeto en la clase canton

                        countDistrict += 1

    print("District add succesfully")
    manageDistrict()


#opciones de administracion de partidos politicos
def politicalPartiesOptions():
    print("\n\n")
    option = (input(str("choose an option \n"
                       "1) Create political partie\n"
                       "2) Modificate political partie\n"
                       "3) Eliminate political partie\n"
                       "4) Back\n"
                       "Option: ")))
    politicalPartiesOptionRediret(option)

#redirige segun la opcion de partidos politicos
def politicalPartiesOptionRediret(option):
    if (option == "1"):
        addPoliticalPartie()
    elif (option == "2"):
        modifyPoliticalPartie()
    elif (option == "3"):
        deletePoliticalPartie()
    elif (option == "4"):
        administratorOptionsUI()
    else:
        politicalPartiesOptions()

# Anade un nuevo partido politico a la lista
def addPoliticalPartie():
    print("\n")
    namePartie = (input("1) Political name: "))
    foundationYear = int(input("2) Year foundation: "))
    color = (input("3) Colors: "))
    ideologicalCurrent = input("4) Ideological current: ")

    typeBallot = typeBallotsPartieUI()
    #territorialDistributionList.append(typeBallots)

    newPoliticalPartie(namePartie,foundationYear,color,ideologicalCurrent,typeBallot)

    print(typeBallot)
    print("Political partie add succesfully")
    politicalPartiesOptions()


#diccionario de partidos politicos
def newPoliticalPartie(namePartie,foundationYear,color,ideologicalCurrent,typeBallot):
    newPartie = {}
    newPartie["namePartie"] = namePartie
    newPartie["foundationYear"] = foundationYear
    newPartie["color"] = color
    newPartie["ideologicalCurrent"] = ideologicalCurrent
    newPartie["typeBallot"] = typeBallot
    politicalList.append(newPartie)

#permite elegir si el partido es presidencial o legislativo
def typeBallotsPartieUI():
    print("\n")
    print("Type of ballot:\n"
          "  1) Presidential\n"
          "  2) Legilative")
    option = input(str("Option: "))

    if (option == "1"):
        return "Presidential"
    elif option == "2":
        return "legislative"
    else:
        return typeBallotsPartieUI()


#agrega los partidos legislativos a las provincias
'''def addPartieLegislativeProvince():
    count = 1
    for i in territorialDistributionList:
        print(str(count) + ")" + i.name + "\n")
        count = count + 1
        option = int(input("Choose a Province: "))

        countProvince = 1
        for x in territorialDistributionList:
            if (option == countProvince):
                legislative = politicalList
                newLegislativeBallots = Province.Province(legislative)
                territorialDistributionList.append(newLegislativeBallots)

'''

#modifica los partidos registrados
def modifyPoliticalPartie():
    print("\nWhat change do you want to make to the political party?")
    option = input(str("1) Name political partie\n"
                       "2) Foundation year\n"
                       "3) Color\n"
                       "4) Ideological Current\n"
                       "5) Type ballot\n"
                       "6) Back\n"
                       "Choose your option: "))

    if option == "1":
        for i in politicalList:
            partie= i["namePartie"]
            print(partie)
        option = (input(str("Choose a political party: ")))

        for x in politicalList:
                if x["namePartie"] == option:
                    newNamePartie = input(str("New name political partie: "))
                    x["namePartie"] = newNamePartie
        print("Name political partie update succesfully")

    elif option == "2":
        for i in politicalList:
            partie = i["namePartie"]
            foundationYear= i["foundationYear"]
            print(partie,foundationYear)
        option = (input(str("Choose a political party: ")))

        for x in politicalList:
                if x["namePartie"] == option:
                    newYearPartie = input(str("New foundation year political partie: "))
                    x["foundationYear"] = newYearPartie
        print("Foundation year of political party update succesfully")

    elif option == "3":
        for i in politicalList:
            partie = i["namePartie"]
            colors= i["color"]
            print(partie,colors)
        option = (input(str("Choose a political party: ")))

        for x in politicalList:
                if x["namePartie"] == option:
                    newColorPartie = input(str("New color of the political partie: "))
                    x["color"] = newColorPartie
        print("Colors of political party update succesfully")

    elif option == "4":
        for i in politicalList:
            partie = i["namePartie"]
            ideologicalCurrent= i["ideologicalCurrent"]
            print(partie,ideologicalCurrent)
        option = (input(str("Choose a political party: ")))

        for x in politicalList:
                if x["namePartie"] == option:
                    newIdeologicalPartie = input(str("New color of the political partie: "))
                    x["ideologicalCurrent"] = newIdeologicalPartie
        print("Ideological current of political party update succesfully")

    elif option == "5":
        for i in politicalList:
            partie = i["namePartie"]
            ballot = i["typeBallot"]
            print(partie,ballot)
        option = input(str("Choose a political party: "))

        for x in politicalList:
            if i["namePartie"] == option:
                newTypeBallot = typeBallotsPartieUI()
                x["typeBallot"] = newTypeBallot
            print("Type ballot of political party update succesfully")


    politicalPartiesOptions()

#elimina los partidos politicos
def deletePoliticalPartie():
   for i in politicalList:
       namePartie = i["namePartie"]
       print(namePartie)
   option = (input(str("Choose a polotical partie: ")))

   for x in politicalList:
        if (x["namePartie"]==option):
            politicalList.remove(x)

   print("Partie delete succesfully!")
   politicalPartiesOptions()

#permite elegir el tipo de papeleta: presidencial o legistativa
def typeBallots():
    print("\n\n")
    option = int(input("Choose an option \n"
                       "1) Presidential Ballots\n"
                       "2) Legislative Ballots\n"
                       "3) Back\n"
                       "Option: "))

    if (option == 1):
        administrationBallots()
    elif (option == 2):
        administrationBallots()
    else:
        administratorOptionsUI()

#menu que permite crear, modificar o eliminar una papeleta
def administrationBallots():
    print("\n\n")
    option = int(input("Choose an option \n"
                       "1) Create Ballots\n"
                       "2) Modify Ballots\n"
                       "3) Delete Ballots\n"
                       "4) Back\n"
                       "Option: "))


    if (option == 1):
        createBallots()
    elif (option == 2):
        '''modificar papeleta'''
    elif (option == 3):
        '''eliminar papeleta'''
    else:
        typeBallots()





#permite crear papeletas
def createBallots():
    count = 1
    for i in politicalList:
        print(str(count) + ")" + i.name + "\n")
        count = count + 1


    administrationBallots()
def modifyBallots():
    count = 1
    for i in politicalList:
        print(str(count) + ")" + i.name + "\n")
        count = count + 1
    option = int(input("choose a partie: "))

    countModify = 1
    for x in politicalList:
        if (option == countModify):
            typeBallots = (str(count) + ")" + i.name + "\n")

#Permite eliminar las papeletas

def deleteBallots():
    count = 1
    for i in politicalList:
        print(str(count) + ")" + i.name + "\n")
        count = count + 1
    option = int(input("Choose a Ballots: "))

    countDelete = 1
    for x in politicalList:
        if (option == countDelete):
             politicalList.pop(countDelete - 1)
        countDelete += 1

    print("Ballots delete succesfully!")
    administrationBallots()
#Opciones del invitado
def invitedOptionsUI():
    option = int(input("choose an option \n"
                       "1) Consultation\n"
                       "2) Sign off\n"
                       "3) Back\n"
                       "Option: "))


    #inicializa el programa

main()

'''def printUsersList():
    for i in usersList:
        print(i)

printUsersList()

main()
'''




