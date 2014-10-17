import urllib2

uid = "100000108537035"

query = "SELECT friend_count FROM user WHERE uid = \""+uid
query+= "  \""
print(query)

query = urllib2.quote(query)
print(query)

url = "https://graph.facebook.com/fql?q=" + query
data = urllib2.urlopen(url).read()
fcdata = data.split('{"data":[{"friend_count":')
FriendCount = fcdata[1].split("}]}")
print FriendCount