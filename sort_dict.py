#Python Test
2	
3	#input
4	n=int(input("Enter the no of iteration:"))
5	n_user=int(input("Enter the no of UserName of Tweets:"))
6	user_tweet=[]
7	
8	for i in range(n):
9	    username_tweetid=[]
10	    for j in range(n_user):
11	        username,id_=input("Enter the username_tweetid[like:sachin tweet_id_1]:").split(" ")
12	        username_tweetid.append(username)
13	    user_tweet.append(username_tweetid)
14	
15	#user with max number of tweets
16	for lis_ele in user_tweet:
17	    dict_user={}
18	    for us_tweet in lis_ele:
19	        if us_tweet not in dict_user:
20	            dict_user[us_tweet]=1
21	        else:
22	            dict_user[us_tweet]=dict_user[us_tweet]+1
23	    print(dict_user)
24	    #lam_sort=sorted(dict_user.items(),key=lambda kv :(kv[1],kv[0],reverse=True)
25	    #print(lam_sort)
