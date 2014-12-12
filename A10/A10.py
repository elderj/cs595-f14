import feedparser
import docclass

def ManualClassifier(fn, limit):
 wOut = open("rated.txt","w")
 rated = {}
 with open(fn) as entries:
    rated = {}
    doc = entries.readlines()
    for line in doc:
        if len(rated) < limit:
            chunk = str(line).split(" ")
            cur = str(chunk[0])
            print cur, " - ", chunk[1], " - ", len(rated)
            cf = raw_input("Classify this site: ")
            if cf != 'N':
             rated[cur] = cf
             wOut.write(cur)
             wOut.write(" ")
             wOut.write(cf)
             wOut.write("\n")
    print rated
 wOut.close()


def FisherClassifier(fn):
 cl=docclass.classifier(docclass.getwords)
 cl.setdb('A10.db')
 stig = {}


 #get ratings into dictionary to be used later with entries
 with open('rated.txt') as rated:
     rated = rated.readlines()
     for entry in rated:
         entry = str(entry).split(" ")
         key = entry[0]
         val = entry[1].encode('utf-8').strip('\n')
         stig[key]=val

 #get all words for each title
 with open(fn) as entries:
  doc = entries.readlines()
  i = 0
  for line in doc:
    title = line.split(" ")
    a = title[0]
    title.pop(0)
    title.pop(0)
    if a in stig.keys():
     #train classifier using first 50 manually rated entries
     if i < 50:
      titlestr =''
      for word in title:
          word = word + ' '
          titlestr= titlestr + word
      category = stig[a]
      cl.train(titlestr,category)
      i+=1
     else:
      for word in title:
          word = word + ' '
          titlestr = titlestr + word
      print "\n"
      print cl.fprob(titlestr, 'A')
      print "\n"





def ParseTopGearFeed():
 #Parse using feed parser module
 d = feedparser.parse('http://www.topgear.com/uk/videos/rss.xml')
 print len(d['entries'])
 wOut = open("entries.txt","w")
 i = 0
 for entry in d['entries']:
  while i < 150:
   print i, d['entries'][i]['link']
   wOut.write(str(i)) # lazy string string cast but it works
   wOut.write(" ")
   wOut.write(d['entries'][i]['link'])
   wOut.write(" ")
   wOut.write(d['entries'][i]['title'].encode('utf-8')) # more appropriate handling of ascii
   wOut.write('\n')
   print '\n'
   i+=1
 wOut.close()






#formerly two()
def Classify():

 #Manually rate the first 50 entries -> rated.txt
 #ManualClassifier("entries.txt", 100)



 #Use fisher classifier to rate the second 50 entries
 FisherClassifier("entries.txt")


#~~~~Main
#ParseTopGearFeed()
Classify()



def three():
 print "Evaluate Classifications of second 50"