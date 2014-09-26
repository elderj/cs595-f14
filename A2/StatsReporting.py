# -*- coding: utf-8 -*-
#print "Read in links.txt and count the number of URIS with 0, 1, 2,... mementos"
def two():
    with open("links.txt") as links:
        ListOfLinks = links.readlines()
        uniques = []
        nums =[]

        wOut = open("two.txt", "w")

        #get unique list
        for link in ListOfLinks:
            spl = link.split(" ")
            #print link[0], link[4]
            test = uniques.count(spl[4])
            if test == 0:
                #print "adding"
                uniques.append(spl[4])

        for item in uniques:
            a = item.split("Mementos:")
            b = a[1].split("\n")
            b = int(b[0])
            nums.append(b)
        #prints sorted unique numbers of mementos
        for num in sorted(nums):
            numCount = 0
            c = "Mementos:" + str(num) + "\n"
            #print c
            for link in ListOfLinks:
                d = link.split(" ")
                e = d[4]
                if e == c:
                    numCount += 1
            print c,"total", numCount
            wOut.write(str(c))
            wOut.write(" ")
            wOut.write(str(numCount))
            wOut.write("\n")
        wOut.close()





def three():
    wOut = open("three.txt", "w")
    with open("links.txt") as links:
        ListOfLinks = links.readlines()
        with open("DateEstimation.txt") as DE:
            CarbonDate = DE.readlines()


            #all links in links.txt
            for link in ListOfLinks:
                lURI = link.split(" ")

                #if mementos exist
                if lURI[4] != "Mementos:0\n":
#                    print lURI[3]

                    #all lines from DateEstimation.txt
                    for line in CarbonDate:
                        sub = line.split(" ")

                        #URIS with mementos
                        if lURI[3] == sub[2]:

                            #URIs with mementos and an estimation date
                            if sub[3] != "NODATE\n":
                                wOut.write(sub[2],)
                                wOut.write("Estimated Date:")
                                wOut.write(sub[3].strip("\n"))
                                wOut.write(" ")
                                wOut.write(lURI[4])




two()
three()