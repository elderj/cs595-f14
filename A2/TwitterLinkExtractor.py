import re
import requests
import tweepy



#Api and Access keys and secrets + oauth login
ckey = 'Qbo488OM0Z5LuWkNZuNif3yAK'
csecret = 'nu0U0gNDropQ2JwZqW6lIbvs67ZtPbyF1Tw8YH9NOJQmzWu3pA'
atoken = '2818832635-hiYeMiYHB0T6WdfhatyM9VrVrodiECV0UWfuRMM'
asecret = 'AsxI3jHudUt4PxzsUBM3rovI4ygpATxEEHZGTq3168FqM'
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)






def GetFriendStatuses():
   uriCount = 0
   TotalMemCount = 0
   urls = []
   f = open("links.txt", "w")
   user = api.get_user('up5free')
   print "Retreiving friends for", user.screen_name
   for friend in tweepy.Cursor(api.friends).items():
	 print "\n", friend.screen_name

	 twitter = api.user_timeline(screen_name = friend.screen_name , count = 128 , include_rts = False)

	 for tweet in twitter:
	    if uriCount < 1000:
            	for url in re.findall('(http://\S+)', tweet.text):
		       try:
			  test = requests.get(url)
			  if test.status_code == 200:
			     check = urls.count(test.url)
			     if check == 0:
				uriCount = uriCount + 1
				urls.append(test.url)
				memento = "http://mementoweb.org/timemap/link/" + test.url
				mems = requests.get(memento)
				
				memCount = str(mems.text)
				memCount = memCount.count('rel="memento"')
				print  memCount, " mementos found for ", test.url
				if mems.status_code == 200:
				    TotalMemCount = TotalMemCount + 1
				#writing to lines
				fileLines = str(uriCount)
				fileLines += str(": ")
			  	fileLines += str(test.status_code)
			  	fileLines += str(" ")
			  	fileLines += str(url)
			  	fileLines += str(" ")
			  	fileLines += str(test.url)
			  	fileLines += str(" Mementos:")
			  	fileLines += str(memCount)
			  	fileLines += str("\n")
			  	f.write(fileLines)
				
				
				
				
			  	print url, test.status_code,test.url, uriCount
			  	

			  	
			  	
			  	
		       except requests.exceptions.ConnectionError as e:
			  print ""


   print "Unique URLs Found", len(urls)




   print "Links with mementos", TotalMemCount
   print "Out of a total of ", uriCount
   f.close()
   return




print "Tweet Grabber 1.2"
GetFriendStatuses()
