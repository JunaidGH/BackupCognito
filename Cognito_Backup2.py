from warrant import Cognito

u = Cognito('eu-west-1_ytbOQ8qVV','t9v9h86al9hn652emad6t53rt')

user = u.get_users(attr_map={"given_name":"first_name","family_name":"last_name"})
groups = u.get_groups()

group_data = {'GroupName': 'user_group', 'Description': 'description',
            'Precedence': 1}

group_obj = u.get_group_obj(group_data)

print(user)
print(groups)
print(group_obj)
