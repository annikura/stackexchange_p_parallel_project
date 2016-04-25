import sys
from file_parser import do_smth_with_that_file
from filter import filter_data

lowest_age = 20
highest_age = 42
lowest_score = 20
sys.stderr = sys.stdout

users_data = do_smth_with_that_file('Users.xml')
posts_data = do_smth_with_that_file('Posts.xml')
comments_data = do_smth_with_that_file('Comments.xml')

filtered_users = filter_data(users_data, 'Id',
                             [
                                 'Age'
                             ],
                             [
                                 lambda age: lowest_age <= int(age) <= highest_age
                             ]
                             )
filtered_posts = filter_data(posts_data, 'Id',
                             [
                                 'Score'
                             ],
                             [
                                 lambda score: lowest_score < int(score)
                             ]
                             )
filtered_comments = filter_data(comments_data, '__index',
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
print(len(filtered_comments))