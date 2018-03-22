registered = [{"Name Complete":"Dayanna Rojas", "Age":"17","Email":"drojasmiran@gmail.com","Password":"dayanna2018","ID":"208090839" }]

def createAccount(cname,cage,cemail,cpassword,cid):
    newAccount = {}
    newAccount["Name Complete"] = cname
    newAccount["Age"] = cage
    newAccount["Email"] = cemail
    newAccount["Password"] = cpassword
    newAccount["ID"] = cid
    registered.append(newAccount)
    print("\n You are registered")

def accountInformation():
