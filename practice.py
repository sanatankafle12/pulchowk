print("Hey there. This is a program that gives you a rough idea about first admission list in pulchowk college.")


faculty=input("Please Enter the branch: ").lower()
rank=int(input("Please Enter your rank: "))
if faculty=='computer':
	lst_rank=[270,308,180,196,224,266,520]
	z=0
	for i in lst_rank:
		if i>rank:
			z+=1
	chances=z/7*100
	print("There is ",chances,'%',' chance that you will get admitted in pulchowk in computer engineering')

elif faculty=='civil':
	lst_rank=[388,341,282,341,371,377,569]
	z=0
	for i in lst_rank:
		if i>rank:
			z+=1
	chances=z/7*100
	
	print("There is ",chances,'%',' chance that you will get admitted in pulchowk in civil engineering')
	
elif faculty=='electrical':
	lst_rank=[563,577,389,402,397,387,755]
	z=0
	for i in lst_rank:
		if i>rank:
			z+=1
	chances=z/7*100
	print("There is ",chances,'%',' chance that you will get admitted in pulchowk in electrical engineering')
	
elif faculty=='electronics':
	lst_rank=[427,504,386,361,387,360,354]
	z=0
	for i in lst_rank:
		if i>rank:
			z+=1
	chances=z/7*100

	print("There is ",chances,'%',' chance that you will get admitted in pulchowk in electronics engineering')
	
elif faculty=='architect':
	lst_rank=[1194,1324,1425,2587,1816,1280,909]
	z=0
	for i in lst_rank:
		if i>rank:
			z+=1
	chances=z/7*100
	
	print("There is ",chances,'%',' chance that you will get admitted in pulchowk in architect')
	
elif faculty=='mechanical':
	lst_rank=[569,474,312,289,380,264,567]
	z=0
	for i in lst_rank:
		if i>rank:
			z+=1
	chances=z/7*100
	print("There is ",chances,'%',' chance that you will get admitted in pulchowk in mechanical engineering')
	
elif faculty=='aerospace':
	lst_rank=[988,683]
	z=0
	for i in lst_rank:
		if i>rank:
			z+=1
			
	Chances=z/2*100
	print("There is ",Chances,'%',' chance that you will get admitted in pulchowk in aerospace engineering')
	
elif faculty=='chemical':
	lst_rank=[3184]
	z=0
	for i in lst_rank:
		if i>rank:
			z+=1
				
	Chances=z*100
	print("There is ",Chances,'%',' chance that you will get admitted in pulchowk in chemical engineering')
	
else:
	print("please be sure that you have chosen correct faculty")

print("NOTE: This is a rough data from past 7 years (i.e from 2070). Every year, the rank keeps on changing so, this isn't a 100% thing. It has been created just to give you a normal idea.")
















