# Welcome to Mukta's fitness camp and Check the BMI
import math
Weight = int(input("Enter the Weight(in kg): "))
Height = float(input("Enter the Height(in cm): "))
Height /= 100
SqurHeight = math.pow(Height,2)
BMI = (Weight / SqurHeight)
if(BMI <= 16.00): print("You are in Severely Underweight Category and BMI is: "+str(BMI))
elif(16.00 < BMI <= 18.40): print("You are in Underweight Category and BMI is: "+str(BMI))
elif(18.50 <= BMI <= 24.90): print("You are in Normal Category and BMI is: "+str(BMI))
elif(25.00 <= BMI <= 29.90): print("You are in Overweight Category and BMI is: "+str(BMI))
elif(30.00 <= BMI <= 34.90): print("You are in Moderately Obese Category and BMI is: "+str(BMI))
elif(35.00 <= BMI <= 39.90): print("You are in Severely Obese Category and BMI is: "+str(BMI))
else: print("You are in Morbidly Obese Category and BMI is: "+str(BMI))


