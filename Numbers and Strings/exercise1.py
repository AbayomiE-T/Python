###################################################################
#A function that returns the temperature, t, expressed in degrees 
#fahrenheit as a temperature expressed in degrees celsius.
###################################################################

def f2c(t):

    return ((t-32) * 5)/9

###################################################################
# A function returns the weight of p pounds and o ounces 
# expressed in kilograms
###################################################################

def lboz2kg(p,o):
    
    p2Kg = p * 0.453592
    o2Kg = o * 0.0283495

    kgVal = p2Kg + o2Kg

    return kgVal

###################################################################
# A function that returns a string of the form "author. title. city: publisher, year".
###################################################################
def bibformat_mla(author,title,city,publisher,year):

    return f'{author}. {title}. {city}: {publisher}, {year}'

###################################################################
# A function that returns a string of the form "author (year). title. city: publisher.".
###################################################################
def bibformat_apa(author,title,city,publisher,year):

    return f'{author} ({year}). {title}. {city}: {publisher}'

###################################################################
# A function that prompts the user for their name and prints a short 
# joke in which the user is the butt of the joke.
###################################################################
def joker():
    name = input("What is your name? ")

    return f"Why did {name} go the corner of his hot classroom? Because it was 90 degrees!"

###################################################################
# A function that returns the body-mass-index (BMI) of someone whose 
# weight (in pounds) is w and whose height (in inches) is h.
###################################################################
def bmi(w,h):
    h2m = h * 0.0254
    p2kg = w * 0.453592
    
    return p2kg/(h2m**2)

###################################################################
#This function prompts the user for their appelation, their first name, their last name, their height in inches, their weight in pounds, and prints a message of the form:
# BMI Record for _APPELATION _FIRSTNAME _LASTNAME: 
# Subject is _X feet _Y inches tall and weighs _Z pounds.  
# The subject's BMI is _B.
###################################################################
def bmi_calculator():
    
    appelation = input("what is your title? ")
    firstName = input("What is your first name? ")
    lastName = input("What is your last name? ")
    height = int(input("What is your height in inches? "))
    weight = int(input("What is your weight in pounds? "))
    result = bmi(weight, height)
    
    feet = height // 12
    inches = height % 12

    print("\n")
    print("""BMI Record for %s %s %s:
            Subject is %d feet %d inches tall and weighs %d pounds.
            The subject's BMI is %f.""" %(appelation,firstName,lastName,feet,inches,weight,result))

###################################################################
# A function that takes an integer returns a string consisting of n # characters. 
###################################################################
def hashes(n):

    hash = ''

    for i in range(n):
        hash += '#'
    
    return hash