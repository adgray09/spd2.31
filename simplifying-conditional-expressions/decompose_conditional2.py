# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

# Blood test analysis program
total_cholostrol = 70
ldl = 30
triglyceride = 120

good_cholesterol = total_cholostrol < 200 and ldl < 100 and triglyceride < 150
high_cholesterol = 200 < total_cholostrol > 240 or ldl > 160 or triglyceride >= 200
moderate_cholesterol = 200 < total_cholostrol < 240 or 130 < ldl < 160 or 150 <= triglyceride < 200

if good_cholesterol:
    # good level
    print('*** Good level of cholestrol ***')
elif high_cholesterol:
    # High cholestrol level
    print('*** High cholestrol level ***')
    print('start taking pills such as statins')
    TLC_diet()
elif moderate_cholesterol:
    #TLC_diet
    print('*** Borderline to moderately elevated ***')
    TLC_diet()
else:
    print('Error: unhandled case.')

def TLC_diet():
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \n \
        should come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol.  \
        For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')
