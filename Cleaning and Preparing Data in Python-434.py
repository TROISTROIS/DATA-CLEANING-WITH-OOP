## 1. Introducing Data Cleaning ##

# Read the text on the left, and then scroll to the bottom
# to find the instructions for the coding exercise

# Write your answer to the instructions below -- the list of
# lists is stored using the variable name `moma`
num_rows = len(moma)
print(num_rows)

## 2. Reading our MoMA Dataset ##

# import the reader function from the csv module
from csv import reader
opened_file = open("artworks.csv")
read_file= reader(opened_file)
moma=list(read_file)
opened_file.close()
moma = moma[1:]

## 3. Replacing Substrings with the replace Method ##

age1 = "I am thirty-one years old"
age2=age1.replace("one", "two")
print(age2)

## 4. Cleaning the Nationality and Gender Columns ##

# Variables you create in previous screens
# are available to you, so you don't need
# to read the CSV again
for row in moma:
    nationality = row[2]
    nationality = nationality.replace("(", "")
    nationality = nationality.replace(")", "")
    row[2] = nationality
    
    gender = row[5]
    gender= gender.replace("(", "")
    gender = gender.replace(")", "")
    row[5] = gender


## 5. String Capitalization ##

for row in moma:
    gender = row[5]
    gender = gender.title()
    if not gender:
        gender = "Gender Unknown/Other"
    row[5] = gender
    
    nationality = row[2]
    nationality = nationality.title()
    if not nationality:
        nationality = "Nationality Unknown"
    row[2] = nationality
    for i in range(5):
        print(row[i])
    

## 6. Errors During Data Cleaning ##

def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date
for row in moma:
    BeginDate = row[3]
    EndDate = row[4]
    BeginDate = clean_and_convert(BeginDate)
    EndDate=clean_and_convert(EndDate)
    row[3]=BeginDate
    row[4]=EndDate

## 7. Parsing Numbers from Complex Strings, Part One ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]
def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char, "")
    return string
stripped_test_data =[]
for test in test_data:
    date = strip_characters(test)
    stripped_test_data.append(date)
print(stripped_test_data)

## 8. Parsing Numbers from Complex Strings, Part Two ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']
def process_date(date):
    if "-" in date:
        new_date = date.split("-")
        date_1 = new_date[0]
        date_2 = new_date[1]
        average = (int(date_1)+ int(date_2))/2
        date = round(average)
    else:
        date = int(date)
    return date
processed_test_data = []
for test in stripped_test_data:
    clean_date = process_date(test)
    processed_test_data.append(clean_date)

for row in moma:
    date = row[6]
    date = strip_characters(date)
    date = process_date(date)
    row[6] = date
    print(row[6])
    
    
            

## 9. Inserting Variables Into Strings ##

template = "{artist}'s birth year is {birth_year}"
ans = template.format(artist = "Pablo Picasso",birth_year = "1881")
print(ans)

## 10. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]
template = "The population of {} is {:,.2f} million"

for country in pop_millions:
    name = country[0]
    pop = country[1]
    output = template.format(name, pop)
    print(output)