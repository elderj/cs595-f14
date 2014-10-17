
import facebook

token = 'CAACEdEose0cBAGZAlenwN9XXCgiTZAYktqo8JwV4qVM5b8ZAqsTAFeoex6HWAYW8unO1ZAXpcvZBF3LbzSBcF5o5DGgS7KCZCJ5xbZBdB9qZCCUL8FvSJbyH8IDqZCHSnmtaStcqYXPTiKjf03rDS4B7Ln2fACy87WLLeeAAZCVUrzoqU1X3M6HyKothKrkdiF2E5m9pUh9pdVSB0RfR1ueV3B'
graph = facebook.GraphAPI(token)


friends = graph.get_object("me/friends")

print friends['data']


