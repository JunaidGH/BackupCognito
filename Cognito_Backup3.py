import json
import boto3

def lambda_handler(event, context):

    client = boto3.client('cognito-idp')
    UserPool_Id = "eu-west-1_ytbOQ8qVV"
    List_Group_Name = list()
    dicti = {}

    try:
        response = client.list_users(
            UserPoolId=UserPool_Id
        )
    except:
        print ("Error message")

    response = client.list_users(
            UserPoolId=UserPool_Id
            print(UserPoolId)
        )
    print(UserPoolId)
#    i = len(response["Users"])

"""
    while (i>0):
        for user in response["Users"]:
            dicti["Users"] = {}
            dicti["Users"][i] = {}
            dicti["Users"][i]["UserName"]=user["Username"]

            time.sleep(1)
            response2 = client.admin_list_groups_for_user(
                Username=user["Username"],
                UserPoolId=UserPool_Id
            )

            List_Group_Name=list()
            for group in  response2["Groups"]:
                List_Group_Name.append(group["GroupName"])

            dicti["Users"][i]["GroupName"]=List_Group_Name
        i=i-1

    return(dicti)


#if __name__ == "__main__":
#    lambda_handler(event, context)
"""
