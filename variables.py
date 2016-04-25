# filtration parameters

lowest_age = 20
highest_age = 42
lowest_score = 20

# show parameters

rows_to_show = 50

text = "Here is the result file.\n Below you can find a table, " \
       "which contains a list of first " + str(rows_to_show) + " users from " + \
       str(lowest_age) + " to " + str(highest_age) + " years old, " \
       "who have the biggest amounts of comments to posts " \
       "with score more than " + str(lowest_score) + '\n'

url = 'http://electronics.stackexchange.com/'
