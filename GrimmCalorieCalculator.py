print ('Calorie Calculator')

gramFat = 9
gramProtein = 4
gramCarbs = 4
totalCalories = 0

numGramsFat = float(input("How many grams of Fat? "))
numGramsProtein = float(input("How many grams of Protein? "))
numGramsCarbs = float(input("How many grams of Carbohydrates? "))

fatCalories = numGramsFat * gramFat
proteinCalories = numGramsProtein * gramProtein
carbsCalories = numGramsCarbs * gramCarbs

totalCalories = fatCalories + proteinCalories + carbsCalories
print ('This item contains ' + str(totalCalories) + ' calories.')
