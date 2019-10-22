1.

import os

Wallets = {}
Wallets[("First Wallet")] = input("First number:")
Wallets[("Second Wallet")] = input("Second number:")
Wallets[("Third Wallet")] = input("Third number:")
Wallets[("Fourth Wallet")] = input("Fourth number:")
Wallets[("Fifth Wallet")] = input("Fifth number:")
print(Wallets)

def print_main_window():
    os.system('clear')
    print("\n\n\n")
    print("Choose an option as follows: ")
    print("[1] The fattest wallet has $ value in it")
    print("[2] The skinniest wallet has $ value in it")
    print("[3] All together, these wallets have $ value in them")
    print("[4] All together, the total value of these wallets is worth $ dimes")
    print("[5] EXIT")

def Fattest(Wallets):
    max_value = max(Wallets.values())
    return max_value

def Skinniest(Wallets):
    min_value = min(Wallets.values())
    return min_value

def All_Together(Wallets):
    Add = sum(int(number) for number in Wallets.values())
    return Add

def Dime_value(Wallets):
    Dimes = 10*sum(int(number) for number in Wallets.values())
    return Dimes

while (True):
        print_main_window()
        option = int(input("Your option: "))
        os.system('clear')
        if (option == 1):
            print("The fattest wallet has $", Fattest(Wallets),"value in it")

        elif (option == 2):
            print("The skinniest wallet has $", Skinniest(Wallets), "value in it")

        elif (option == 3):
            print("All together, these wallets have $", All_Together(Wallets), "value in them")

        elif (option == 4):
         print("All together, the total value of these wallets is worth $", Dime_value(Wallets), "dimes")

        else:
            print("Invalid option. ")
            break

        input("\n\nClick Return key to return")


2.
Periodic_Table = {}

class element:
    def __init__(self,symbol,name,atomic_number,row,column):
        self.symbol = symbol
        self.name = name
        self.atomic_number = atomic_number
        self.row = row
        self.column = column

def main_window():
    print("\n\n")
    print("choose option you want:")
    print("1. See all the information that is stored about any element, by entering that element's symbol")
    print("2. Choose a property, and see that property for each element in the table.")
    print("3. Enter a new element")
    print("4. Change the attributes of an element, by entering the element's symbol.")
    print("5.Exit the program")

def checkperiodic_table(element,n):
    if n == 1 or n == 2:
        print("symbol   "+ element.symbol)
    if n == 1 or n == 3:
        print("name   " + element.name)
    if n == 1 or n == 4:
        print("atomic   " + str(element.atomic_number))
    if n == 1 or n == 6:
        print("row   " + str(element.row))
    if n == 1 or n == 7:
        print("column   " + str(element.column))

while (True):
    main_window()
    option = int(input("enter your option\n"))

    if option == 1:
        symbol = input("enter symbol: ")
        checkperiodic_table(Periodic_Table[symbol], 1)
    elif option == 2:
        print("enter property you want to see:\n")
        print("1. view all symbol")
        print("2. view all name")
        print("3. view all atomic_number")
        print("4. view all row")
        print("5. view all column")

        choice = int(input())
        if choice == 1:
            for i in Periodic_Table.keys():
                checkperiodic_table(Periodic_Table[i], 2)
        elif choice == 2:
            for i in Periodic_table.keys():
                checkperiodic_table(Periodic_Table[i], 3)
        elif choice == 3:
            for i in Periodic_table.keys():
                checkperiodic_table(Periodic_Table[i], 4)
        elif choice == 4:
            for i in Periodic_table.keys():
                checkperiodic_table(Periodic_Table[i], 5)
        elif choice == 5:
            for i in Periodic_table.keys():
                checkperiodic_table(Periodic_Table[i], 6)

    elif option == 3:
        symbol = input("enter symbol: ")
        name = input("enter element name: ")
        atomic_number = int(input("enter atomic_number: "))
        row = int(input("enter row number: "))
        column = int(input("enter column number: "))

        if symbol not in Periodic_Table.keys():
            e = element(symbol,name,atomic_number,row,column)
            Periodic_Table[symbol] = e
            print(symbol + "  added\n")
        else:
            print(symbol + "  already in\n")

    elif option == 4:
        symbol = input("enter symbol: ")
        name = input("enter element name: ")
        atomic_number = int(input("enter atomic_number: "))
        row = int(input("enter row number: "))
        column = int(input("enter column number: "))

        e = element(symbol, name, atomic_number, row, column)
        Periodic_Table[symbol] = e

        print(symbol + "  updated\n")

    elif option == 5:

        print("exit")

        break

    input("\n\nClick Return key to return.")




