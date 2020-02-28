print("Cal count bc you're fat")

gfat = float(input("Grams of Fat: "))
gprotein = float(input("Grams of Protein: "))
gcarbohydrate = float(input("Grams of Carbohydrates: "))

# Calorie calc

ONEG_FAT = 9 
ONEG_PROTEIN = 4
ONEG_CARBOHYD = 4

fatCal =  gfat * ONEG_FAT
print ("Grams of Fat: " +str(fatCal))

proteinCal = gprotein * ONEG_PROTEIN
print ("Grams of Protein: " + str(proteinCal))

carbohydCal = gcarbohydrate * ONEG_CARBOHYD
print ("Grams of Carbohydrates: " + str(carbohydCal))

totalCal = fatCal + proteinCal + carbohydCal
print ("Total Calories: " + str(totalCal))

