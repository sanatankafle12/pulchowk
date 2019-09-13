dictionary={}
more='yes'
while more!='no':
	name=input("Enter name you want to store: ")	
	age=input("Enter the age of the above person: ")
	dictionary[name]=age
	more=input("Do you want more name?")


name=input('Enter a name:')

if name in dictionary:
	print(dictionary[name])
else:
	print('The name you enter is not in stored')

