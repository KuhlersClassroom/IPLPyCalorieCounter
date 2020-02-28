print("Calorie Calculator")

totalFatCalories = float(input("Grams of fat eaten: ")) * 9
totalProteinCalories = float(input("Grams of protein eaten: ")) * 4
totalCarbCalories = float(input("Grams of carbs eaten: ")) * 4

totalCal = (totalFatCalories + totalProteinCalories + totalCarbCalories)
print("Your total number of calories eaten is: " + str(totalCal))
