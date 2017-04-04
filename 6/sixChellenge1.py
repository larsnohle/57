import datetime

now = datetime.datetime.now()
#print(now.year)
current_year = int(now.year)

age_string = input("What is your current age? ")
retirement_age_string = input("At what age would you like to retire? ")

age = int(age_string)
retirement_age = int(retirement_age_string)

years_to_retirement = retirement_age - age
retirement_year = current_year + years_to_retirement
# if age 

if years_to_retirement > 0:
    output_line_1 = "You have %d years left until you can retire." % years_to_retirement
    output_line_2 = "It's %d, so you can retire in %d." % (current_year, retirement_year)
    print(output_line_1)
    print(output_line_2)
else:
    print("You can already retire!")
