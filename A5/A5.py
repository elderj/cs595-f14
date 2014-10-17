import tweepy
import time

#Api and Access keys and secrets + oauth login
ckey = 'Qbo488OM0Z5LuWkNZuNif3yAK'
csecret = 'nu0U0gNDropQ2JwZqW6lIbvs67ZtPbyF1Tw8YH9NOJQmzWu3pA'
atoken = '2818832635-hiYeMiYHB0T6WdfhatyM9VrVrodiECV0UWfuRMM'
asecret = 'AsxI3jHudUt4PxzsUBM3rovI4ygpATxEEHZGTq3168FqM'
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)



def GetFriends():

    f = open("paradox.txt", "w")
    f.write("Freinds for Joseph Elder\n")

    #cursor through all of my friends on twitter
    for myfriend in tweepy.Cursor(api.friends).items():
        screenName = myfriend.screen_name
        print screenName
        ids = []

        #cursor through all pages of friend's friends
        for page in tweepy.Cursor(api.friends_ids, screen_name=screenName).pages():
            ids.extend(page)
            time.sleep(80)# handles rate limiting
        print len(ids),"\n"
        f.write(screenName)
        f.write(" ")
        friendCount = len(ids)
        f.write('%d' % friendCount)
        f.write("\n")
    f.close()






#get friends friends from twitter

GetFriends()
