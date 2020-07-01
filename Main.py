import Return
import ListSplit
import dt
import Borrow

def welcomeToLibrary():
    while(True):
        print("------------------------------------------------------")
        print("        Welcome to the Library Management System      ")
        print("------------------------------------------------------")
        print("Enter 1. To Display")
        print("Enter 2. To Borrow a book")
        print("Enter 3. To return a book")
        print("Enter 4. To exit")
        try:
            choice=int(input("Select a choice from 1-4: "))
            print()
            if(choice==1):
                with open("stock.txt","r") as f:
                    lines=f.read()
                    if(lines == ''):
                        print (" There are no books in the Library ")
                    else:
                        print(lines)
                    print ()
   
            elif(choice==2):
                ListSplit.listSplit()
                Borrow.borrowBook()
            elif(choice==3):
                ListSplit.listSplit()
                Return.returnBook()
            elif(choice==4):
                print("Thank you for using library management system")
                break
            else:
                print("Please enter a valid choice from 1-4")
        except ValueError:
            print("Please input as suggested.")

welcomeToLibrary()
