
#------------------------------------------------------------------------------------------------------------------------------
from array import *
import re
arr1= array('i')
arr2= array('i')
physicalSize1= 100
sizeofArray1 = 0
filledIndexarray1 = 0
emptyIndexesArray1 = 0
isArray1full= True
isArray1Empty= True
isArray1Created= False
physicalSize2= 100
sizeofArray2 = 0
filledIndexarray2 = 0
emptyIndexesArray2 = 0
isArray2full= True
isArray2Empty= True
isArray2Created= False 

arr1= [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
arr2= [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

def userInput(message):
    choice= input(message)
    if re.findall("[0-9]+",choice):
        return int(choice)
    else:
        print("worng input type")
        print("------------END---------")
        menu()
def menu():
    global arr1, arr2, sizeofArray1 , filledIndexarray1, emptyIndexesArray1 , isArray1full, isArray1Empty, isArray1Created, sizeofArray2, filledIndexarray2, emptyIndexesArray2 , isArray2full, isArray2Empty, isArray2Created 
    print("1. Create array     2. Size\n3. Insert Element     4. Update elemen\n5. Delete array     6. Traverse\n7. Sort    8. End\n")
    userChoice= userInput("Enter your Choice")
    if userChoice == 1:
        choice = userInput("which array t0 create 1 or 2")
        CreateArray(choice)
        print ("-------------------------")
        menu()
    elif userChoice == 2:
        choice = userInput("which array do you want to declare size ")
        print("3")
        declareSizeofArray(choice)
        print ("-------------------------")
        menu()
    elif userChoice == 3:
        choice = userInput("which array do you want to insert ")
        insertElement(choice)
        print ("-------------------------")
        menu()
    elif userChoice == 4:
        update()
        print ("A")
        print ("-------------------------")
        menu()
    elif userChoice == 5:
        delete()
        print ("-------------------------")
        menu()
    elif userChoice == 6:
        if isArray1Created or isArray2Created:
            choice = userInput("which array to work on:")
            if choice ==1:
                if isArray1Created:
                    if not isArray1Empty:
                        traverse(arr1, sizeofArray1, emptyIndexesArray1, filledIndexarray1)
                        print()
                    else:
                        print("no element in Array")
            elif choice == 2:
                if isArray2Created:
                    if not isArray2Empty:
                        traverse(arr2, sizeofArray2, emptyIndexesArray2, filledIndexarray2)
                        print()
                    else:
                        print("no element in Array")
                
            else:
                print ("wrong choice")
        else :
                print ("No Array Created")
        print ("-------------------------")
        menu()
    elif userChoice == 7:
        sort()
        menu()
    elif userChoice == 8:
        print ("Program Ends Here")
        print ("-------------------------")
    else:
        print ("Wrong Input")
        print ("-------------------------")
        menu()

    
def CreateArray(choice):
    if choice ==1:
        global isArray1full, isArray1Empty, isArray1Created
        filledIndexarray1 = 0
        isArray1full= False
        isArray1Empty= True
        isArray1Created= True
        print ("Array 1 Created")
        print ("---------------------------")
    elif choice == 2:
        global isArray2full, isArray2Empty, isArray2Created
        filledIndexarray2 = 0
        isArray2full= False
        isArray2Empty= True
        isArray2Created= True
        print ("Array 2 Created")
        print ("---------------------------")
    else:
        print ("wrong Input")

def declareSizeofArray(choice):
    global isArray1full, filledIndexarray1, emptyIndexesArray1
    if choice ==1:
        if isArray1Created == True:
            choice = userInput("Enter your Choice between 1 to 50")
            if choice > 50 or choice < 1:
                print("worng size")
            else:
                global isArray1full, filledIndexarray1, emptyIndexesArray1, sizeofArray1
                sizeofArray1 = choice
                filledIndexarray1 = 0
                emptyIndexesArray1 = choice
                print(" Declared sizeofArray1")
            
        else:
            print("Array1 not Created")
            print ("---------------------------")
    global isArray2full, filledIndexarray2, emptyIndexesArray2
    if choice ==2:
        if isArray2Created == True:
            choice = userInput("Enter your Choice between 1 to 50")
            if choice > 50 or choice < 1:
                print("worng size")
            else:
                global isArray2full, filledIndexarray2, emptyIndexesArray2, sizeofArray2
                sizeofArray2 = choice
                filledIndexarray2 = 0
                emptyIndexesArray2 = choice
                print(" Declared sizeofArray2")
            
        else:
            print("Array2 not Created")
        print ("---------------------------")


def insertElement(choice):
    global arr1, emptyIndexesArray1, filledIndexarray1, isArray1Empty
    if choice ==1:
        if isArray1Created == True and sizeofArray1 > 0:
            choices = userInput ("how many values do you want to insert?")
            if choices<= emptyIndexesArray1:
                isArray1Empty = False
                insertmenu()
                choice = userInput("enter your choice")
                if choice ==1:
                    if filledIndexarray1>0:
                        for i in range (0, choices):
                            elementAlreadyInserted(choices)
                    else :
                        insertElementAt1stIndex(choices)
                elif choice ==2:
                    insertAtLastIndex(choices)
                    print("data inserted")
                elif choice == 3:
                    choice = userInput("enter element to search")
                    index = linearSearch(arr1, choice, filledIndexarray1)
                    if index == -1:
                        print("element no found")
                    else:
                        choice = userInput("enter 1 to before and 2 to after")
                        if choice ==1:
                            for i in range (0, choices):
                                elementAlreadyInserted(index)
                        elif choice ==2:
                                elementAlreadyInsertedafter(choices)
                            
                        else:
                            print("worg Input")
                elif choice == 4 :
                    i=int(input("at which index"))
                    arr1[i] = userInput("enter value ")
                    print("do")
    elif choice ==2:
        if isArray2Created == True and sizeofArray2 > 0:
            choices = userInput ("how many values do you want to insert?")
            if choices<= emptyIndexesArray2:
                isArray2Empty = False
                insertmenu()
                choice = userInput("enter your choice")
                if choice ==1:
                    if filledIndexarray2>0:
                        for i in range (0, choices):
                            elementAlreadyInserted(choices)
                    else :
                        insertElementAt1stIndex(choices)
                elif choice ==2:
                    insertAtLastIndex(choices)
                    print("data inserted")
                elif choice == 3:
                    choice = userInput("enter element to search")
                    index = linearSearch(arr2, choice, filledIndexarray2)
                    if index == -1:
                        print("element no found")
                    else:
                        choice = userInput("enter 1 to before and 2 to after")
                        if choice ==1:
                            for i in range (0, choices):
                                elementAlreadyInserted(index)
                        elif choice ==2:
                                elementAlreadyInsertedafter(choices)
                            
                        else:
                            print("worg Input")
                elif choice == 4 :
                    i=int(input("at which index"))
                    arr2[i] = userInput("enter value ")
                    print("do")
        
    else:
        print("wrong input")

def insertmenu():
    print ("1. insert at first index\n2. insert at last index\n3. insert before or after  element\n4. insert at particular index\n ........................\n")
    


def insertElementAt1stIndex(choices):
    global arr1 , emptyIndexesArray1, filledIndexarray1, arr2, emptyIndexesArray2, filledIndexarray2
    ch =int(input("which array whose element do you want insert"))
    if ch ==1 :
        for i in range(0, choices):
                        arr1[i]= userInput("Enter value")
                        emptyIndexesArray1 -=1
                        filledIndexarray1 +=1
    elif ch ==2:
        for i in range(0, choices):
                        arr2[i]= userInput("Enter value")
                        emptyIndexesArray2 -=1
                        filledIndexarray2 +=1
def elementAlreadyInserted(choices):
    global arr1, emptyIndexesArray1, filledIndexarray1, arr2, emptyIndexesArray2, filledIndexarray2
    ch= int(input("which array whose element do you want to  insert"))
    if ch ==1:
        for i in range (filledIndexarray1-1, -1, -1):
            arr1[i+1] = arr1[i]
        arr1[0] = userInput(f"enter value at index 0:")
        emptyIndexesArray1-= 1
        filledIndexarray1+= 1
    elif ch ==2:
        for i in range (filledIndexarray1-1, -1, -1):
            arr1[i+1] = arr1[i]
        arr1[0] = userInput(f"enter value at index 0:")
        emptyIndexesArray1-= 1
        filledIndexarray1+= 1
    else:
        print("wrong input")
    
def elementAlreadyInsertedafter(choices):
    global arr1, arr2
    ch= int(input("which array whose element do you want to  insert"))
    if ch ==1:
        arr1[choices] = userInput(f"enter value at index 0:")
    if ch ==2:
        arr2[choices] = userInput(f"enter value at index 0:")



def traverse(arr1, sizeofArray1, emptyIndexesArray1, filledIndexarray1):
    choice=int(input("which array whose element do you want to traverse"))
    if choice == 1:
        print (("size ofArray is ", sizeofArray1))
        print (("filled spaces of Array is ", filledIndexarray1))
        print (("empty spaces of Array is ", sizeofArray1))
        for i in range (0, filledIndexarray1):
            print(f("{arr[i] }"), end=" ")
    if choice == 2:
        print (("size ofArray is", sizeofArray2))
        print (("filled spaces of Array is ", filledIndexarray2))
        print (("empty spaces of Array is ", sizeofArray2))
        for i in range (0, filledIndexarray2):
            print(f("{arr[i] }"), end=" ")
        
def insertAtLastIndex(choices):
    global arr1, emptyIndexesArray1, filledIndexarray1, isArray1Empty
    ch=int(input("which array whose element do you want to insert"))
    
    if ch ==1:
        for i in range(filledIndexarray1, filledIndexarray1+choices):
            arr1[i] = userInput(f"enter value at index 0:")
            emptyIndexesArray1-= 1
            filledIndexarray1+= 1
    elif ch ==2:
        for i in range(filledIndexarray1, filledIndexarray1+choices):
            arr1[i] = userInput(f"enter value at index 0:")
            emptyIndexesArray1-= 1
            filledIndexarray1+= 1
    else :
        print ("wrong input")
def linearSearch(arr, elementToSearch, filledIndexarray):
    choice=int(input("which array do you want to search"))
    if ch == 1:
            for i in range(0, filledIndexarray):
                if arr[i] == elementToSearch:
                    return i
                else:
                    return -1
    if ch == 2:
            for i in range(0, filledIndexarray):
                if arr[i] == elementToSearch:
                    return i
                else:
                    return -1
    



def sort():
    global arr1, arr2, arr
    choice=int(input("which array do you want to sort"))
    arrr = []
    if choice == 1 and isArray1Empty== False:
        while arr1:
            min = arr1[0]
            for x in arr1:
                if x < min:
                    min = x
                    arrr.append(min)
                    arr1.remove(min)
            arr1.append(arrr)
            return arr1
        print("sorted")
    elif choice == 2 and isArray2Empty== False:
        while arr1:
            min = arr2[0]
            for x in arr2:
                if x < min:
                    min = x
                    arrr.append(min)
                    arr2.remove(min)
            arr2.append(arrr)
            return arr2
        print("sorted")
    else:
        print("Array is not created or wrongInput")
def delete():
    choice=int(input("which array do you want to delete"))
    
    if choice ==1 and isArray1Empty== False:
        global arr1, emptyIndexesArray1, filledIndexarray1
        for i in range (0, sizeofArray1):
            arr1[i] = 0
            emptyIndexesArray1-= 1
            filledIndexarray1+= 1
        print("deleted")
    elif choice ==2 and isArray2Empty== False:
        global arr2, emptyIndexesArray2, filledIndexarray2
        for i in range (0, sizeofArray2):
            arr1[i] = 0
            emptyIndexesArray2-= 1
            filledIndexarray2+= 1
        print("deleted")
    else :
        print("Array is not created or wrong input")
        
def update():
    global arr1, arr2
    choice=int(input("which array whose element do you want to update"))
    if choice ==1 and isArray1Empty==False:
        i=int(input("value"))
        arr1[i-1] = userInput("enter value :")
    elif choice ==2 and isArray2Empty== False:
        i=int(input("value"))
        arr2[i-1] = userInput("enter value :")
    else :
        print("array is not created or wrong Input")


#
#********************************************************************************************************************************
#







#
#*************************************************************************************************************************************
#






menu()









    
    






