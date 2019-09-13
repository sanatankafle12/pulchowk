dictionary={
	"sanatan":[23,96,70,81,64],
	"sudip":[84,90,100,59,99],
	"munu":[88,77,99,66,55],
	"toney":[99,50,78,97,56],
	"sujan":[7,67,87,78,99]
}
name=input("Enter the name of the student whose percentage you would like to know: ")
for marks in dictionary[name]:
	if marks<40:
		remark="failed"
		break
	else:
		remark="passed"


total_marks=sum(dictionary[name])
percentage=total_marks/500*100
print("The total marks and percentage obtained by ",name," is",total_marks ," and " ,percentage,"% simultaneously and has ",remark)
