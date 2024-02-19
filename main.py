import os
class library: 

    def __init__(self):
        global file
        file=open("books.txt","a+")

    def __del__(self):
        file.close()

    def listBook(self):
        file.seek(0)
        content = file.read().splitlines()
        booklist=content
        if len(booklist)>0:
            print("This is your book list")
            for i in range(len(content)):
                print(content[i])
        elif len(booklist)==0:
            print("Your Book List Empty")
    
    def addBook(self):
       bookTitle= input("Please, Enter Book Title ")
       bookAuthor=  input("Please, Enter Book Author ")
       firstReleaseYear=input("Please, Enter First Release Year ")
       numberofPages=input("Please, Number of Pages ")
       file.seek(0)
       content = file.read().splitlines(" ")
       Exists=False
       for j in range(len(content)):
           if bookTitle==content[j].split(",")[0] and bookAuthor==content[j].split(",")[1]:
                   Exists=True
           elif bookTitle!=content[j].split(",")[0] and bookAuthor!=content[j].split(",")[1]:
            Exists=False
       if Exists==True:
           print("Your Book List Include This Book")
       if Exists==False:
           file.writelines(bookTitle+","+bookAuthor+","+firstReleaseYear+","+numberofPages+"\n")
           print("Your Book is Added Book List")


    def removeBook(self):
        bookName = input("Please, Enter Book Name ")
        file.seek(0)
        content = file.read().splitlines(" ")
        removeList=[]
        if len(content)>=1:
            for i in range(len(content)):          
                if bookName== content[i].split(",")[0]:
                    print(bookName+" is Deleted")
                elif bookName!= content[i].split(",")[0]:
                    removeList.append(content[i])
                if len(content)>=1:
                    file.truncate(0)
            if len(removeList)>0:
                for j in range(len(removeList)):
                    file.write(removeList[j])
            elif len(removeList)==0:
                file.write("")



lib=library()
loginState=False


def login():
    username=input("Please, Enter Username ")
    password=int(input("Please, Enter Password "))
    if username=="User" and password==1234:
        print("Hey! You are in Successfully")
        global loginState
        loginState=True
        menu()
    else:
        print("Attention, Your username or password is wrong")
    
def logout():
    global loginState
    loginState=False


def menu():
        if(loginState==True):
            print("""*** MENU *** \n1)List Books \n2)Add Book \n3)Remove Book \n4)Logout\n""")
            answer=int(input("Please, Select Your Process "))
            if answer == 1:
                lib.listBook()
            elif answer == 2:
                lib.addBook()
            elif answer == 3:
                lib.removeBook()
            elif answer == 4:
                logout()
            else:
                print("Please, Select Process Again")
                menu()
        else:
            print("Please, Login and Try Again")
            login()

while(True):
    menu()

