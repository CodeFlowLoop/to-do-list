#creating class or list
class list:
    def __init__(self):
        self.s=[]
#adding data to list

    def add(self,item):
        self.s.append(item)
#displaying list

    def display(self):
        
        print("[MY TO DO LIST]")
        print("------------------")
        for index,item in enumerate(self.s,start=1):
            print(f"{index}.{item}")
#removing the item form list

    def remove(self):
        ele_remove=int(input("Enter the remove "))
        if not self.s:
            print("\n No List")
        else:
            self.s.pop(ele_remove-1)
#creating object for class
obj=list()
#created menu to choice
while True:
    print("Enter Your Choice:")
    print()
    print("{1}[   ADD  TO  LIST ]")
    print()
    print("{2}[   REMOVE FORM LIST  ]")
    print()
    print("{3}[   EXIT/DELET  ]")
    print()

    choice=input("ENTER YOUR CHOICE:|:")
#Exiting the function
    if choice=="3":
        print("{ MY TO DO LIST IS DELETED }")
        print("EXITING OR DELETING THE LIST ",end="THANK YOU")
        break

    else:
        #function calling add()
        if choice=="1":
            obj.add(input("ENTER YOUR TEXT/NOTE TO LIST|:|"))
            obj.display()
        #function  call for remove the item
        elif choice=="2":
            
            obj.remove()
            obj.display()

        else:
            print("INVALID CHOICEC")
    