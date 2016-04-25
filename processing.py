from file_parser import file_content
from filter import filtered_data

lowest_age = 20
highest_age = 42
lowest_score = 20

users_data = file_content('Users.xml')
posts_data = file_content('Posts.xml')
comments_data = file_content('Comments.xml')

filtered_users = filtered_data(users_data, 'Id',
                             [
                                 'Age'
                             ],
                             [
                                 lambda age: lowest_age <= int(age) <= highest_age
                             ]
                             )
filtered_posts = filtered_data(posts_data, 'Id',
                             [
                                 'Score'
                             ],
                             [
                                 lambda score: lowest_score < int(score)
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
