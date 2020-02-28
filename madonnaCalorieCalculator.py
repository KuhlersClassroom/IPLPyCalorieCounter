print("Net Income Calculator")

totalFat = float(input("Enter Amount of Fats: "))
totalProteins = float(input("Enter Amount of Proteins: "))
totalCarbs = float(input("Enter Amount of Carbohydrates: "))

GRAM_FAT = 9
GRAM_PROTEIN = 4
GRAM_CARB = 4

fatCalories = totalFat * GRAM_FAT
print("Total Calories From Fats: " + str(fatCalories))

proteinCalories = totalProteins * GRAM_PROTEIN
print("Total Calories From Proteins: " + str(proteinCalories))

carbsCalories = totalCarbs * GRAM_CARB
print("Total Calories From Carbs: " + str(carbsCalories))

totalCalories = carbsCalories + proteinCalories + fatCalories
print("Total Amount of Calories: " + str(totalCalories))

