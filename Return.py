
import ListSplit
import dt
def returnBook():
    name=input("Enter name of borrower: ")
    a="Borrow-"+name+".txt"
    try:
        with open(a,"r") as f:
            lines=f.readlines()
            lines=[a.strip("$") for a in lines]
    
        with open(a,"r") as f:
            data=f.read()
            print("\t\tCurrent Book Holdings\t\t\t")
            print(data)
    except:
        print("The borrower "+name+" does not exist in System Currently")
        returnBook()

    b="Return-"+name+".txt"
    with open(b,"w+")as f:
        f.write("                Library Management System \n")
        f.write("                   Returned By: "+ name+"\n")
        f.write("    Date: " + dt.getDate()+"    Time:"+ dt.getTime()+"\n\n")
        f.write("S.N.\t\tBookname\t\n")
       

    for i in range(3):
        if ListSplit.bookname[i] in data:
            with open(b,"a") as f:
                f.write(str(i+1)+"\t\t"+ListSplit.bookname[i]+"\t\n")
                #ListSplit.quantity[i]=int(ListSplit.quantity[i])+1
         
    bookReturn=input(" Enter book Name you want to Return : ") 
    if bookReturn in data:

        with open("Stock.txt","w+") as f:
            for i in range(3):
                if (bookReturn == ListSplit.bookname[i]) :
                    ListSplit.quantity[i]=int(ListSplit.quantity[i])+1                            
                f.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+"\n")

        with open(a, "r") as f:
            lines = f.readlines()
        with open(a, "w+") as f:
            for line in lines:
                if bookReturn in line.strip("\n") :
                    pass
                else:
                    f.write(line)

    else:
        print("Given Book "+bookReturn+" is not available in the list")