usersList = [{"name":"Dayana","age":"17","id": "1","email":"fsdfsd","typeUser":"Administrator", "password":"1"}] #Listado de usuarios registrados en el sistema
userLogged = {} #Mantiene los datos del usuario autenticado
territorialDistributionList = []# Lista de distribucion territorial, almacena provinvias, cantones, distritos
politicalList = []# lista de partidos politicos
presidentialList = []# almacena la papelta presidencial

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
        politicalPartyOptions()
    elif (option == "3"):
        administrationBallots()
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
    newProvince = {"nameCanton":[]}
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
    option = (input("Name of province you want to delete: "))

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
    i=0
    while i < len(territorialDistributionList):
        if territorialDistributionList[i]



    for i in territorialDistributionList:
        province = i["name"]
        print(province)
    option = (input("Choose a Province: "))

    for x in territorialDistributionList:
        if x["name"]==option:
            nameCanton = (input("1) Canton name"))
        newCanton(nameCanton)
    print("Canton add succesfully")
    #nameCanton(nameCanton)

    manageCanton()

#diccionario del crear canton
def newCanton(nameCanton):
    newCanton = {}
    newCanton["nameCanton"] = nameCanton
    territorialDistributionList.append(newCanton)

#permite modificar cantones
def modifyCanton():
   for i in territorialDistributionList:
        #print i.name )

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
                    z.name = name
                countCantonModify += 1

        countProvince += 1


    print("Canton update succesfully")
    manageCanton()

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
def politicalPartyOptions():
    print("\n\n")
    option = (input(str("choose an option \n"
                       "1) Create political party\n"
                       "2) Modificate political party\n"
                       "3) Eliminate political party\n"
                       "4) Back\n"
                       "Option: ")))
    politicalPartyOptionRediret(option)

#redirige segun la opcion de partidos politicos
def politicalPartyOptionRediret(option):
    if (option == "1"):
        addPoliticalParty()
    elif (option == "2"):
        modifyPoliticalParty()
    elif (option == "3"):
        deletePoliticalParty()
    elif (option == "4"):
        administratorOptionsUI()
    else:
        politicalPartyOptions()

# Anade un nuevo partido politico a la lista
def addPoliticalParty():
    print("\n")
    nameParty = (input("1) Political name: "))
    foundationYear = int(input("2) Year foundation: "))
    color = (input(str("3) Colors: ")))
    ideologicalCurrent = input(str("4) Ideological current: "))

    newPoliticalParty(nameParty,foundationYear,color,ideologicalCurrent)


    print("Political party add succesfully")
    politicalPartyOptions()


#diccionario de partidos politicos
def newPoliticalParty(nameParty,foundationYear,color,ideologicalCurrent):
    newParty = {}
    newParty["nameParty"] = nameParty
    newParty["foundationYear"] = foundationYear
    newParty["color"] = color
    newParty["ideologicalCurrent"] = ideologicalCurrent
    politicalList.append(newParty)

#modifica los partidos registrados
def modifyPoliticalParty():
    print("\nWhat change do you want to make to the political party?")
    option = input(str("1) Name political party\n"
                       "2) Foundation year\n"
                       "3) Color\n"
                       "4) Ideological Current\n"
                       "5) Back\n"
                       "Choose your option: "))

    if option == "1":
        for i in politicalList:
            party= i["nameParty"]
            print(party)
        option = (input(str("Choose a political party: ")))

        for x in politicalList:
                if x["nameParty"] == option:
                    newNameParty = input(str("New name political party: "))
                    x["nameParty"] = newNameParty
        print("Name political party update succesfully")

    elif option == "2":
        for i in politicalList:
            party = i["nameParty"]
            foundationYear= i["foundationYear"]
            print(party,foundationYear)
        option = (input(str("Choose a political party: ")))

        for x in politicalList:
                if x["nameParty"] == option:
                    newYearParty = input(str("New foundation year political party: "))
                    x["foundationYear"] = newYearParty
        print("Foundation year of political party update succesfully")

    elif option == "3":
        for i in politicalList:
            party = i["nameParty"]
            colors= i["color"]
            print(party,colors)
        option = (input(str("Choose a political party: ")))

        for x in politicalList:
                if x["nameParty"] == option:
                    newColorParty = input(str("New color of the political party: "))
                    x["color"] = newColorParty
        print("Colors of political party update succesfully")

    elif option == "4":
        for i in politicalList:
            party = i["nameParty"]
            ideologicalCurrent= i["ideologicalCurrent"]
            print(party,ideologicalCurrent)
        option = (input(str("Choose a political party: ")))

        for x in politicalList:
                if x["nameParty"] == option:
                    newIdeologicalParty = input(str("New color of the political party: "))
                    x["ideologicalCurrent"] = newIdeologicalParty
        print("Ideological current of political party update succesfully")


    politicalPartyOptions()

#elimina los partidos politicos
def deletePoliticalParty():
   for i in politicalList:
       nameParty = i["nameParty"]
       print(nameParty)
   option = (input(str("Choose a political party: ")))

   for x in politicalList:
        if (x["nameParty"]==option):
            politicalList.remove(x)

   print("Party delete succesfully!")
   politicalPartyOptions()


#menu que permite crear, modificar o eliminar una papeleta
def administrationBallots():
    print("\n\n")
    option =(input(str("Choose an option \n"
                       "1) Create Ballots\n"
                       "2) Modify Ballots\n"
                       "3) Delete Ballots\n"
                       "4) Back\n"
                       "Option: ")))


    if (option == "1"):
        createBallots()
    elif (option == "2"):
        modifyBallots()
    elif (option == "3"):
       '''typeBallots()'''
    elif (option == "4"):
        '''administratorOptionsUI()'''
    else:
        '''administratorOptionsUI()'''
'''
#permite elegir el tipo de papeleta: presidencial o legistativa
def typeBallots():
    print("\n\n")
    option = (input(str("Choose an option \n"
                       "1) Presidential Ballots\n"
                       "2) Legislative Ballots\n"
                       "3) Back\n"
                       "Option: ")))

    if (option == "1"):
        createBallotPresidential()
    #elif (option == "2"):

    else:
        administratorOptionsUI()

'''


#permite crear papeletas
def createBallots():
    for i in politicalList:
        party = i["nameParty"]
        print(party)
    option = input(str("Choose the party which you want to add to the ballot: "))

    for x in politicalList:
        if x["nameParty"]==option:
            nameParty = x["nameParty"]
            print("Type ballot")
            typeBallot = input(str("Presidential or Lesgislative"))
            if typeBallot == "Presidential":
                if typeBallot == "presidential":
                    presidential = typeBallot
                    addBallotPresidential(nameParty,presidential)

                print(nameParty,presidential)

            elif typeBallot == "Legislative":
                if typeBallot == "legislative":
                    nameParty=x["nameParty"]
                    for y in territorialDistributionList:
                        province = y["name"]
                        print(province)
                    option = input(str("Choose a province: "))
                    for n in territorialDistributionList:
                        if n["name"] == option:
                            nameProvince = n["name"]
                            legislative = typeBallot


    administrationBallots()


def addBallotPresidential(nameParty,presidential):
    ballotPresidential = {}
    ballotPresidential["presidential"]=presidential
    ballotPresidential["nameParty"]=nameParty

    presidentialList.append(ballotPresidential)

def addBallotLegislative(nameParty,legislative,nameProvince):
    ballotLegislative = {}
    ballotLegislative["legislative"]= legislative
    ballotLegislative["nameParty"] = nameParty
    ballotLegislative["namePtovince"] = nameProvince
    territorialDistributionList.append(ballotLegislative)

def modifyBallots():
    for i in presidentialList:
        nameParty = ["nameParty"]
        presidential=["presidential"]
        print(nameParty,presidential)
    administrationBallots()

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




