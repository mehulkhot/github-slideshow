hour = input("Enter hour ")


try :
	hour = float(hour)
except : 
	print("eRRO")
	quit()
	
rate = input("Enter rate ")
try :
	rate = float(rate)
except : 
	print("eRRO")	
	quit()
	
if float(hour) > 40 :
	pay = float(hour) * float(rate)*1.5
else :
	pay = float(hour) * float(rate)
print("Pay: ", pay)
