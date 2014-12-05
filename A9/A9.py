import re
import urllib2
from bs4 import BeautifulSoup

def gatherBlogs():
    Blogs = []
    i = 0
    while i < 98:
        try:
            response = urllib2.urlopen('http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117')
            blog =response.geturl()  # best practice to close the file
            print "adding ", blog
            Blogs.append(str(blog))
            #html = response.read()
            response.close()  # best practice to close the file
            i +=1

        except urllib2.HTTPError, e:
            print e


    wOut = open("blogs.txt","w")

    wOut.write("http://f-measure.blogspot.com/feeds/posts/default?alt=rss\n")
    wOut.write("http://ws-dl.blogspot.com/feeds/posts/default?alt=rss\n")


    for blog in Blogs:
        blog = blog.split("?")
        blog = blog[0] + "feeds/posts/default?alt=rss"
        wOut.write(blog)
        wOut.write("\n")

    wOut.close()


def getTitles():


    termz = {}
    termsinorder=[]
    wOut = open("blogdata.txt","w")
    with open("blogs.txt") as blogFile:
        lines = blogFile.readlines()
        for line in lines:
           #print line
           response = urllib2.urlopen(line)
           xml = response.read()
           bs = BeautifulSoup(xml)
           #print bs.rss.channel.title
           items = bs.rss.channel.findAll("item")
           for item in items:
               item = str(item).split("</title>")
               item = item[0].split("<title>")
               item = str(item[1])
               item = re.sub('[\"!@#$:.(),\-]', '', item)
               terms = item.split()
               for term in terms:
                   term = str(term).lower()
                   if term in termz:
                       termz[term] += 1
                   else:
                       termz[term] = 1

               #print item ,len(terms),len(termz)


    #Remove Stop Words from counted
    del termz['the']
    del termz['a']
    del termz['of']
    del termz['and']
    del termz['in']
    del termz['i']
    del termz['my']
    del termz['to']
    del termz['is']
    del termz['on']
    del termz['for']
    del termz['it']
    del termz['with']
    del termz['at']
    del termz['these']
    wOut.write("Blog\t")
    sortedTermz  = sorted(termz.items(), key=lambda x:x[1], reverse=True)
    for word in sortedTermz[:500]:
        termsinorder.append(word[0])
        wOut.write(word[0])
        wOut.write('\t')





    #print "loop go site by site "
    with open("blogs.txt") as blogFile:
        lines = blogFile.readlines()
        wOut.write('\n')

        #for each blog url
        for line in lines:


            #download and parse xml
           response = urllib2.urlopen(line)
           xml = response.read()
           bs = BeautifulSoup(xml)
           blog = bs.rss.channel.title
           blog = str(blog).split('</title>')
           blog = blog[0].split('<title>')
           blog = blog[1]
           print blog
           wOut.write(blog)
           wOut.write('\n')
           items = bs.rss.channel.findAll("item")

           #reset term count before search
           for term in termsinorder:
               termz[term]=0


           #Count occurance of terms in each item/title
           for item in items:
               title = str(item).split("</title>")
               title = title[0].split("<title>")
               title = str(title[1])
               title = re.sub('[\"!@#$:.(),\-]', '', title)
               title = title.lower()
               #check against each term
               for term in termsinorder:
                   if term in title:
                       termz[term]+= title.count(term)




           for term in termsinorder:
                print termz[term]

           #write to blogdata.txt
           for term in termsinorder:
                wOut.write(str(termz[term]))
                wOut.write("\t")
           wOut.write("\n")



#gatherBlogs()
getTitles()
