import re
def reverse(string): 
    string = "".join(reversed(string)) 
    return string 
l1=["No1","Iam2", "notcolorblind3","myworld4 ","isblackandwhite5","trytokeep6"]
l=["No 1","Iam 2", "notcolorblind 33","myworld44 ","isblackandwhite 5","trytokeep 6"]
num=[]
for i in range(len(l)):
	if (i+1)%2 == 0:
		print(l[i])
for i in range(1,len(l)):
	if (i+1)%3==0:
		l[i]=l[i].upper()
		print(l[i])
l2=[reverse(i) for i in l]
print(l2)

newstring=" ".join(l) 
print(newstring)

for i in range(len(newstring)):
 for j in newstring[i].split():
  if(j.isdigit()):
    num.append(j)
print(num)

#returns a list for each string

