# A file which contains all the constants


# filtration parameters

lowest_age = 20
highest_age = 42
lowest_score = 20

# output file parameters

rows_to_show = 50

text = "Here is the result file.\n Below you can find a table, " \
       "which contains a list of first " + str(rows_to_show) + " users from " + \
       str(lowest_age) + " to " + str(highest_age) + " years old, " \
       "who have the biggest amounts of comments to posts " \
       "with score more than " + str(lowest_score) + '\n' + "To change the number of the " \
       "table rows, change the variable 'rows_to_show' in 'variables.py' file\n" + \
       "To change the age or score filters, change variables 'lowest_age', " \
       "'highest_age' or 'lowest_score' in the same file\n"

# a link of a site to redirect to. (where the users are situated)

url = 'http://electronics.stackexchange.com/'
