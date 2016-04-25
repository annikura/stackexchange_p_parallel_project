# A file which contains all the constants


# filtration parameters

min_age = 20
max_age = 42
min_score = 20

# output file parameters

rows_to_show = 50

text = "Here is the result file.\n Below you can find a table, " \
       "which contains a list of first " + str(rows_to_show) + " users from " + \
       str(min_age) + " to " + str(max_age) + " years old, " \
       "who have the biggest amounts of comments to posts " \
       "with score more than " + str(min_score) + '\n' + "To change the number of the " \
       "table rows, change the variable 'rows_to_show' in 'variables.py' file\n" + \
       "To change the age or score filters, change variables 'min_age', " \
       "'max_age' or 'min_score' in the same file\n"

# a link of a site to redirect to. (where the users are situated)

url = 'http://electronics.stackexchange.com/'
