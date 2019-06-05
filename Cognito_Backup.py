import boto3

client = boto3.client('cognito-idp')

def user_pool():
    response = client.list_user_pools(
        NextToken="PaginationKeyType",
        MaxResults=20
    )
    #list_users()
    print(response)
    #print(response.keys())
    print(response.values())
    filter_user_pools(response)

def filter_user_pools(response):
#    if response:
#        print("The if is working")
#        return False

#    else:
#        print("Nothing to print")
#        return True

#    listpools = filter(filter_user_pools, response)
#    print(listpools)
#    for x in listpools:
#        print(x)
    listpools = response.list_user_pools.filter(
    Filters=[{'Id': 'eu-west-1_ytbOQ8qVV'}])
    for list in listpools:
        print(list.Id)

    for c in response:
        print(c)
    return

def list_users():
    response = client.list_users(
        UserPoolId='eu-west-1_ytbOQ8qVV',
        AttributesToGet=[
    #         'username',
             'email',
    #         'phone_number',
    #         'name',
    #         'given_name',
    #         'family_name',
    #         'perferred_username',
             'sub'
        ],
        Limit=60
        )
    print(response)


if __name__ == "__main__":
    user_pool()
    #list_users()
