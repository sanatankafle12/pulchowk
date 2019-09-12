print("Hey there. This is a program that gives you a rough idea about first admission list in pulchowk college.")

while True:
	faculty=input("Please Enter the branch: ").lower()
	rank=int(input("Please Enter your rank: "))
	if faculty=='computer':
		z=0
		#2076
		
		if rank<270:
			z+=1
			
		#2075

		if rank<308:
			z+=1
			
		#2074
		
		if rank<180:
			z+=1
				
		#2073

		if rank<196:
			z+=1
				
		#2072
		
		if rank<224:
			z+=1
				
		#2071
		
		if rank<266:
			z+=1
		
		#2070
		
		if rank<520:
			z+=1
		
		Chances=z/7*100
		print("There is ",Chances,'%',' chance that you will get admitted in pulchowk in computer engineering')
		break

	elif faculty=='civil':
		z=0
		#2076
		
		if rank<338:
			z+=1
		
		#2075
		
		if rank<341:
			z+=1
		
		#2074
		
		if rank<282:
			z+=1
		
		#2073
		
		if rank<341:
			z+=1
	
		#2072
		
		if rank<371:
			z+=1
		
		#2071
	
		if rank<377:
			z+=1
				
		#2070
		
		if rank<569:
			z+=1
				
		Chances=z/7*100
		print("There is ",Chances,'%',' chance that you will get admitted in pulchowk in civil engineering')
		break
	elif faculty=='electrical':
		z=0
		#2076
		
		if rank<563:
			z+=1
			
		#2075
		
		if rank<577:
			z+=1
				
		#2074
	
		if rank<389:
			z+=1
			
		#2073
	
		if rank<402:
			z+=1
				
		#2072
		
		if rank<397:
			z+=1
			
		#2071
		
		if rank<387:
			z+=1
			
		#2070
		
		if rank<755:
			z+=1
			
		Chances=z/7*100
		print("There is ",Chances,'%',' chance that you will get admitted in pulchowk in electrical engineering')
		break
	elif faculty=='electronics':
		z=0
		#2076
		
		if rank<427:
			z+=1
				
		#2075
		
		if rank<504:
			z+=1
				
		#2074
	
		if rank<386:
			z+=1
				
		#2073
		if rank<361:
			z+=1
				
		#2072
	
		if rank<387:
			z+=1
				
		#2071
	
		if rank<360:
			z+=1
				
		#2070
	
		if rank<354:
			z+=1
				
		Chances=z/7*100
		print("There is ",Chances,'%',' chance that you will get admitted in pulchowk in electronics engineering')
		break
	elif faculty=='architect':
		z=0
		#2076
		if rank<1194:
			z+=1
			
		#2075
		if rank<1324:
			z+=1
				
		#2074
		if rank<1425:
			z+=1
				
		#2073
		if rank<1587:
			z+=1
				
		#2072
		if rank<1816:
			z+=1
				
		#2071
		
		if rank<1280:
			z+=1
			
		#2070
		
		if rank<909:
			z+=1
				
		Chances=z/7*100
		print("There is ",Chances,'%',' chance that you will get admitted in pulchowk in architect')
		break
	elif faculty=='mechanical':
		z=0
		#2076
		
		if rank<569:
			z+=1
				
		#2075
		if rank<474:
			z+=1
			
		#2074
		if rank<312:
				z+=1
			
		#2073
		if rank<289:
			z+=1
				
		#2072
		if rank<380:
			z+=1
				
		#2071
		if rank<264:
			z+=1
				
		#2070
		if rank<567:
			z+=1
		Chances=z/7*100
		print("There is ",Chances,'%',' chance that you will get admitted in pulchowk in mechanical engineering')
		break
	elif faculty=='aerospace':
		z=0
		#2076
		if rank<988:
			z+=1
				
		#2075
		if rank<683:
			z+=1
				
		Chances=z/2*100
		print("There is ",Chances,'%',' chance that you will get admitted in pulchowk in aerospace engineering')
		break
	elif faculty=='chemical':
		z=0
		#2076
		if rank<3184:
			z+=1
				
		
		Chances=z*100
		print("There is ",Chances,'%',' chance that you will get admitted in pulchowk in chemical engineering')
		break
	else:
		print('The branch you have chosen is not available in pulchowk. Please try some other branch or check your spelling.')
		continue


print("NOTE: This is a rough data from past 7 years (i.e from 2070). Every year, the rank keeps on changing so, this isn't a 100% thing. It has been created just to give you a normal idea.")
















