class Contacts:
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email

    def __str__(self):
        return f"{self.name:10}  {self.phone:10}  {self.email:10} "

class ContactManager:
    def __init__(self):
       self.contacts=[]

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"{contact.name} has been added successfully")
    
    def remove_contact(self,name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"{contact.name} has been successfully deleted")
                break
        else:
            print(f"{name} not found")


    def search_contact(self,name):
        for contact in self.contacts:
            if contact.name == name:
                print(f"{'Name':10}  {'Number':10}  {'Email':10}  ")
                print(contact)
                break
        else:
            print( "None" )
    
    def display_contacts(self):
        if self.contacts == []:
            print("No contacts found")
        else:
            print(f"{'Name':10}  {'Number':10}  {'Email':10}  ")
            for contact in self.contacts:
                print(contact)


contact_manager=ContactManager()
while True:
    print("---Contact Manager---")
    print("1- Add Contact")
    print("2- Remove Contact")
    print("3- Search Contact")
    print("4- Display Contact")
    print("5- Exit")
    user_choice=input("Enter your choice")
    if user_choice=='1':
        name=input("Enter the name")
        phone_number=input("Enter the phone number")
        email=input("Enter the email")
        Contact=Contacts(name,phone_number,email)
        contact_manager.add_contact(Contact)

    elif user_choice=='2':
        name=input("Enter the name")
        contact_manager.remove_contact(name)

    elif user_choice=='3':
        name=input("Enter the name")
        contact_manager.search_contact(name)

    elif user_choice=='4':
        contact_manager.display_contacts()
    else:
        break
    user_choice=input("DO you want to try again y/n")
    if user_choice == 'y' or user_choice == 'Y': 
        pass
    else:
        break










