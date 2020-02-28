print ("claorie calculator")

fat = float(input("how many grams of fat did you eat?"))
protein = float(input("how many grams of protien did you eat?"))
carbs = float(input("how many grams of carbs did you eat?"))

fatVal = 9
proVal = 4
carbVal = 4

fatCal = fat * fatVal
print("Your calories from fat are: "  + str(fatCal) + "cal")

proCal = protein * proVal
print("Your calories from protien are: " + str(proCal) + "cal")

carbCal = carbs * carbVal
print("Your calories from carbs are: " + str(carbCal) + "cal")

totalCal = carbCal + proCal + fatCal
print("Your total calories are: " + str(totalCal) + "cal")
