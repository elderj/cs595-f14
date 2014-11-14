from math import sqrt


wOut = open("u.critics", "w")

rating= {}
count= {}
total= {}


with open("u.data") as uData:
    lines = uData.readlines()
    for line in lines:
        print "\n"
        chunk = line.split()
        #print "Movie:",chunk[1]
        key = chunk[1]
        #print "Rating:",chunk[2]
        value = float(chunk[2])
        if key in rating:
            count[key]+=1
            total[key] += float(value)

            average = total[key] / count[key]
            rating[key] = average

        else:
            rating[key] = float(value)
            count[key] = 1
            total[key] = float(value)


#1
print "Best Average Review"
wOut.write("1: ")
one = sorted(rating.items(), key=lambda x:x[1], reverse=True)
i=0
while i<20:
    if one[i][1] == 5.0:
        wOut.write( one[i][0])
        wOut.write(",")
        i+=1
    else:
        i+=100
wOut.write("\n")


#2
print "Highest Review Count"
wOut.write("2: ")
two = sorted(count.items(), key=lambda x:x[1], reverse=True)
i=0
while i<5:
        print "Movie:", two[i][0], "  # of ratings:", two[i][1]
        wOut.write("(")
        wOut.write(two[i][0])
        wOut.write(";")
        wOut.write(str(two[i][1]))
        wOut.write("),")
        i+=1

wOut.write("\n")




#Get all ids based on gender for 3 and 4
mIDs = []
mrating= {}
mcount= {}
mtotal= {}

fIDs = []
frating= {}
fcount= {}
ftotal= {}

with open("u.user") as uUser:
    lines = uUser.readlines()
    for line in lines:
        chunk = line.split('|')
        if chunk[2] == 'F':
            fIDs.append(chunk[0])
        else:
            mIDs.append(chunk[0])

with open("u.data") as uData:
    lines = uData.readlines()
    for line in lines:
        chunk = line.split()
        if chunk[0] in fIDs:
            key = chunk[1]
        #print "Rating:",chunk[2]
            value = float(chunk[2])
            if key in frating:
                fcount[key]+=1
                ftotal[key] += float(value)
                faverage = ftotal[key] / count[key]
                frating[key] = average
            else:
                frating[key] = float(value)
                fcount[key] = 1
                ftotal[key] = float(value)
        else:
            key = chunk[1]
            value = float(chunk[2])
            if key in mrating:
                mcount[key]+=1
                mtotal[key] += float(value)
                maverage = mtotal[key] / count[key]
                mrating[key] = average
            else:
                mrating[key] = float(value)
                mcount[key] = 1
                mtotal[key] = float(value)




#3
print "3. Best Average Review(Female)"
wOut.write("3: ")
three = sorted(frating.items(), key=lambda x:x[1], reverse=True)
i=0
while i<20:
    if three[i][1] == 5.0:
        print three[i][0]
        wOut.write(three[i][0])
        wOut.write(", ")
        i+=1
    else:
        i+=100


wOut.write("\n")



#4
print "4. Best Average Review(Male)"
wOut.write("4: ")
four = sorted(mrating.items(), key=lambda x:x[1], reverse=True)
i=0
while i<20:
    if four[i][1] == 5.0:
        print four[i][0]
        wOut.write(four[i][0])
        wOut.write(", ")
        i+=1
    else:
        i+=100

wOut.write("\n")





#6
rcount = {}
with open("u.data") as uData:
    print "6. who rated the most films?"
    wOut.write("6: ")
    lines = uData.readlines()
    for line in lines:
        chunk = line.split()
        key = chunk[0]
        if key in rcount:
            rcount[key]+=1
        else:
            rcount[key]=1

six = sorted(rcount.items(), key=lambda x:x[1], reverse=True)
print six[0]
wOut.write(str(six[0]))
wOut.write(", ")
print six[1]
wOut.write(str(six[1]))
wOut.write(", ")
print six[2]
wOut.write(str(six[2]))
wOut.write(", ")
print six[3]
wOut.write(str(six[3]))
wOut.write(", ")
print six[4]
wOut.write(str(six[4]))
wOut.write(", ")

wOut.write("\n")








#Get raters by gender and age
mUnder = []
mUnderRating= {}
mUnderCount= {}
mUnderTotal= {}

mOver = []
mOverRating= {}
mOverCount= {}
mOverTotal= {}


fUnder = []
fUnderRating= {}
fUnderCount= {}
fUnderTotal= {}

fOver = []
fOverRating= {}
fOverCount= {}
fOverTotal= {}




print "9. Highest by men over 40 and under 40"
with open("u.user") as uUser:
    lines = uUser.readlines()
    for line in lines:
        chunk = line.split('|')
        if chunk[2] == 'M':
            if int(chunk[1]) < 40:
                #print chunk[1], "under"
                mUnder.append(chunk[0])
            else:
                #print chunk[1], "over"
                mOver.append(chunk[0])
        else:
            if int(chunk[1]) < 40:
                #print chunk[1], "under"
                fUnder.append(chunk[0])
            else:
                #print chunk[1], "over"
                fOver.append(chunk[0])



with open("u.data") as uData:
    lines = uData.readlines()
    for line in lines:
        chunk = line.split()
        if chunk[0] in mUnder: #if user id in mUnder

            key = chunk[1] #movie title
            if key in mUnderCount:
                #print "already recorded"
                mUnderCount[key] += int(1)
                mUnderTotal[key] += float(chunk[2])
                average = float(mUnderTotal[key]) / float(mUnderCount[key])
                mUnderRating[key] = average

            else:
                #print "new movie"
                mUnderCount[key] = 1
                mUnderTotal[key] = float(chunk[2])
                mUnderRating[key] = float(chunk[2])
        elif chunk[0] in mOver:

            key = chunk[1] #movie title
            if key in mOverCount:
                #print "already recorded"
                mOverCount[key] += int(1)
                mOverTotal[key] += float(chunk[2])
                average = float(mOverTotal[key]) / float(mOverCount[key])
                mUnderRating[key] = average

            else:
                #print "new movie"
                mOverCount[key] = 1
                mOverTotal[key] = float(chunk[2])
                mOverRating[key] = float(chunk[2])
        elif chunk[0] in fUnder:
            key = chunk[1] #movie title
            if key in fUnderCount:
                #print "already recorded"
                fUnderCount[key] += int(1)
                fUnderTotal[key] += float(chunk[2])
                average = float(fUnderTotal[key]) / float(fUnderCount[key])
                fUnderRating[key] = average

            else:
                #print "new movie"
                fUnderCount[key] = 1
                fUnderTotal[key] = float(chunk[2])
                fUnderRating[key] = float(chunk[2])

        elif chunk[0] in fOver:
            key = chunk[1] #movie title
            if key in fOverCount:
                #print "already recorded"
                fOverCount[key] += int(1)
                fOverTotal[key] += float(chunk[2])
                average = float(fOverTotal[key]) / float(fOverCount[key])
                fUnderRating[key] = average

            else:
                #print "new movie"
                fOverCount[key] = 1
                fOverTotal[key] = float(chunk[2])
                fOverRating[key] = float(chunk[2])

        else:
            print "error"




















#9
print "9a. Best Average Review(Men Under 40)"
wOut.write("9a: ")

nineA = sorted(mUnderRating.items(), key=lambda x:x[1], reverse=True)

i=0
while i<20:
    if nineA[i][1] == 5.0:
        print nineA[i][0]
        wOut.write(nineA[i][0])
        wOut.write(", ")
        i+=1
    else:
        i+=100
        #count number of ratings for each user     count dictionary

wOut.write("\n")

print "9b. Best Average Review(Men Over 40)"
wOut.write("9b: ")
nineB = sorted(mOverRating.items(), key=lambda x:x[1], reverse=True)

i=0
while i<20:
    if nineB[i][1] == 5.0:
        print nineB[i][0]
        wOut.write(nineB[i][0])
        wOut.write(", ")
        i+=1
    else:
        i+=100
        #count number of ratings for each user     count dictionary

wOut.write("\n")

#10
print "10a. Best Average Review(Women Under 40)"
wOut.write("10a: ")

tenA = sorted(fUnderRating.items(), key=lambda x:x[1], reverse=True)

i=0
while i<20:
    if tenA[i][1] == 5.0:
        wOut.write(tenA[i][0])
        wOut.write(", ")
        i+=1
    else:
        i+=100
        #count number of ratings for each user     count dictionary
wOut.write("\n")



print "10b. Best Average Review(Women Over 40)"
wOut.write("10b: ")
tenB = sorted(fOverRating.items(), key=lambda x:x[1], reverse=True)

i=0
while i<20:
    if tenB[i][1] == 5.0:
        print tenB[i][0]
        wOut.write(tenB[i][0])
        wOut.write(", ")
        i+=1
    else:
        i+=100
        #count number of ratings for each user     count dictionary

wOut.close()
print "\n\n"




#convert data to to answers and write answers to 'u.answers'
wOut = open("u.answers","w")


titles={}

with open("u.item") as uItem:
    lines = uItem.readlines()
    for line in lines:
        chunk = line.split("|")
        key = chunk[0]
        value = chunk[1]
        titles[key] = value

#print titles

with open("u.critics") as uCritics:
    lines = uCritics.readlines()
    for line in lines:
            line = str(line).replace(" ", "")
            chop = line.split(":")



            if chop[0] == '1':
                entry = chop[1].split(",")
                print "1. Movies with Highest Average Rating"
                wOut.write("1. Movies with Highest Average Rating")
                wOut.write("\n")

                for ID in entry:
                    if ID != '\n':

                        print titles[ID], "rating: 5.0"
                        wOut.write(titles[ID])
                        wOut.write(" rating: 5.0\n")

                wOut.write("\n")


            if chop[0] == '2':
                print "\n2. Movies with most reviews"
                wOut.write("\n2. Movies with most reviews\n")
                entry = chop[1].split(",")
                for ID in entry:
                    if ID != '\n':
                        ID = str(ID).replace("(","")
                        ID = str(ID).replace(")","")
                        ID = ID.split(";")
                        print titles[ID[0]], " total reviews: ", ID[1]
                        wOut.write(titles[ID[0]])
                        wOut.write(" total reviews: ")
                        wOut.write(ID[1])
                        wOut.write("\n")
                wOut.write("\n")


            if chop[0] == '3':
                print "\n3.Movies with Highest Average Rating(female)"
                wOut.write("\n3.Movies with Highest Average Rating(female)\n")
                entry = chop[1].split(",")
                for ID in entry:
                    if ID != '\n':
                        print titles[ID], "rating: 5.0"
                        wOut.write(titles[ID])
                        wOut.write(" rating: 5.0")
                        wOut.write("\n")
                wOut.write("\n")






            if chop[0] == '4':
                print "\n4. Movies with Highest Average Rating(male)"
                wOut.write("\n4.Movies with Highest Average Rating(male)\n")
                entry = chop[1].split(",")
                for ID in entry:
                    if ID != '\n':
                        print titles[ID], "rating: 5.0"
                        wOut.write(titles[ID])
                        wOut.write(" rating: 5.0")
                        wOut.write("\n")
                wOut.write("\n")


            if chop[0] == '6':
                print "\n6. Who Rated the Most Films?"
                wOut.write("\n6. Who Rated the Most Films?\n")
                entry = str(chop[1]).replace(",", "")
                entry = entry.split(")")
                for e in entry:
                    e = e.split("'")
                    if e[0] != '\n':
                        print "user", e[1], " total ratings:", e[2]
                        wOut.write("User: ")
                        wOut.write(e[1])
                        wOut.write(" total ratings: ")
                        wOut.write(e[2])
                    wOut.write("\n")


            if chop[0] == '9a':
                print "\n9a. Highest Ratings by Men Under 40"
                wOut.write("\n9a. Highest Ratings by Men Under 40\n")
                entry = chop[1].split(',')
                for e in entry:
                    if e != '\n':
                        print titles[e]
                        wOut.write(titles[e])
                        wOut.write("\n")
                wOut.write("\n")

            if chop[0] == '9b':
                print "\n9b.Highest Ratings by  Men Over 40"
                wOut.write("\n9b. Highest Ratings by Men Over 40\n")
                entry = chop[1].split(',')
                for e in entry:
                    if e != '\n':
                        print titles[e]
                        wOut.write(titles[e])
                        wOut.write("\n")
                wOut.write("\n")

            if chop[0] == '10a':
                print "\n10a.Highest Ratings by  Women Under 40"
                wOut.write("\n10a. Highest Ratings by Women Under 40\n")
                entry = chop[1].split(',')
                for e in entry:
                    if e != '\n':
                        print titles[e]
                        wOut.write(titles[e])
                        wOut.write("\n")
                wOut.write("\n")

            if chop[0] == '10b':
                print "\n10b.Highest Ratings by  Women Under 40"
                wOut.write("\n10b. Highest Ratings by Women Over 40\n")
                entry = chop[1].split(',')
                for e in entry:
                    if e != '\n':
                        if e != '':
                            print titles[e]
                            wOut.write(titles[e])
                            wOut.write("\n")
                wOut.write("\n")




#5
#get number of ratings for top gun
print "The Movie Top Gun"
a1 =count['161']
a2 =rating['161']


#find a movie with the smallest distance for both
eDistFromTopGun = {}

i = 0
#determine e dist for every movie title (using ids)


for key in rating.keys():
    b1 = count[key]
    b2 = rating[key]

    edist = 1/(1+sqrt(pow(a1-b1,2)+pow(a2-b2,2)))
    eDistFromTopGun[key] = edist

#Highest correlation
fivea = sorted(eDistFromTopGun.items(), key=lambda x:x[1], reverse=False)

wOut.write("\n\n5. What Movie is rated most like Top Gun, the least?")

print fivea[0][0], fivea[0][1]
with open("u.item") as uItem:
    lines = uItem.readlines()
    for line in lines:
        chunk = line.split('|')
        if chunk[0] == fivea[0][0]:
            wOut.write("\n The Most: ")
            wOut.write(chunk[1])




eDistFromTopGun['161'] = 0
#Lowest correlation
fiveb = sorted(eDistFromTopGun.items(), key=lambda x:x[1], reverse=True)




print fiveb[0][0], fiveb[0][1]
with open("u.item") as uItem:
    lines = uItem.readlines()
    for line in lines:
        chunk = line.split('|')
        if chunk[0] == fiveb[0][0]:
            wOut.write("\n The Least: ")
            wOut.write(chunk[1])

wOut.close()