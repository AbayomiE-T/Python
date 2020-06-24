import csv

########################################################################################
# Write a function code_to_names(code) that takes an int crime code and returns a list of 
# strings where each string contains the code extension and the full name of the crime.
########################################################################################
def code_to_names(code):
    names = {}

    with open('offense_codes.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)  # skip the first row
        for row in reader:
            if (int(row[0]) == code):
                codeExtension = row[1]
                offenseTypeName = row[3]
                names[codeExtension] = offenseTypeName 
    return names

####################################################################################
# Write a function code_from_keywords(keywords) that an a list of strings and returns 
# a list of all the crime codes that include all the keywords in their description
####################################################################################
def codes_from_keywords(keywords):
    codelist = []
    keywordsLowerCase = [word.lower() for word in keywords]
    20
    with open('offense_codes.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)  # skip the first row
        for row in reader:
            offenseTypeName = row[3]
            offenseTypeName_list_lower = [word.lower() for word in offenseTypeName.split(" ")]
            if len([commonWords for commonWords in offenseTypeName_list_lower if commonWords in keywords]) == len(keywordsLowerCase):
                codelist.append(int(row[0]))
    return codelist

############################################################################################
# Write a function crimes_by_code(code) that returns a list of all the crimes with the given 
# code that have occurred. Each element of the return list is a tuple having he crime id, the 
# abbreviated crime name, the date and time, and neighbourhood id of the crime.
############################################################################################
def crimes_by_code(code):
    crimeList = []

    with open('crime.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        next(reader)  # skip the first row
        for row in reader:
            if code == int(row[2]):
                crimeList.append([row[0],row[4],row[8],row[16]])
    return crimeList 

#########################################################################################
# Write a function crimes_by_code_extension(code, extension) that returns a list of all the 
# crimes with the given code and extension that have occurred.
########################################################################################
def crimes_by_code_extension(code, extension):
    crimes = []
    with open('crime.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        next(reader)  # skip the first row
        for row in reader:
            if code == int(row[2]) and extension == int(row[3]):
                crimes.append([row[0],row[4],row[8],row[16]])
    return crimes
