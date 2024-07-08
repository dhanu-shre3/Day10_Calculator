#function with outputs

def format_name(f_name, l_name):
    """Take first and last name and format it to return the title case version of the name ."""
    #the above is used to document for function.
    #this is called docstring
    formatted_fname = print(f_name.title())
    formatted_lname = print(l_name.title())
    return f"{formatted_fname} {formatted_lname}"


print(format_name("dhanushRee", "somAiah"))