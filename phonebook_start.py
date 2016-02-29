import os

choice = ""
ContactsFile = "phonebook.txt"
ContactsTempFile = "phonebooktemp.txt"

def PhoneNumberCheck(phone):
    phone_int = False
    while not phone_int:
        for i in phone:
            if i in "-_/\,.#":
                phone = phone.replace(i, "")
        try:
            new_phone = int(phone)
            phone_int = True
        except ValueError or TypeError:
            print("Invalid")
            phone = input("Their phone number: ")
    return phone          
 
def AddContact(name, phone):
    PhoneNumberCheck(phone)
    contacts = open(ContactsFile, "a")
    details = name + ";" + str(phone) + "\n"
    contacts.write(details)
    contacts.close()

def AddMultipleContacts(amount):
    phonebook_array = []
    
    for i in range(amount):
        temp_array = []
        name = input("Name number {}: ".format(i+1))
        phonenumber = PhoneNumberCheck(input("{}'s phone number: ".format(name)))
        temp_array += name, phonenumber
        phonebook_array.append(temp_array)

    contacts = open(ContactsFile, "a")
    
    for row in range(len(phonebook_array)):
            contacts.write(phonebook_array[row][0] + ";" +  phonebook_array[row][1] + "\n")

    contacts.close()

def DeleteContact(DeleteName):
    found = False
    Contacts = open(ContactsFile, "r")
    TempContacts = open(ContactsTempFile, "w")
    for details in Contacts:
        details = details.strip()
        details_array = details.split(";")
        if details_array[0] == DeleteName:
            print(DeleteName, "has been deleted.")
            found = True
        else:
            TempContacts.write(details + "\n")
            
    if not found:
        print("Name not found")
        
    Contacts.close()
    TempContacts.close()

    os.remove(ContactsFile)
    os.rename(ContactsTempFile, ContactsFile)
    
def SearchContact(SearchName):
    contacts = open(ContactsFile, "r")
    found = False
    for details in contacts:
        details = details.strip()
        details = details.split(";")
        
        if details[0] == SearchName:
            phone = details[1]
            print(SearchName,"found. The number is",phone)
            found = True
            break
        
    if not found:
        print("Name not found.")
        
    contacts.close()
    
def Menu():
    print("1)Add")
    print("2)Add multiple")
    print("3)Delete")
    print("4)Search")
    choice = input("Choice: ")
    return choice


if __name__ == "__main__":
    while choice != "q":
        choice = Menu()
        if choice == "1":
            name = input("The name you want added: ")
            phonenumber = PhoneNumberCheck(input("And their phone number: "))
            AddContact(name, phonenumber)
        elif choice == "2":
            amount = int(input("How many contacts would you like to add? "))
            AddMultipleContacts(amount)
        elif choice == "3":
            name = input("The name you want deleted: ")
            DeleteContact(name)
        elif choice == "4":
            name = input("Whose phone number would you like? ")
            SearchContact(name)
