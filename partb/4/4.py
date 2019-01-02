import sys
import os
import functools

if(len(sys.argv) != 2):
	print ("Invalid Arguments")
	sys.exit()

if(not(os.path.exists(sys.argv[0]))):
	print ("Invalid File Path")
	sys.exit()

if(sys.argv[1].split('.')[-1] != "txt"):
	print ("Invalid File Format. Only TXT files allowed")
	sys.exit()

escape = open(sys.argv[1])

worddic = { }


for line in escape: 
 myline = line.split()  

 for word in myline: 
  w = worddic.get(word,0) 
  worddic[word] = w + 1
 
print ("\n Result of storing number of occurances of word in dictionary \n", worddic ,"\n ")

sortedlist = [ ]

sortedlist = sorted(worddic.items(), key = lambda Y : Y[1], reverse = True)
print ("\n Sorting in Dscending order of Value Occurance - frequency of word occurance \n", sortedlist)

topten = []

print ("\n Top Ten Occuring Words \n")
for i in range(10): 
		wordTuple = sortedlist[i]
		topten.append(len(wordTuple[0]))
		print ("\n ", wordTuple[0], ", Frequency: " , wordTuple[1] , ", Length " , len(wordTuple[0]))
	except IndexError:
		print ("\n File has less than 10 words")
		break

print ("\n Lengths of 10 most frequently occuring words:")
print (topten)

mysum = functools.reduce(lambda x, y: x + y, topten)
print ("Average length of Top Ten words: " , mysum/len(topten))

squares = [x**2 for x in topten if x%2 != 0]
print ("\n Squres of odd word lengths: ")
print (squares)