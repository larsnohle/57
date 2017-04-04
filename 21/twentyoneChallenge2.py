#!/usr/bin/python3
# -*- coding: utf-8 -*-

def get_positive_number_input(msg, to_float = False):
    done = False
    while not done:
        try:
            i = -1.0
            if to_float == True:
                i = float(input(msg))
            else:
                i = int(input(msg))
            if i < 0:
                print("Please enter a number > 0")
            else:
                done = True
        except ValueError:
            print("That was not a valid integer. Please try again!")

    return i

def main():
    month_dict_en = {}
    month_dict_en[1] = "January"
    month_dict_en[2] = "February"
    month_dict_en[3] = "March"
    month_dict_en[4] = "April"
    month_dict_en[5] = "May"
    month_dict_en[6] = "June"
    month_dict_en[7] = "July"
    month_dict_en[8] = "August"
    month_dict_en[9] = "September"
    month_dict_en[10] = "October"
    month_dict_en[11] = "November"
    month_dict_en[12] = "December"

    month_dict_se = {}
    month_dict_se[1] = "Januari"
    month_dict_se[2] = "Februari"
    month_dict_se[3] = "Mars"
    month_dict_se[4] = "April"
    month_dict_se[5] = "Maj"
    month_dict_se[6] = "Juni"
    month_dict_se[7] = "Juli"
    month_dict_se[8] = "Augusti"
    month_dict_se[9] = "September"
    month_dict_se[10] = "Oktober"
    month_dict_se[11] = "November"
    month_dict_se[12] = "December"

    month_dict = month_dict_en
    enter_month_message = "Please enter the number of the month: "
    default_message = "there is no such month!"
    output_message_template = "The name of the month is %s."

    language = input("Please entry language (en/se): ")
    if language.upper() == "SE":
        month_dict = month_dict_se
        enter_month_message = "Var vänlig ange ett månadsnummer: "
        default_message = "Det finns ingen sådan månad!"
        output_message_template = "Månadens namn är %s."

    month_as_number = get_positive_number_input(enter_month_message)
    month_as_string = month_dict.get(month_as_number, default_message)

    string_to_output = output_message_template % month_as_string 

    print(string_to_output)

### MAIN ###

if __name__ == '__main__':
    main()


