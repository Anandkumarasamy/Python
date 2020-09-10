#Python Test

#input
test_case=int(input("Enter the no of test case:"))
user_list=[]

for i in range(test_case):
    number_of_tweets=int(input("Enter the number of tweets:"))
    username=[]
    for j in range(number_of_tweets):
        user,id_=input("Enter the username_tweetid[like:sachin tweet_id_1]:").split(" ")
        username.append(user)
    user_list.append(username)

# max number of tweets
for lis_ele in user_list:
    dict_user={}
    for user_name in list(set(lis_ele)):
        dict_user.setdefault(lis_ele.count(user_name),[]).append(user_name)
    sort_val=sorted(dict_user.items(),key=lambda kv :(kv[0],kv[1]),reverse=True)
    for val in sorted(sort_val[0][1]):
        print("{} {}".format(val,sort_val[0][0]))
'''
Result
Enter the no of test casen:1
Enter the number of tweets:6
Enter the username_tweetid[like:sachin tweet_id_1]:sachin tweet_id_1
Enter the username_tweetid[like:sachin tweet_id_1]:sachin tweet_id_2
Enter the username_tweetid[like:sachin tweet_id_1]:sehwag tweet_id_3
Enter the username_tweetid[like:sachin tweet_id_1]:sehwag tweet_id_4
Enter the username_tweetid[like:sachin tweet_id_1]:kohli tweet_id_5
Enter the username_tweetid[like:sachin tweet_id_1]:kohli tweet_id_6
kohli 2
sachin 2
sehwag 2
'''