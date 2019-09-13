dictionary={}
while True:
	name=input("Enter name you want to store: ")	
	age=input("Enter the age of the above person: ")
	if name=='n' or age=='n':
		break
	else:
		dictionary[name]=age
		continue

name=input('Enter a name:')
if name in dictionary:
	print(dictionary[name])
else:
	print('The name you enter is not in stored')

