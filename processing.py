# A file which gets and parses the data from the file, filters it and then outputs into the result.html
# Uses the functions from the other files


import variables
from file_parser import file_content
from filter import filtered_data
from html_file_creator import output
from html_file_creator import link_maker

# file_content gets all the data from the file and pushes it into the list of dicts

users_data = file_content("Users.xml")
posts_data = file_content("Posts.xml")
comments_data = file_content("Comments.xml")

# a filter function returns a set of contents for the field name,
# which goes as a second argument, for those elements of the given
# list which passed all the filters

filtered_users = filtered_data(users_data, "Id",
                               [                # a list of field names to filter
                                   "Age"
                               ],
                               [                # a list of lambdas filtering the field contents
                                   lambda age: variables.lowest_age <= int(age) <= variables.highest_age
                               ]
                               )
filtered_posts = filtered_data(posts_data, "Id",
                               [                # a list of field names to filter
                                   "Score"
                               ],
                               [                # a list of lambdas filtering the field contents
                                   lambda score: variables.lowest_score < int(score)
                               ]
                               )
filtered_comments = filtered_data(comments_data, "__index",
                                  [             # a list of field names to filter
                                      "PostId",
                                      "UserId"
                                  ],
                                  [             # a list of lambdas filtering the field contents
                                      lambda post_id: post_id in filtered_posts,
                                      lambda user_id: user_id in filtered_users
                                  ]
                                  )

# as far as some Ids are absent, __indexes are not equal to Ids
# So let's have a dict() (Id -> __index) to have a fast access to the user if we know his Id

users_id_to_index = dict()

for elem in users_data:
    users_id_to_index[elem["Id"]] = elem["__index"]

# for each comment which passed the filtration
# let's increment the number of appropriate comments for its author
# and get a list of appropriate users indexes at the same time

comments_counter = dict()
users_to_output = []

for index in filtered_comments:
    id_user = users_id_to_index[comments_data[index]["UserId"]]
    if comments_counter.get(id_user) is None:
        comments_counter[id_user] = 0
        users_to_output.append(id_user)
    comments_counter[id_user] += 1
users_to_output.sort(key=lambda i: comments_counter[i], reverse=True)  # sorting from max number of comments to min

output(len(users_to_output),  # a maximum valid number of rows in the table
                              # (if more, lambdas will go out of the list range)
       [        # a list of the column titles of the table
           '#',
           "Id",
           "Link",
           "Num of comments"
       ],
       [        # a list of lambdas which generate the table content
           lambda i: i + 1,
           lambda i: users_data[users_to_output[i]]["Id"],
           lambda i: link_maker(variables.url + "users/" +
                                users_data[users_to_output[i]]["Id"],
                                users_data[users_to_output[i]]["DisplayName"]),
           lambda i: comments_counter[users_to_output[i]]
       ]
       )
