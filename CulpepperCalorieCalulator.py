print("Calorie Calulator")

FAT = float(input("Enter grams of fat: "))
CARBOHYDRATES = float(input("Enter grams of Carbohydrates: "))
PROTEIN= float(input("Enter grams of Protein: "))







Fatg = 9 * FAT
print("Number of calories from Fat is: " + str(Fatg))

Protieng = 4 * PROTEIN
print("Number of calories from Protein is: " + str(Protieng))

Carbohydratesg = 4 * CARBOHYDRATES 
print("Number of calories from Carbohydrates is: " + str(Carbohydratesg))

totalCalorie = Fatg + Protieng + Carbohydratesg
print("Total number of Calories is:  " + str(totalCalorie))
