import variables
from file_parser import file_content
from filter import filtered_data
from html_file_creator import output
from html_file_creator import link_maker

users_data = file_content('Users.xml')
posts_data = file_content('Posts.xml')
comments_data = file_content('Comments.xml')

filtered_users = filtered_data(users_data, 'Id',
                               [
                                   'Age'
                               ],
                               [
                                   lambda age: variables.lowest_age <= int(age) <= variables.highest_age
                               ]
                               )
filtered_posts = filtered_data(posts_data, 'Id',
                               [
                                   'Score'
                               ],
                               [
                                   lambda score: variables.lowest_score < int(score)
                               ]
                               )
filtered_comments = filtered_data(comments_data, '__index',
                                  [
                                      'PostId',
                                      'UserId'
                                  ],
                                  [
                                      lambda post_id: post_id in filtered_posts,
                                      lambda user_id: user_id in filtered_users
                                  ]
                                  )

users_id_to_index = dict()

for elem in users_data:
    users_id_to_index[elem['Id']] = elem['__index']

comments_counter = dict()
users_to_output = []

for index in filtered_comments:
    id = users_id_to_index[comments_data[index]['UserId']]
    if comments_counter.get(id) is None:
        comments_counter[id] = 0
        users_to_output.append(id)
    comments_counter[id] += 1
users_to_output.sort(key=lambda i: comments_counter[i], reverse=True)

output(
    len(users_to_output),
    [
        '#',
        'Id',
        'Link',
        'Comments'
    ],
    [
        lambda i: i + 1,
        lambda i: users_data[users_to_output[i]]['Id'],
        lambda i: link_maker(variables.url + 'users/' +
                             users_data[users_to_output[i]]['Id'],
                             users_data[users_to_output[i]]['DisplayName']),
        lambda i: comments_counter[users_to_output[i]]
    ]
)
