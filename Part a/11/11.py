import re
def reverse(string): 
    string = "".join(reversed(string)) 
    return string 
l1=["No1","Iam2", "notcolorblind3","myworld4 ","isblackandwhite5","trytokeep6"]
l=["No 1","Iam 2", "notcolorblind 33","myworld 4 ","isblackandwhite 5","trytokeep 6"]
for i in range(len(l)):
	if (i+1)%2 == 0:
		print(l[i])
for i in range(1,len(l)):
	if (i+1)%3==0:
		l[i]=l[i].upper()
		print(l[i])
l2=[reverse(i) for i in l]
print(l2)
newstring=" ".join(l1) 
print(newstring)
print([int(s) for s in newstring.split() if s.isdigit()])

#returns a list for each string

