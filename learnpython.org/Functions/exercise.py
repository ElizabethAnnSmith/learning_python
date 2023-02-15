# Tutorial exercise

# Use an existing function and create own function
# Add a function called list_benefits() that returns these strings - 'More organized code', 'More readablecode', 'Easier code reuse' and 'Allowing programmers to share and connect code together'
# Add function called build_sentence(info) which receives a string argument and returns a sentence starting with the given string and ending with 'is a benefit of functions'


def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

def build_sentence(benefit):
    return "%s is a benefit of functions." % (benefit)

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
