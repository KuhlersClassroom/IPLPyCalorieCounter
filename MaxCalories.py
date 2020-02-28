print ("Calorie Counter")
calorie = float(input("calorie"))

CARBO_H = 4
FAT_T = 9
PROT_E = 4

carboE= calorie * CARBO_H
print (input("carbohydrates are 4 calories" + str (carboE)))
fatT= calorie * FAT_T
print (input("fat is 9 calories" + str (fatT)))
protE= calorie * PROT_E
print (input("protiens are worth 4 calories" + str (protE)))
totalCalories = fatT + carboE + protE
print ("total calories " + str (totalCalories))
print("My total amount of Calories is " + str (totalCalories))
