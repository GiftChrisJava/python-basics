#prompt user to ener weight in pounds
weight =  eval(input("Enter weight in pounds : "))

#enter height in inches
heigth = eval(input("Enter height in inches : "))

KILOGRAM_PER_POUND = 0.45359237 #contant
METERS_PER_INCH = 0.0254 #constant

#compute BMI
weightKilograms = weight * KILOGRAM_PER_POUND
heigthMeters = heigth * METERS_PER_INCH
bmi = weightKilograms / (heigthMeters * heigthMeters)

# display result
print("BMI is ", format(bmi, ".2f"))

if bmi < 18.5 :
    print("underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30 :
    print("Overweight")
else : 
    print("Obese")