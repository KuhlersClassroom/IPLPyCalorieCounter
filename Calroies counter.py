print ("Calories Counter")

inputfat = float(input("Enter grams of fat:"))
inputprotein = float(input("Enter grams of protein:"))
inputcarbohydrate = float(input("Enter grams of carbohydrates:"))


fat = 9
protein = 4
carbohydrate = 4


cal_fat = inputfat * fat
print("total fat" + str(cal_fat))

cal_protein = inputprotein * protein
print("total protein:" +str(cal_protein))

cal_carbohydrate = inputcarbohydrate * carbohydrate
print("total carbohydrate:" +str(cal_carbohydrate))

      
total = cal_fat + cal_protein + cal_carbohydrate
print("wow look at that total" +str(total))
