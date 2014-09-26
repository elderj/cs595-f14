#!/usr/bin/env python

from bs4 import BeautifulSoup
import argparse
import urllib2
import time




#Argument Parsing Stuff
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--team", help="Select team to get current scores.put teams in quotations")
parser.add_argument("-s", "--seconds", help="Refresh time interval (in seconds.)")
parser.add_argument("-u", "--uri", help="Selected URI.")
args = parser.parse_args()

interval = float(args.seconds)


while 1:

    #handles arguments still need defaults
    if args.team:

            #print args.uri



    	if args.seconds:
             print "Score Update:"

    	else:
    	    print "No refresh interval entered"
    	
    	if args.uri:

    	#handles ampersands in command line argument
    	    theTeam = args.team

    	    if '&' in theTeam:
    	        buf = theTeam.split('&')
    	        theTeam= buf[0]+'&amp;'+buf[1]




    	    theURI = args.uri
    	    #print theURI
    	    data = urllib2.urlopen(theURI).read()
    	    #Get All Rows of the html table containing the scores
    	    AllRows = BeautifulSoup(data).find('div', id='mediasportsscoreboardgrandslam').find_all('tr')




    	    #Search All Rows for team name
    	    tmnm = str(theTeam)


    	    i=0
    	    while i< len(AllRows):
    	        teamsPlaying = AllRows[i].find_all('em')




    	        awayScore = AllRows[i].find("span", "away")
    	        homeScore = AllRows[i].find("span", "home")

    	        if tmnm in str(teamsPlaying):

    	            #string trimming

    	            awayTeam = str(teamsPlaying[0])
    	            homeTeam = str(teamsPlaying[1])
    	            awayScore = str(awayScore)
    	            homeScore = str(homeScore)
    	            awayTeam = awayTeam.split('<em>')[1]
    	            awayTeam = awayTeam.split('</em>')[0]

    	            homeTeam = homeTeam.split('<em>')[1]
    	            homeTeam = homeTeam.split('</em>')[0]
    	            awayScore = awayScore.strip('</span>')
    	            awayScore = awayScore.strip('class ="away winner">')
    	            homeScore = homeScore.strip('</span>')
    	            homeScore = homeScore.strip('class="home winner">')


    	            if tmnm == awayTeam:
    	                print "\nAway:", args.team  , " : " ,  awayScore
    	                print "Home:", homeTeam  , " : " ,  homeScore
    	                print "\n"


    	            if tmnm == homeTeam:
    	                print "\nAway: ", awayTeam  , " : " ,  awayScore
    	                print "Home:", args.team , " : " ,  homeScore
    	                print "\n"




    	        i = i+1
    else:
        print "No team specified"
    time.sleep(interval)




