dictionary={}
while True:
	name=input("Enter name you want to store: ")	
	age=input("Enter the age of the above person: ")
	dictionary[name]=age
	more_name=input("Any more name?")
	if more_name=='no':
		break
	else:
		continue

name=input('Enter a name:')
if name in dictionary:
	print(dictionary[name])
else:
	print('The name you enter is not in stored')

