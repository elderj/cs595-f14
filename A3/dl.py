import os
import mmap

def getRawHTML():
    with open("1000URIs.txt") as theURIs:
        URIs = theURIs.readlines()

        for URI in URIs:
	    if URI != "":
            	URI = URI.replace("\n", "")
            	sn = URI.split("//")
            	sn = sn[1]
            	sn = sn.replace("/", "")
            	sn = sn.replace("&", "")
            	sn = sn.replace("@", "")
            	sn = sn.replace("%", "")
            	sn = sn[:88]
            	print "Line:", URI
            	cmd = "wget -O src/" + sn
            	cmd += " "
            	cmd += URI
            	os.system(cmd)




def cutHTML():
    srcs = os.listdir("src")
    for src in srcs:
        if src != "":
            cmd = "lynx -dump -force_html src/"+ src
            cmd += " > prc/"
            cmd += src
            os.system(cmd)


def processHTML():
    #get all in prc
    ffs = []
    srcs = os.listdir("prc")
    for src in srcs:
        if src != "":
            #print "line:", src
            loc = "prc/"+src
            f = open(loc)
            s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            if s.find('shooting') != -1:
                #print 'add this uri to found list', src
                if len(ffs) < 10:
                    ffs.append(src)
                #    print len(ffs)
                #Find 10 URIS with content





    print "\n\nURI                          TC      WC       TF"
    print "---                          --      --       --"
    for each in ffs:
        #print "Filename:", each

        with open("1000URIs.txt") as theURIs:
            URIs = theURIs.readlines()
            for URI in URIs:
                wc = 0
                tc = 0


                if URI != "":
                    URI = URI.replace("\n", "")
                    sn = URI.split("//")
                    sn = sn[1]
                    sn = sn.replace("/", "")
                    sn = sn.replace("&", "")
                    sn = sn.replace("@", "")
                    sn = sn.replace("%", "")
                    sn = sn[:88]
                    if each == sn:
                        #print like this
                        loc = "prc/"+sn
                        with open(loc, 'r') as f:
                            for line in f:
                                count = line.count("shooting")
                                if count !=0:
                                    tc += count
                                words = line.split()
                                wc += len(words)

                        tf = tc/float(wc)
                        print URI[:25], "  ",tc,"     ",wc,"   ",tf
                        #print URI, "\n"

#caluluate values for each




getRawHTML()
cutHTML()
processHTML()