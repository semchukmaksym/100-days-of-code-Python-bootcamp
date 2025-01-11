def format_name(f_name, l_name):
    '''This function take first name and last name and make it title case'''

    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}"


formated_string = format_name("maksym" , "semchuk")

print(formated_string)
