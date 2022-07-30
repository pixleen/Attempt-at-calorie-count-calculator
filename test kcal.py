#Attempt at making a very simplified daily calories calculator


age = int(input("Please enter your age\n"))
weight = float(input("How much do you weigh? Please enter your weight in kilos\n"))
height = float(input("How tall are you? Please enter your height in centimeters\n"))


dailyCalories1 = "2000-2500"
dailyCalories2 = "2500-3000"

if age < 16:
    print("You´re too young to be counting calories! Go out in the sun and play with your friends!")
elif age >= 16 and weight < 100 and height < 190:
    print("Your estimated daily caloric intake equals:", dailyCalories1, "calories")
elif age >= 16 and weight > 100 and height <= 200:
    print("Your estimated daily caloric intake equals:", dailyCalories2, "calories")
else:
    print("Error.\nPlease try again later.")



#I´ve not been able to figure out how to incorporate gender as a factor in my equation.
#In my program I will only count male and female as valid gender options.
#So far this is the line I have played with:
    #gender = str(input("Please enter you gender; either ´xx´ if female or ´xy´if male\n"))

#I have not been able to make it work.
#Any help would be appreciated. 
