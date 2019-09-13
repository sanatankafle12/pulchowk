dictionary={
	"sudip": 28,
	"sanatan": 19,
	"munu": 13,
	"toney": 9
}

name=input("Enter your name: ").lower()
if name in dictionary:
	print("The age of ",name," is" ,dictionary[name])
else:
	print("The name you mentioned isn't available. Try again")