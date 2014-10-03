print "Produces 1000URIs.txt"


#get file containing links and their information

wOut = open("1000URIs.txt", "w")
with open("links.txt") as links:
    ListOfLinks = links.readlines()
    #Strip info keep URI
    for link in ListOfLinks:
        line = link.split(" ")
        wOut.write(line[3])
        wOut.write("\n")
wOut.close()