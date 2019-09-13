dictionary={
	"computer":[270,308,180,196,224,266,520],
	"civil":[388,341,282,341,371,377,569],
	"electronics":[427,504,386,361,387,360,354],
	"electrical":[563,577,389,402,397,387,755],
	"architect":[1194,1324,1425,2587,1816,1280,909],
	"mechanical":[569,474,312,289,380,264,567],
	"aerospace":[988,683],
	"chemical":[3184]
}
faculty_list=['computer','civil','electrical','electronics','architect','mechanical','aerospace','chemical']
faculty=None
while dictionary.get(faculty)==None:
	faculty=input("Enter the faculty you what to know about: ").lower()
	rank=int(input("Enter your rank: "))
	if faculty not in faculty_list:
		print("Please Enter a valid faculty.")
lst_rank=dictionary.get(faculty)
no_of_chances=0
for i in lst_rank:
	if rank<i:
		no_of_chances+=1


percentage=no_of_chances/len(lst_rank)*100
print("You would have gotten admission ",no_of_chances,"times in ",len(lst_rank),"years in ",faculty," engineering. The Probable percentage being ",percentage,"%.")


