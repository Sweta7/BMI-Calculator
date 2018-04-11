# BMI calculator code on python.
name = input('Enter your name: ')
weight = int(input("Enter your weight (kg): "))
height = int(input("Enter you height (cm): "))
bmi = round(weight/(height/100) **2,2)
# output = round(x,2) "to wound the decimal value"
if (bmi>=25 and bmi<=24.99):
          print(name, "your BMI is ",bmi, "and you are overweight")
elif (bmi<18.5):
          print(name, "your BMI is ",bmi, "and your are underweight")
elif (bmi>=18.5 and bmi<=24.99):
          print(name, "your BMI is ",bmi, "and your are normal weight")
else:
          print(name, "your BMI is ",bmi, "and your are obese")
