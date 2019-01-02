mylist=[]
mylist2=[]
def FtoC(far):
    cel=(far-32)*5/9
    mytuple=(far,cel)
    mylist.append(mytuple)
    print("From F to C is: ")
    print(mytuple)

def CtoF(cel):
    far=cel*1.8+32
    mytuple=(cel,far)
    mylist2.append(mytuple)
    print("\nFrom C to F is:\n")
    print(mytuple)

while(1):
    ans=int(input("1.Convert Celsius to Farenheit \n2.Convert Farenheit to Celsius \n3.Display \n4.Exit\n"))
    if(ans==1):
        c=float(input("Enter Celsius temperature: "))
        CtoF(c)
    elif(ans==2):
        f=float(input("Enter Farhenheit temperature: "))
        FtoC(f)
    elif(ans==3):
        print(mylist)
        print(mylist2)
    elif(ans is 4):
        exit(0)
    else:
        print("\nInvalid\n")