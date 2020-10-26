age = float(input("How old are you? "))

ticket_price = 3
discount = 0.5

if age < 6 or age > 60 :
	print("The ticket is free.")

elif 6 <= age <= 18 :
	print(float(ticket_price * discount))

else :
	print("The ticket price is 3")