#Python Test

#input
n=int(input("Enter the no of iteration:"))
user_list=[]

for i in range(n):
    n_user=int(input("Enter the no of UserName of Tweets:"))
    username=[]
    for j in range(n_user):
        user,id_=input("Enter the username_tweetid[like:sachin tweet_id_1]:").split(" ")
        username.append(user)
    user_list.append(username)

#user with max number of tweets
for lis_ele in user_list:
    dict_user={}
    for user_name in lis_ele:
        if user_name not in dict_user:
            dict_user[user_name]=1
        else:
            dict_user[user_name]=dict_user[user_name]+1
    lam_sort=sorted(dict_user.items(),key=lambda kv :(kv[1],kv[0]),reverse=True)
    #print(lam_sort)
    count=0
    for ln in range(len(lam_sort)-1):
        if lam_sort[count][1]==lam_sort[count+1][1]:
            print("{} {}".format(lam_sort[count][0],lam_sort[count][1]))
            count=count+1
            if (len(lam_sort)-1)==count:
                print("{} {}".format(lam_sort[count][0],lam_sort[count][1]))
        else:
            print("{} {}".format(lam_sort[count][0],lam_sort[count][1]))
            break