print("Hey there. This is a program that gives you a rough idea about first admission list in pulchowk college.")

while True:
	faculty=input("Please Enter the branch: ").lower()
	rank=int(input("Please Enter your rank: "))
	if faculty=='computer':
		z=0
		#2076
		for numbers in range(1,270):
			if rank<numbers:
				z+=1
				break
		#2075
		for numbers in range(1,308):
			if rank<numbers:
				z+=1
				break
		#2074
		for numbers in range(1,180):
			if rank<numbers:
				z+=1
				break
		#2073
		for numbers in range(1,196):
			if rank<numbers:
				z+=1
				break
		#2072
		for numbers in range(1,224):
			if rank<numbers:
				z+=1
				break
		#2071
		for numbers in range(1,266):
			if rank<numbers:
				z+=1
				break
		#2070
		for numbers in range(1,520):
			if rank<numbers:
				z+=1
				break
		Chances=z/7*100
		print("There is ",Chances,'%',' chance that you will get admitted in pulchowk in computer engineering')
		break

	elif faculty=='civil':
		z=0
		#2076
		for numbers in range(1,338):
			if rank<numbers:
				z+=1
				break
		#2075
		for numbers in range(1,341):
			if rank<numbers:
				z+=1
				break
		#2074
		for numbers in range(1,282):
			if rank<numbers:
				z+=1
				break
		#2073
		for numbers in range(1,341):
			if rank<numbers:
				z+=1
				break
		#2072
		for numbers in range(1,371):
			if rank<numbers:
				z+=1
				break
		#2071
		for numbers in range(1,377):
			if rank<numbers:
				z+=1
				break
		#2070
		for numbers in range(1,569):
			if rank<numbers:
				z+=1
				break
		Chances=z/7*100
		print("There is ",Chances,'%',' chance that you will get admitted in pulchowk in civil engineering')
		break
	elif faculty=='electrical':
		z=0
		#2076
		for numbers in range(1,563):
			if rank<numbers:
				z+=1
				break
		#2075
		for numbers in range(1,577):
			if rank<numbers:
				z+=1
				break
		#2074
		for numbers in range(1,389):
			if rank<numbers:
				z+=1
				break
		#2073
		for numbers in range(1,402):
			if rank<numbers:
				z+=1
				break
		#2072
		for numbers in range(1,397):
			if rank<numbers:
				z+=1
				break
		#2071
		for numbers in range(1,387):
			if rank<numbers:
				z+=1
				break
		#2070
		for numbers in range(1,755):
			if rank<numbers:
				z+=1
				break
		Chances=z/7*100
		print("There is ",Chances,'%',' chance that you will get admitted in pulchowk in electrical engineering')
		break
	elif faculty=='electronics':
		z=0
		#2076
		for numbers in range(1,427):
			if rank<numbers:
				z+=1
				break
		#2075
		for numbers in range(1,504):
			if rank<numbers:
				z+=1
				break
		#2074
		for numbers in range(1,386):
			if rank<numbers:
				z+=1
				break
		#2073
		for numbers in range(1,361):
			if rank<numbers:
				z+=1
				break
		#2072
		for numbers in range(1,387):
			if rank<numbers:
				z+=1
				break
		#2071
		for numbers in range(1,360):
			if rank<numbers:
				z+=1
				break
		#2070
		for numbers in range(1,354):
			if rank<numbers:
				z+=1
				break
		Chances=z/7*100
		print("There is ",Chances,'%',' chance that you will get admitted in pulchowk in electronics engineering')
		break
	elif faculty=='architect':
		z=0
		#2076
		for numbers in range(1,1194):
			if rank<numbers:
				z+=1
				break
		#2075
		for numbers in range(1,1324):
			if rank<numbers:
				z+=1
				break
		#2074
		for numbers in range(1,1425):
			if rank<numbers:
				z+=1
				break
		#2073
		for numbers in range(1,1587):
			if rank<numbers:
				z+=1
				break
		#2072
		for numbers in range(1,1816):
			if rank<numbers:
				z+=1
				break
		#2071
		for numbers in range(1,1280):
			if rank<numbers:
				z+=1
				break
		#2070
		for numbers in range(1,909):
			if rank<numbers:
				z+=1
				break
		Chances=z/7*100
		print("There is ",Chances,'%',' chance that you will get admitted in pulchowk in architect')
		break
	elif faculty=='mechanical':
		z=0
		#2076
		for numbers in range(1,569):
			if rank<numbers:
				z+=1
				break
		#2075
		for numbers in range(1,474):
			if rank<numbers:
				z+=1
				break
		#2074
		for numbers in range(1,312):
			if rank<numbers:
				z+=1
				break
		#2073
		for numbers in range(1,289):
			if rank<numbers:
				z+=1
				break
		#2072
		for numbers in range(1,380):
			if rank<numbers:
				z+=1
				break
		#2071
		for numbers in range(1,264):
			if rank<numbers:
				z+=1
				break
		#2070
		for numbers in range(1,567):
			if rank<numbers:
				z+=1
				break
		Chances=z/7*100
		print("There is ",Chances,'%',' chance that you will get admitted in pulchowk in mechanical engineering')
		break
	elif faculty=='aerospace':
		z=0
		#2076
		for numbers in range(1,988):
			if rank<numbers:
				z+=1
				break
		#2075
		for numbers in range(1,683):
			if rank<numbers:
				z+=1
				break
		Chances=z/2*100
		print("There is ",Chances,'%',' chance that you will get admitted in pulchowk in aerospace engineering')
		break
	elif faculty=='chemical':
		z=0
		#2076
		for numbers in range(1,3184):
			if rank<numbers:
				z+=1
				break
		
		Chances=z*100
		print("There is ",Chances,'%',' chance that you will get admitted in pulchowk in chemical engineering')
		break
	else:
		print('The branch you have chosen is not available in pulchowk. Please try some other branch or check your spelling.')
		continue


print("NOTE: This is a rough data from past 7 years (i.e from 2070). Every year, the rank keeps on changing so, this isn't a 100% thing. It has been created just to give you a normal idea.")
















