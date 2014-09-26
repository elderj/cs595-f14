import local

with open("links.txt") as f:
    ListOfLinks = f.readlines()

fOut = open("DateEstimation.txt", "w")
i = 0

for link in ListOfLinks:

   #get URI
   uri = link.split(" ")
   print uri[2], " ", uri[3]

   i+=1
   maybe = local.cd(link)
   maybe = maybe.split('Estimated Creation Date": "')
   maybe = str(maybe[1])
   maybe = maybe.split('"')
   print "\n", i, ": ", uri[2] ," ", uri[3] , " " ,maybe[0]
   fOut.write(str(i))
   fOut.write(": ")
   fOut.write(uri[2])
   fOut.write(" ")
   fOut.write(uri[3])
   fOut.write(" ")
   if maybe[0] != "":
      fOut.write(maybe[0])
   else:
      fOut.write("NODATE")
   fOut.write("\n")
