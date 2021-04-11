weight , height = float (input ("Please enter your weight (kg):")), float (input ("Please enter your height (meters):"))
bmi = weight/height**2       #Body_mass_index
print ("Your body mass index is :" + str (bmi))
if bmi < 18.5 :
    print ( "You are Underweight")
elif 18.5 <= bmi <= 25 :
    print ("You are perfect. Enjoy it")
else:
    print ("You are Overweight")