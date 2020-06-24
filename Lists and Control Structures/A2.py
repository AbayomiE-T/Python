###################################################################
# Write a function, zeta1(n), that takes a positive integer, n, and 
# returns the value 1 + 1/2 + 1/3 + 1/4 + ⋯ + 1/n.
###################################################################

def zetal(n):
    sum = 0

    for i in range(1,n+1):
        sum += 1/i

    return sum

###################################################################
# Write a function, product(a), that takes an array, a, of numbers and returns their product: 
# a[0] * a[1] * ⋯ * a[len(a)-1].
###################################################################

def product(a):
    product = 1

    for i in range(0, len(a)):
        product *= a[i]

    return product

###################################################################
# Write a function, average(a), that takes an array, a, of numbers and returns their average:
# (a[0] + a[1] + ⋯ + a[len(a)-1]) / len(a).
###################################################################

def average(a):

    sum = 0

    for i in range(0, len(a)):
        sum += a[i]

    average = sum/len(a)

    return average

###################################################################
# Write a function, to_str(a), that takes an array, a, converts each 
# of its elements to a string (using str(a[i])) and appends all these strings together.
###################################################################

def to_str(a):

    result = ''

    for i in range(0, len(a)):
        result += str(a[i])

    return result

###################################################################
# Write a function, threshold(a,x), that takes an array, a, of numbers 
# and a number, x, and returns an array containing only the values of a 
# that are greater than or equal to x
###################################################################

def threshold(a, x):

    newArray = []

    for i in range(0, len(a)):
        if a[i] >= x:
            newArray.append(a[i])

    return newArray

###################################################################
# Write a function, square(a), that takes an array, a, of numbers and 
# returns an array containing each of the values of a squared.
###################################################################

def square(a):

    aSquared = []

    for i in range(0, len(a)):
        aSquared.append(a[i]**2)

    return aSquared

###################################################################
# Write a function, is_zero(x), that takes a number, x, and returns the string:
# "zero" if x = 0. 
# "not zero" if x ≠ 0
###################################################################

def is_zero(x):

    if x == 0:
        return "Zero"
    else:
        return "Not Zero"

###################################################################
# Write a function, bmi_cat(bmi), that takes a number, bmi, and returns the string:
# "underweight" if bmi < 18.5.
# "normal" if 18.5 ≤ bmi < 25.
# "overweight" if 25 ≤ bmi < 30.
# "obese" if bmi ≥ 30.
###################################################################

def bmi_cat(bmi):

    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    else:
        return "Obese"

###################################################################
# Write a simple command-line application, bmi_app(), that reads a user's 
# height (in inches) and weight (in pounds) and reports their BMI and their BMI category. 
####################################################################

#Helper function
def bmi(w,h):

    p2Kg = w * 0.453592
    inches2Meters = h * 0.0254
    bmi = p2Kg/(inches2Meters**2)

    return bmi

def bmi_app():

    heightInInches = int(input("Enter your height in inches:"))
    weightInPounds = int(input("Enter your weight in pounds:"))

    result = bmi(weightInPounds, heightInInches)
    print("\n")
    print("""Your BMI is %f. You are %s""" %(round(result,2), bmi_cat(result)))

###################################################################
# Write a function, weight_format(mg), that takes an integer, mg, that 
# represents a number milligrams and returns a readable string representation of this number of milligrams. 
# The representation uses the metric units of milligrams (mg), grams (g), kilograms (kg), and tonnes (t) and includes 1 significant decimal place. 
# Some examples:
# weight_format(623) returns "623.0mg"
# weight_format(1500) returns "1.5g"
# weight_format(2732) returns "2.7g"
# weight_format(2732888) returns "2.7kg"
# weight_format(2762888000) returns "2.8t"
####################################################################

def weight_format(mg):
    result = ''

    if mg < 1000:
        result += str(round(float(mg), 1)) + 'mg'
    elif mg >= 1000 and mg < 1000000:
        result += str(round(float(mg/1000), 1)) + 'g'
    elif mg >= 1000000 and mg < 1000000000:
        result += str(round(float(mg/1000000), 1)) + 'kg'
    elif mg >= 1000000000:
        result += str(round(float(mg/1000000000), 1)) + 't'

    return result
