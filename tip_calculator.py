#tip_calculator

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Hi. Welcome to the Bill Spliter!")

total = input("Please enter the total bill amount.\n $")
int_total = int(total)

persons = input("How many people are splitting this bill?\n")
int_persons = int(persons)

tip = input("What percentage of the total bill are you willing to tip? \n*(please enter a no. between 1-100 only)\n")
int_tip = int(tip)

per_head = int_total/int_persons
per_tip = ((per_head)*int_tip/100)
perhead_split= per_head + per_tip

total_round = (round (perhead_split,2))
str_total_round = "{:.2f}".format(total_round)

print(f"Per head split including the tip is {str_total_round} \n Your per head total for bill is {round(per_head,2)}\n And per head tip is {per_tip}")