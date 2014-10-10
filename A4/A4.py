from bs4 import BeautifulSoup
import os
import requests

def SaveTheFiles():


    with open("uris.txt") as uris:
        uris = uris.readlines()
        for uri in uris:
            print uri
            grab = len(os.listdir("sitelinks"))
            if grab < 101:
                try:
                    web = requests.get(uri)
                    if web.status_code == 200:
                        anchors = BeautifulSoup(web.text).findAll('a')
                        if len(anchors) > 5:
                            links = []

                        for a in anchors:
                            if a.has_key('href'):
                                    if links.count(a['href']) == 0:
                                        links.append(a['href'])

                        if len(links) > 1:

                            fn = uri.replace("\n","")
                            fn = uri.split("//")
                            fn = fn[1]
                            fn = uri.replace("/","")
                            fn = fn.replace("&","")
                            fn = fn.replace("@", "")
                            fn = fn.replace("%", "")
                            fn = fn[:88]
                            fn = "sitelinks/" + fn
                            f = open(fn,"w")
                            f.write("Site:\n")
                            f.write(uri)
                            f.write("\nLinks:\n")
                            #print len(anchors)
                            for link in links:
                                if link != '':
                                    if "http://" in link:
                                        link += ""
                                        f.write(link.encode('utf-8'))
                                        f.write("\n")
                                    elif "https://" in link:
                                        f.write(link.encode('utf-8'))
                                        f.write("\n")
                                        #print "https ",link
                                    elif link[0] == "/" :
                                        oc= uri.split("/")
                                        oc = "http://"+ oc[2]

                                        if link != "/":
                                            oc += link



                                        f.write(oc)
                                        print oc
                                        f.write("\n")
                            f.close()


                        print "\n"

                except requests.exceptions.ConnectionError as e:
                    print e





def dot():
    f = open("href.dot", "w")
    f.write("digraph href {\n")

    #get all files from site links
    files = os.listdir("sitelinks")
    for src in files:
        links = []
        loc = "sitelinks/"+ src
        with open(loc) as opn:
            lines = opn.readlines()

            base = lines[1]
            base = base.replace("\n","")
            base = base.replace("http://","")
            base = base.replace("https://","")
            base = base.replace("/","")
            base = base.replace("www.","")
            base = base.replace(".com","")
            base = base.replace(".org","")
            base = base.replace("-","")
            base = base.replace("?","")
            base = base[:40]
            base = '"' +base
            lines.pop(0)
            lines.pop(0)
            lines.pop(0)
            lines.pop(0)
            for line in lines:
                line = line.replace("\n","")
                line = line.replace("?","")
                line = line.replace("http://","")
                line = line.replace("https://","")
                line = line.replace("/","")
                line = line.replace("www.","")
                line = line.replace(".com","")
                line = line.replace(".org","")
                line = line.replace("-","")
                line = line[:40]
                if links.count(line) == 0:
                    links.append(line)
            for link in links:

                gvLine = base + '" -> "'
                link += '"'
                gvLine += link
                gvLine += ";\n"

                f.write(gvLine)
    f.write("}")
    f.close()





#SaveTheFiles()
dot()