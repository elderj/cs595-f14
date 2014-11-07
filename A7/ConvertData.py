"""


  Converts Matrices to JSON for D3


"""



def linksJSON():
    #get file containing links and their information
    wOut = open("before.json","w")
    wOut.write('{\n')
    wOut.write('  "nodes":[\n')
    a= 0
    while a< 34:
        wOut.write('    {"name":"')
        wOut.write(str(a))
        if a == 33:
            wOut.write('","group":1}\n')
        else:
            wOut.write('","group":1},\n')
        a+= 1
    wOut.write("  ],\n")
    wOut.write('  "links":[\n')


    with open("zachary.dat") as Karate:
        k= Karate.readlines()
        i= 41
        while i< 75:

            #Current Line
            line= i- 41
            print "Line ",line," :",k[i]
            data = k[i].split()
            j= 0
            for weight in data:
                if weight != "0" :
                    if j > line:
                        wOut.write('    {"source":')
                        wOut.write(str(line))
                        wOut.write(',"target":')
                        wOut.write(str(j))
                        wOut.write(',"value":')
                        wOut.write(weight)
                        if line == 32:
                            wOut.write('}')
                        else:
                            wOut.write('},\n')
                        print line,"->",j,weight
                j+= 1
                """
                    else:
                        print "Already recorded"
                else:
                    print "no connection"

                """


            #print "Get ", 33-line
            i+= 1
    wOut.write("\n  ]")
    wOut.write("\n}")
    wOut.close()





    #wOut.close()

#nodesJSON()
linksJSON()