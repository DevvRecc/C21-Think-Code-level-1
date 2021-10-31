print("▒█░░▒█ █▀▀ █░░ █▀▀ █▀▀█ █▀▄▀█ █▀▀ 　 ▀▀█▀▀ █▀▀█ 　 ▒█▀▀█ █░░█ ▀▀█▀▀ █░░█ █▀▀█ █▀▀▄")
print("▒█▒█▒█ █▀▀ █░░ █░░ █░░█ █░▀░█ █▀▀ 　 ░░█░░ █░░█ 　 ▒█▄▄█ █▄▄█ ░░█░░ █▀▀█ █░░█ █░░█")
print("▒█▄▀▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░░░▀ ▀▀▀ 　 ░░▀░░ ▀▀▀▀ 　 ▒█░░░ ▄▄▄█ ░░▀░░ ▀░░▀ ▀▀▀▀ ▀░░▀")

def menu(): 
    print("[1] Login")
    print("[2] Rate my app!")
    print("[0] Exit the program")

users = {}
status = ""

def newUser():
    createLogin = input("Create login name: ")
 
    if createLogin in users:
        print("\nLogin name already exist!\n")
    else:
        createPassw = input("Enter password: ")
        users[createLogin] = createPassw
        print("\nLogin successful!\n")

def rate():
    print("Hey how do you like my program?")
    rateMe = input("Your Rating: ")
    print("Thanks for your rating!")
        

menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        #hierbij inloggen
        print("Optie 1 is gekozen")
        newUser()
    elif option == 2:
        #optie 2 dingen
        print("Optie 2 is gekozen")
        rate()
        pass
    else:  
        print("Invalid Option.")  

    print()
    menu()
    option = int(input("Enter your option: "))                  

print("Thanks for using my program!")
#einde
