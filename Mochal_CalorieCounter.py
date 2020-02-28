print("Calorie Calculator")

# These are my user input values.
fat = float(input("Enter grams of fat you've consumed."))
protein = float(input("Enter grams of protein you've consumed."))
carbs = float(input("Enter grams of Carbohydrates you've consumed."))

# These are my standard conversion values.
FAT     = 9 # 1 gram of FAT     = 9 calories
PROTEIN = 4 # 1 gram of PROTEIN = 4 calories
CARBS   = 4 # 1 gram of CARBS   = 4 calories

print("----") # To seperate the inputs from outputs.

# These are the converted values.
fatConverted = fat * FAT
print("Fat: " + str(fatConverted) + " calories.")

proteinConverted = protein * PROTEIN
print("Protein: " + str(proteinConverted) + " calories.")

carbsConverted = carbs * CARBS
print("Carbohydrates: " + str(carbsConverted) + " calories.")

print("----") # To seperate the individual values from the total.

# This is my total 
totalCalories = fatConverted + proteinConverted + carbsConverted
print("You've consumed " + str(totalCalories) + " calories so far.")
