print("Calorie Calculator")

gramsoffat = float(input("Enter grams of fat: "))

gramsofprotein = float(input("Enter grams of protein: "))

gramsofcarbohydrates = float(input("Enter grams of carbohydrates: "))

CALORIES_FAT = 9
CALORIES_PROTEIN = 4
CALORIES_CARBOHYDRATES = 4

gramsOfFat = gramsoffat * CALORIES_FAT
print("Grams of fat: " + str(gramsOfFat))

gramsOfProtein = gramsofprotein * CALORIES_PROTEIN
print("Grams of protein: " + str(gramsOfProtein))

gramsOfCarbohydrates = gramsofcarbohydrates * CALORIES_CARBOHYDRATES
print("Grams of carbohydrates: " + str(gramsOfCarbohydrates))

totalCalories = (gramsoffat * CALORIES_FAT) + (gramsofprotein * CALORIES_PROTEIN) + (gramsofcarbohydrates * CALORIES_CARBOHYDRATES)

print("My total calories is: " + str(totalCalories))
