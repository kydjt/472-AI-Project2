import numpy as np
import math

#a method to sum all elements of a list
def totalcountlist(mylist):
    sum=0
    for i in range(len(mylist)):
        sum+=float(mylist[i])
    return sum


# creating unigram with isalpha
def createcountisalpha(mystring):
        mydictionary={}
        for char1 in mystring:
            if (char1.isalpha() or char1==" "):
                if(not (char1 in mydictionary)):
                    mydictionary[char1]=1
                elif(char1 in mydictionary):
                    mydictionary[char1]=(float(mydictionary[char1])+1)
        return mydictionary

#creating bigram with isalpha
def createbigramisalpha(mystring):
    mybigramdic={}
    for i in range(len(mystring)-1):
        if((mystring[i].isalpha() or mystring[i]==" ") and (mystring[i+1].isalpha() or mystring[i+1]==" ")):
            bigramkey=(mystring[i]+mystring[i+1])
            if(not(bigramkey in mybigramdic)):
                mybigramdic[bigramkey]=1
            elif(bigramkey in mybigramdic):
                mybigramdic[bigramkey]=float(mybigramdic[bigramkey])+1
    return mybigramdic


# creating trigram with isalpha
def createtrigramisalpha(mystring):
    mytrigramdic={}
    for i in range(len(mystring)-2):
        if((mystring[i].isalpha() or mystring[i]==" ") and (mystring[i+1].isalpha() or mystring[i+1]==" ") and (mystring[i+2].isalpha() or mystring[i+2]==" ")):
            trigramkey=(mystring[i]+mystring[i+1]+mystring[i+2])
            if(not(trigramkey in mytrigramdic)):
                mytrigramdic[trigramkey]=1
            elif(trigramkey in mytrigramdic):
                mytrigramdic[trigramkey]=float(mytrigramdic[trigramkey])+1
    return mytrigramdic

# creating 4grams
def create4gramisalpha(mystring):
    my4gramdic={}
    for i in range(len(mystring)-3):
        if((mystring[i].isalpha() or mystring[i]==" ") and (mystring[i+1].isalpha() or mystring[i+1]==" ") and (mystring[i+2].isalpha() or mystring[i+2]==" ") and (mystring[i+3].isalpha() or mystring[i+3]==" ")):
            fourgramkey=(mystring[i]+mystring[i+1]+mystring[i+2]+mystring[i+3])
            if(not(fourgramkey in my4gramdic)):
                my4gramdic[fourgramkey]=1
            elif(fourgramkey in my4gramdic):
                my4gramdic[fourgramkey]=float(my4gramdic[fourgramkey])+1
    return my4gramdic


# merging two dictionaries
def combinedictionaries(dic1,dic2):
    for i in dic2:
        if(i in dic1):
            dic1[i]=float(dic1[i])+float(dic2[i])
        else:
            dic1[i]=dic2[i]
    return dic1



def getfirst3letof4gram(mydic):
    mylist=[]
    for i in mydic:
        trigram=i[0]+i[1]+i[2]
        if(not (trigram  in mylist)):
            mylist.append(trigram)
    return mylist





def getfirst2letoftrigram(mydic):
    mylist=[]
    for i in mydic:
        bigram=i[0]+i[1]
        if(not (bigram  in mylist)):
            mylist.append(bigram)
    return mylist

def trainv3(train,n):
    tweets = []
    numtweetbasque = 0
    numtweetcatalan = 0
    numtweetgalician = 0
    numtweetspanish = 0
    numtweetenglish = 0
    numtweetportoguse = 0

    countalphabasque={}
    countalphacatalan={}
    countalphagalician={}
    countalphaspanish={}
    countalphaenglish={}
    countalphaportoguse={}

    countalphabigrambasque = {}
    countalphabigramcatalan = {}
    countalphabigramgalician = {}
    countalphabigramspanish = {}
    countalphabigramenglish = {}
    countalphabigramportoguse = {}

    countalphatrigrambasque = {}
    countalphatrigramcatalan = {}
    countalphatrigramgalician = {}
    countalphatrigramspanish = {}
    countalphatrigramenglish = {}
    countalphatrigramportoguse = {}


    countalpha4grambasque = {}
    countalpha4gramcatalan = {}
    countalpha4gramgalician = {}
    countalpha4gramspanish = {}
    countalpha4gramenglish = {}
    countalpha4gramportoguse = {}

    exclusivebasque=[]
    exclusivecatalan=[]
    exclusivegalician=[]
    exclusivespanish=[]
    exclusiveenglish=[]
    exclusiveportoguse=[]




    results=[]
    with open(train, encoding="utf8") as f:
        for line in f:
            tweets.append(line)
    copystring = [''] * (len(tweets))
    copytweets = [''] * (len(tweets))
    for i in range(len(tweets)):
        if (i < (len(tweets) - 1)):
            tweets[i] = tweets[i][:-1]
        copytweets[i] = tweets[i].split()
        index = tweets[i].index(copytweets[i][3])
        copystring[i] = tweets[i][index:]

        if(n==1):

            if (copytweets[i][2] == 'eu'):
                countalphabasque = combinedictionaries(countalphabasque,createcountisalpha(copystring[i]))
                numtweetbasque += 1
            elif (copytweets[i][2] == 'ca'):
                countalphacatalan =combinedictionaries(countalphacatalan,createcountisalpha(copystring[i]))
                numtweetcatalan += 1
            elif (copytweets[i][2] == 'gl'):
                countalphagalician = combinedictionaries(countalphagalician,createcountisalpha(copystring[i]))
                numtweetgalician += 1
            elif (copytweets[i][2] == 'es'):
                countalphaspanish = combinedictionaries(countalphaspanish,createcountisalpha(copystring[i]))
                numtweetspanish += 1
            elif (copytweets[i][2] == 'en'):
                countalphaenglish = combinedictionaries(countalphaenglish,createcountisalpha(copystring[i]))
                numtweetenglish += 1
            elif (copytweets[i][2] == 'pt'):
                countalphaportoguse = combinedictionaries(countalphaportoguse,createcountisalpha(copystring[i]))
                numtweetportoguse += 1
        elif(n==2):

            if (copytweets[i][2] == 'eu'):
                countalphabasque = combinedictionaries(countalphabasque,createcountisalpha(copystring[i]))
                countalphabigrambasque = combinedictionaries(countalphabigrambasque, createbigramisalpha(copystring[i]))
                numtweetbasque += 1
            elif (copytweets[i][2] == 'ca'):
                countalphacatalan =combinedictionaries(countalphacatalan,createcountisalpha(copystring[i]))
                countalphabigramcatalan = combinedictionaries(countalphabigramcatalan, createbigramisalpha(copystring[i]))
                numtweetcatalan += 1
            elif (copytweets[i][2] == 'gl'):
                countalphagalician = combinedictionaries(countalphagalician,createcountisalpha(copystring[i]))
                countalphabigramgalician = combinedictionaries(countalphabigramgalician, createbigramisalpha(copystring[i]))
                numtweetgalician += 1
            elif (copytweets[i][2] == 'es'):
                countalphaspanish = combinedictionaries(countalphaspanish,createcountisalpha(copystring[i]))
                countalphabigramspanish = combinedictionaries(countalphabigramspanish, createbigramisalpha(copystring[i]))
                numtweetspanish += 1
            elif (copytweets[i][2] == 'en'):
                countalphaenglish = combinedictionaries(countalphaenglish,createcountisalpha(copystring[i]))
                countalphabigramenglish = combinedictionaries(countalphabigramenglish, createbigramisalpha(copystring[i]))
                numtweetenglish += 1
            elif (copytweets[i][2] == 'pt'):
                countalphaportoguse = combinedictionaries(countalphaportoguse,createcountisalpha(copystring[i]))
                countalphabigramportoguse = combinedictionaries(countalphabigramportoguse, createbigramisalpha(copystring[i]))
                numtweetportoguse += 1
        elif(n==3):

            if (copytweets[i][2] == 'eu'):
                countalphabasque = combinedictionaries(countalphabasque, createcountisalpha(copystring[i]))
                countalphatrigrambasque = combinedictionaries(countalphatrigrambasque, createtrigramisalpha(copystring[i]))
                numtweetbasque += 1
            elif (copytweets[i][2] == 'ca'):
                countalphacatalan = combinedictionaries(countalphacatalan, createcountisalpha(copystring[i]))
                countalphatrigramcatalan = combinedictionaries(countalphatrigramcatalan, createtrigramisalpha(copystring[i]))
                numtweetcatalan += 1
            elif (copytweets[i][2] == 'gl'):
                countalphagalician = combinedictionaries(countalphagalician, createcountisalpha(copystring[i]))
                countalphatrigramgalician =combinedictionaries(countalphatrigramgalician, createtrigramisalpha(copystring[i]))
                numtweetgalician += 1
            elif (copytweets[i][2] == 'es'):
                countalphaspanish = combinedictionaries(countalphaspanish, createcountisalpha(copystring[i]))
                countalphatrigramspanish = combinedictionaries(countalphatrigramspanish, createtrigramisalpha(copystring[i]))
                numtweetspanish += 1
            elif (copytweets[i][2] == 'en'):
                countalphaenglish = combinedictionaries(countalphaenglish, createcountisalpha(copystring[i]))
                countalphatrigramenglish = combinedictionaries(countalphatrigramenglish, createtrigramisalpha(copystring[i]))
                numtweetenglish += 1
            elif (copytweets[i][2] == 'pt'):
                countalphaportoguse = combinedictionaries(countalphaportoguse, createcountisalpha(copystring[i]))
                countalphatrigramportoguse = combinedictionaries(countalphatrigramportoguse, createtrigramisalpha(copystring[i]))
                numtweetportoguse += 1
        elif(n==4):
            if (copytweets[i][2] == 'eu'):
                countalphabasque = combinedictionaries(countalphabasque, createcountisalpha(copystring[i]))
                countalpha4grambasque = combinedictionaries(countalpha4grambasque, create4gramisalpha(copystring[i]))
                numtweetbasque += 1
            elif (copytweets[i][2] == 'ca'):
                countalphacatalan = combinedictionaries(countalphacatalan, createcountisalpha(copystring[i]))
                countalpha4gramcatalan = combinedictionaries(countalpha4gramcatalan, create4gramisalpha(copystring[i]))
                numtweetcatalan += 1
            elif (copytweets[i][2] == 'gl'):
                countalphagalician = combinedictionaries(countalphagalician, createcountisalpha(copystring[i]))
                countalpha4gramgalician =combinedictionaries(countalpha4gramgalician, create4gramisalpha(copystring[i]))
                numtweetgalician += 1
            elif (copytweets[i][2] == 'es'):
                countalphaspanish = combinedictionaries(countalphaspanish, createcountisalpha(copystring[i]))
                countalpha4gramspanish = combinedictionaries(countalpha4gramspanish, create4gramisalpha(copystring[i]))
                numtweetspanish += 1
            elif (copytweets[i][2] == 'en'):
                countalphaenglish = combinedictionaries(countalphaenglish, createcountisalpha(copystring[i]))
                countalpha4gramenglish = combinedictionaries(countalpha4gramenglish, create4gramisalpha(copystring[i]))
                numtweetenglish += 1
            elif (copytweets[i][2] == 'pt'):
                countalphaportoguse = combinedictionaries(countalphaportoguse, createcountisalpha(copystring[i]))
                countalpha4gramportoguse = combinedictionaries(countalpha4gramportoguse, create4gramisalpha(copystring[i]))
                numtweetportoguse += 1



    if(n==1):
        results.append(numtweetbasque)
        results.append(numtweetcatalan)
        results.append(numtweetgalician)
        results.append(numtweetspanish)
        results.append(numtweetenglish)
        results.append(numtweetportoguse)


        results.append(countalphabasque)
        results.append(countalphacatalan)
        results.append(countalphagalician)
        results.append(countalphaspanish)
        results.append(countalphaenglish)
        results.append(countalphaportoguse)


        results.append(len(countalphabasque))
        results.append(len(countalphacatalan))
        results.append(len(countalphagalician))
        results.append(len(countalphaspanish))
        results.append(len(countalphaenglish))
        results.append(len(countalphaportoguse))


    elif(n==2):
        results.append(numtweetbasque)
        results.append(numtweetcatalan)
        results.append(numtweetgalician)
        results.append(numtweetspanish)
        results.append(numtweetenglish)
        results.append(numtweetportoguse)

        results.append(countalphabigrambasque)
        results.append(countalphabigramcatalan)
        results.append(countalphabigramgalician)
        results.append(countalphabigramspanish)
        results.append(countalphabigramenglish)
        results.append(countalphabigramportoguse)

        results.append(len(countalphabasque))
        results.append(len(countalphacatalan))
        results.append(len(countalphagalician))
        results.append(len(countalphaspanish))
        results.append(len(countalphaenglish))
        results.append(len(countalphaportoguse))




    elif(n==3):

        results.append(numtweetbasque)
        results.append(numtweetcatalan)
        results.append(numtweetgalician)
        results.append(numtweetspanish)
        results.append(numtweetenglish)
        results.append(numtweetportoguse)

        results.append(countalphatrigrambasque)
        results.append(countalphatrigramcatalan)
        results.append(countalphatrigramgalician)
        results.append(countalphatrigramspanish)
        results.append(countalphatrigramenglish)
        results.append(countalphatrigramportoguse)

        results.append(len(countalphabasque))
        results.append(len(countalphacatalan))
        results.append(len(countalphagalician))
        results.append(len(countalphaspanish))
        results.append(len(countalphaenglish))
        results.append(len(countalphaportoguse))

        results.append(getfirst2letoftrigram(countalphatrigrambasque))
        results.append(getfirst2letoftrigram(countalphatrigramcatalan))
        results.append(getfirst2letoftrigram(countalphatrigramgalician))
        results.append(getfirst2letoftrigram(countalphatrigramspanish))
        results.append(getfirst2letoftrigram(countalphatrigramenglish))
        results.append(getfirst2letoftrigram(countalphatrigramportoguse))

        for i in countalphabasque:
            if( (not(i in countalphacatalan)) and (not(i in countalphagalician)) and (not(i in countalphaspanish)) and (not(i in countalphaenglish)) and (not(i in countalphaportoguse)) ):
                exclusivebasque.append(i)
        for i in countalphacatalan:
            if( (not(i in countalphabasque)) and (not(i in countalphagalician)) and (not(i in countalphaspanish)) and (not(i in countalphaenglish)) and (not(i in countalphaportoguse)) ):
                exclusivecatalan.append(i)
        for i in countalphagalician:
            if( (not(i in countalphabasque)) and (not(i in countalphacatalan)) and (not(i in countalphaspanish)) and (not(i in countalphaenglish)) and (not(i in countalphaportoguse)) ):
                exclusivegalician.append(i)
        for i in countalphaspanish:
            if( (not(i in countalphacatalan)) and (not(i in countalphagalician)) and (not(i in countalphabasque)) and (not(i in countalphaenglish)) and (not(i in countalphaportoguse)) ):
                exclusivespanish.append(i)
        for i in countalphaenglish:
            if( (not(i in countalphacatalan)) and (not(i in countalphagalician)) and (not(i in countalphaspanish)) and (not(i in countalphabasque)) and (not(i in countalphaportoguse)) ):
                exclusiveenglish.append(i)
        for i in countalphaportoguse:
            if( (not(i in countalphacatalan)) and (not(i in countalphagalician)) and (not(i in countalphaspanish)) and (not(i in countalphaenglish)) and (not(i in countalphabasque)) ):
                exclusiveportoguse.append(i)

        results.append(exclusivebasque)
        results.append(exclusivecatalan)
        results.append(exclusivegalician)
        results.append(exclusivespanish)
        results.append(exclusiveenglish)
        results.append(exclusiveportoguse)


    elif(n==4):
        results.append(numtweetbasque)
        results.append(numtweetcatalan)
        results.append(numtweetgalician)
        results.append(numtweetspanish)
        results.append(numtweetenglish)
        results.append(numtweetportoguse)

        results.append(countalpha4grambasque)
        results.append(countalpha4gramcatalan)
        results.append(countalpha4gramgalician)
        results.append(countalpha4gramspanish)
        results.append(countalpha4gramenglish)
        results.append(countalpha4gramportoguse)

        results.append(len(countalphabasque))
        results.append(len(countalphacatalan))
        results.append(len(countalphagalician))
        results.append(len(countalphaspanish))
        results.append(len(countalphaenglish))
        results.append(len(countalphaportoguse))

        results.append(getfirst3letof4gram(countalpha4grambasque))
        results.append(getfirst3letof4gram(countalpha4gramcatalan))
        results.append(getfirst3letof4gram(countalpha4gramgalician))
        results.append(getfirst3letof4gram(countalpha4gramspanish))
        results.append(getfirst3letof4gram(countalpha4gramenglish))
        results.append(getfirst3letof4gram(countalpha4gramportoguse))

        for i in countalphabasque:
            if( (not(i in countalphacatalan)) and (not(i in countalphagalician)) and (not(i in countalphaspanish)) and (not(i in countalphaenglish)) and (not(i in countalphaportoguse)) ):
                exclusivebasque.append(i)
        for i in countalphacatalan:
            if( (not(i in countalphabasque)) and (not(i in countalphagalician)) and (not(i in countalphaspanish)) and (not(i in countalphaenglish)) and (not(i in countalphaportoguse)) ):
                exclusivecatalan.append(i)
        for i in countalphagalician:
            if( (not(i in countalphabasque)) and (not(i in countalphacatalan)) and (not(i in countalphaspanish)) and (not(i in countalphaenglish)) and (not(i in countalphaportoguse)) ):
                exclusivegalician.append(i)
        for i in countalphaspanish:
            if( (not(i in countalphacatalan)) and (not(i in countalphagalician)) and (not(i in countalphabasque)) and (not(i in countalphaenglish)) and (not(i in countalphaportoguse)) ):
                exclusivespanish.append(i)
        for i in countalphaenglish:
            if( (not(i in countalphacatalan)) and (not(i in countalphagalician)) and (not(i in countalphaspanish)) and (not(i in countalphabasque)) and (not(i in countalphaportoguse)) ):
                exclusiveenglish.append(i)
        for i in countalphaportoguse:
            if( (not(i in countalphacatalan)) and (not(i in countalphagalician)) and (not(i in countalphaspanish)) and (not(i in countalphaenglish)) and (not(i in countalphabasque)) ):
                exclusiveportoguse.append(i)

        results.append(exclusivebasque)
        results.append(exclusivecatalan)
        results.append(exclusivegalician)
        results.append(exclusivespanish)
        results.append(exclusiveenglish)
        results.append(exclusiveportoguse)

    return results




def countlefttotalbigram(dic,leftchar):
    sum=0
    for i in dic:
        if(i[0]==leftchar):
            sum+=float(dic[i])

    return sum


def counttrigramtotal12(dic,one,two):
    sum=0
    for i in dic:
        if(i[0]==one and i[1]==two):
            sum+=float(dic[i])
    return sum


def countkeys(mydict):
    sum=0
    for i in mydict:
        sum+=float(mydict[i])
    return sum




def getingfirstletofbigram(mydic):
    mylist=[]
    for i in mydic:
        mylist.append(i[0])
    return mylist

def getingsecondletofbigram(mydic):
    mylist=[]
    for j in mydic:
        mylist.append(j[1])
    return mylist



def calculatescoreisalphatrigram(mystring, smoothing, classsize, vocabularysize, totaldocs, traininglist,bigramlist):
    score = 0


    for i in range(len(mystring)-2):
        trigram=mystring[i] + mystring[i + 1]+mystring[i+2]
        bigram=mystring[i] + mystring[i + 1]
        if (((mystring[i].isalpha()) or mystring[i]==" ") and ((mystring[i + 1].isalpha()) or mystring[i+1]==" ") and ((mystring[i + 2].isalpha() or mystring[i+2]==" ") )and (trigram in traininglist)):
            if((float(traininglist[trigram]) + smoothing) >0 and (counttrigramtotal12(traininglist,mystring[i],mystring[i+1]) + (vocabularysize + 1) * smoothing)>0):

                score += math.log(((float(traininglist[trigram]) + smoothing) / (counttrigramtotal12(traininglist,mystring[i],mystring[i+1]) + (vocabularysize + 1) * smoothing)), 10)
            else:
                score=float('-inf')
        elif (((mystring[i].isalpha() ) or mystring[i]==" ")and  ((mystring[i + 1].isalpha()) or mystring[i+1]==" ") and ((mystring[i + 2].isalpha()) or mystring[i+2]==" ") and  (not (trigram in traininglist)) and (bigram in bigramlist) ):
            if((smoothing)>0 and (counttrigramtotal12(traininglist, mystring[i], mystring[i + 1]) + (vocabularysize + 1) * smoothing)>0 ):
                score += math.log(((smoothing) / (counttrigramtotal12(traininglist, mystring[i], mystring[i + 1]) + (vocabularysize + 1) * smoothing)), 10)
            else:
                score=float('-inf')
        elif ((mystring[i].isalpha() or mystring[i]==" ") and  ((mystring[i + 1].isalpha()) or mystring[i+1]==" ") and  ((mystring[i + 2].isalpha()) or mystring[i+2]==" ")  and (not (bigram in bigramlist) )):
            if((smoothing)>0 and ( (vocabularysize + 1) * smoothing)>0):

                score += math.log((smoothing) / ( (vocabularysize + 1) * smoothing), 10)
            else:
                score=float('-inf')

    score += math.log((classsize / totaldocs), 10)
    return score


def count4gramtotal123(dic,one,two,three):
    sum=0
    for i in dic:
        if(i[0]==one and i[1]==two and i[2]==three):
            sum+=float(dic[i])
    return sum


def calculatescoreisalpha4gram(mystring, smoothing, classsize, vocabularysize, totaldocs, traininglist,trigramlist):
    score = 0

    for i in range(len(mystring)-3):

        fourgram=mystring[i] + mystring[i + 1]+mystring[i+2]+mystring[i+3]
        trigram=mystring[i] + mystring[i + 1]+mystring[i+2]
        if (((mystring[i].isalpha()) or mystring[i]==" ") and ((mystring[i + 1].isalpha()) or mystring[i+1]==" ") and ((mystring[i + 2].isalpha() ) or mystring[i+2]==" ") and((mystring[i+3].isalpha()) or mystring[i+3]==" ") and (fourgram in traininglist)):
            if((float(traininglist[fourgram]) + smoothing) >0 and (count4gramtotal123(traininglist,mystring[i],mystring[i+1],mystring[i+2]) + (vocabularysize + 1) * smoothing)>0):

                score += math.log(((float(traininglist[fourgram]) + smoothing) / (count4gramtotal123(traininglist,mystring[i],mystring[i+1],mystring[i+2]) + (vocabularysize + 1) * smoothing)), 10)
            else:
                score=float('-inf')
        elif (((mystring[i].isalpha() ) or mystring[i]==" ")and  ((mystring[i + 1].isalpha()) or mystring[i+1]==" ") and  ((mystring[i + 2].isalpha()) or mystring[i+2]==" ") and((mystring[i+3].isalpha()) or mystring[i+3]==" ") and  (not (fourgram in traininglist)) and (trigram in trigramlist) ):
            if((smoothing)>0 and (count4gramtotal123(traininglist, mystring[i], mystring[i + 1],mystring[i+2]) + (vocabularysize + 1) * smoothing)>0 ):
                score += math.log(((smoothing) / (count4gramtotal123(traininglist, mystring[i], mystring[i + 1],mystring[i+2]) + (vocabularysize + 1) * smoothing)), 10)
            else:
                score=float('-inf')
        elif (((mystring[i].isalpha()) or mystring[i]==" ") and  ((mystring[i + 1].isalpha()) or mystring[i+1]==" ") and  ((mystring[i + 2].isalpha()) or mystring[i+2]==" ")  and ((mystring[i+3].isalpha()) or mystring[i+3]==" ") and (not (trigram in trigramlist) )):
            if((smoothing)>0 and ( (vocabularysize + 1) * smoothing)>0):

                score += math.log((smoothing) / ( (vocabularysize + 1) * smoothing), 10)
            else:
                score=float('-inf')

    score += math.log((classsize / totaldocs), 10)
    return score





def naivebayes(v,n,delta,train,test):
    nameoftracefile="trace_myModel"+str(v)+"_"+str(n)+"_"+str(delta)+".txt"
    confusionmatrix=np.array([[0] * 6] * 6)
    f1 = open(nameoftracefile, "w+", encoding="utf8")
    numcorrectclass=0
    results=[]
    correctbasque=0
    correctcatalan=0
    correctgalician=0
    correctspanish=0
    correctenglish=0
    correctportoguse=0

    falsepositivebasque=0
    falsepositivecatalan=0
    falsepositivegalician=0
    falsepositivespanish=0
    falsepositiveenglish=0
    falsepositiveportoguse=0


    falsenegativebasque=0
    falsenegativecatalan=0
    falsenegativegalician=0
    falsenegativespanish=0
    falsenegativeenglish=0
    falsenegativeportoguse=0

    indexm=0
    label=''
    label2=''
    scores=[0]*6
    if (v==1):
        results=trainv1(train,n)
    elif(v==2):
        results=trainv2(train,n)
    elif(v==3):
        results=trainv3(train,n)
    tweets=[]


    with open(test,encoding="utf8") as f:
        for line in f:
            tweets.append(line)
    copystring = [''] * (len(tweets))
    copytweets = [''] * (len(tweets))
    for i in range(len(tweets)):
        if (i < (len(tweets) - 1)):
            tweets[i] = tweets[i][:-1]
        copytweets[i] = tweets[i].split()
        index = tweets[i].index(copytweets[i][3])

        copystring[i] = tweets[i][index:]
        print(i)
        if(v==1 and n==1):
            scores[0] = calculatescores(copystring[i], delta, results[0], 26, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[6])
            scores[1] = calculatescores(copystring[i], delta, results[1], 26, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[7])
            scores[2] = calculatescores(copystring[i], delta, results[2], 26, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[8])
            scores[3] = calculatescores(copystring[i], delta, results[3], 26, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[9])
            scores[4] = calculatescores(copystring[i], delta, results[3], 26, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[10])
            scores[5] = calculatescores(copystring[i], delta, results[5], 26, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[11])
        elif(v==1 and n==2):
            scores[0] = calculatescorebigram(copystring[i], delta, results[0], 26, (results[0]+results[1]+results[2]+ results[3]+ results[4]+ results[5]), results[6])
            scores[1] = calculatescorebigram(copystring[i], delta, results[1], 26, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[7])
            scores[2] = calculatescorebigram(copystring[i], delta, results[2], 26, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[8])
            scores[3] = calculatescorebigram(copystring[i], delta, results[3], 26, (results[0]+results[1]+results[2]+results[3]+results[4]+results[5]),results[9])
            scores[4] = calculatescorebigram(copystring[i], delta, results[4], 26, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[10])
            scores[5] = calculatescorebigram(copystring[i], delta, results[5], 26, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[11])
        elif(v==1 and n==3):
            scores[0] = calculatescoretrigram(copystring[i], delta, results[0], 26, (results[0]+results[1]+results[2]+ results[3]+ results[4]+ results[5]), results[6])
            scores[1] = calculatescoretrigram(copystring[i], delta, results[1], 26, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[7])
            scores[2] = calculatescoretrigram(copystring[i], delta, results[2], 26, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[8])
            scores[3] = calculatescoretrigram(copystring[i], delta, results[3], 26, (results[0]+results[1]+results[2]+results[3]+results[4]+results[5]),results[9])
            scores[4] = calculatescoretrigram(copystring[i], delta, results[4], 26, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[10])
            scores[5] = calculatescoretrigram(copystring[i], delta, results[5], 26, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[11])
        elif(v==2 and n==1):
            scores[0] = calculatescorescase(copystring[i], delta, results[0], 52, (results[0]+results[1]+results[2]+ results[3]+ results[4]+ results[5]), results[6])
            scores[1] = calculatescorescase(copystring[i], delta, results[1], 52, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[7])
            scores[2] = calculatescorescase(copystring[i], delta, results[2], 52, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[8])
            scores[3] = calculatescorescase(copystring[i], delta, results[3], 52, (results[0]+results[1]+results[2]+results[3]+results[4]+results[5]),results[9])
            scores[4] = calculatescorescase(copystring[i], delta, results[4], 52, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[10])
            scores[5] = calculatescorescase(copystring[i], delta, results[5], 52, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[11])
        elif(v==2 and n==2):
            scores[0] = calculatescorebigramcase(copystring[i], delta, results[0], 52, (results[0]+results[1]+results[2]+ results[3]+ results[4]+ results[5]), results[6])
            scores[1] = calculatescorebigramcase(copystring[i], delta, results[1], 52, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[7])
            scores[2] = calculatescorebigramcase(copystring[i], delta, results[2], 52, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[8])
            scores[3] = calculatescorebigramcase(copystring[i], delta, results[3], 52, (results[0]+results[1]+results[2]+results[3]+results[4]+results[5]),results[9])
            scores[4] = calculatescorebigramcase(copystring[i], delta, results[4], 52, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[10])
            scores[5] = calculatescorebigramcase(copystring[i], delta, results[5], 52, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[11])
        elif(v==2 and n==3):
            scores[0] = calculatescoretrigramcase(copystring[i], delta, results[0], 52, (results[0]+results[1]+results[2]+ results[3]+ results[4]+ results[5]), results[6])
            scores[1] = calculatescoretrigramcase(copystring[i], delta, results[1], 52, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[7])
            scores[2] = calculatescoretrigramcase(copystring[i], delta, results[2], 52, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[8])
            scores[3] = calculatescoretrigramcase(copystring[i], delta, results[3], 52, (results[0]+results[1]+results[2]+results[3]+results[4]+results[5]),results[9])
            scores[4] = calculatescoretrigramcase(copystring[i], delta, results[4], 52, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[10])
            scores[5] = calculatescoretrigramcase(copystring[i], delta, results[5], 52, (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[11])
        elif(v==3 and n==1):
            scores[0] = calculatescoreisalpha(copystring[i], delta, results[0], results[12], (results[0]+  results[1]+  results[2]+  results[3]+  results[4]+  results[5]), results[6])
            scores[1] = calculatescoreisalpha(copystring[i], delta, results[1], results[13], (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[7])
            scores[2] = calculatescoreisalpha(copystring[i], delta, results[2], results[14], (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[8])
            scores[3] = calculatescoreisalpha(copystring[i], delta, results[3], results[15], (results[0]+  results[1]+  results[2]+  results[3]+  results[4]+  results[5]), results[9])
            scores[4] = calculatescoreisalpha(copystring[i], delta, results[4], results[16], (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[10])
            scores[5] = calculatescoreisalpha(copystring[i], delta, results[5], results[17], (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[11])
        elif(v==3 and n==2):

            scores[0] = calculatescoreisalphabigram(copystring[i], delta, results[0], results[12], (results[0] +  results[1] +  results[2] +  results[3]+  results[4] +  results[5]), results[6])
            scores[1] = calculatescoreisalphabigram(copystring[i], delta, results[1], results[13], (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[7])
            scores[2] = calculatescoreisalphabigram(copystring[i], delta, results[2], results[14], (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[8])
            scores[3] = calculatescoreisalphabigram(copystring[i], delta, results[3], results[15], (results[0] +  results[1] +  results[2] +  results[3]+  results[4] +  results[5]), results[9])
            scores[4] = calculatescoreisalphabigram(copystring[i], delta, results[4], results[16], (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[10])
            scores[5] = calculatescoreisalphabigram(copystring[i], delta, results[5], results[17], (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[11])
        elif(v==3 and n==3):
            scores[0] = calculatescoreisalphatrigram(copystring[i], delta, results[0], results[12], (results[0] +  results[1]+  results[2] +  results[3]+  results[4] +  results[5]), results[6],results[18])
            scores[1] = calculatescoreisalphatrigram(copystring[i], delta, results[1], results[13], (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[7],results[19])
            scores[2] = calculatescoreisalphatrigram(copystring[i], delta, results[2], results[14], (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[8],results[20])
            scores[3] = calculatescoreisalphatrigram(copystring[i], delta, results[3], results[15], (results[0] +  results[1]+  results[2] +  results[3]+  results[4] +  results[5]), results[9],results[21])
            scores[4] = calculatescoreisalphatrigram(copystring[i], delta, results[4], results[16], (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[10],results[22])
            scores[5] = calculatescoreisalphatrigram(copystring[i], delta, results[5], results[17], (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[11],results[23])

        elif(v==3 and n==4):
            scores[0] = calculatescoreisalpha4gram(copystring[i], delta, results[0], results[12], (results[0] +  results[1]+  results[2] +  results[3]+  results[4] +  results[5]), results[6],results[18])
            scores[1] = calculatescoreisalpha4gram(copystring[i], delta, results[1], results[13], (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[7],results[19])
            scores[2] = calculatescoreisalpha4gram(copystring[i], delta, results[2], results[14], (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[8],results[20])
            scores[3] = calculatescoreisalpha4gram(copystring[i], delta, results[3], results[15], (results[0] +  results[1]+  results[2] +  results[3]+  results[4] +  results[5]), results[9],results[21])
            scores[4] = calculatescoreisalpha4gram(copystring[i], delta, results[4], results[16], (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[10],results[22])
            scores[5] = calculatescoreisalpha4gram(copystring[i], delta, results[5], results[17], (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[11],results[23])

        indexm=0

        for j in range(6):
            if(scores[j]>scores[indexm]):
                indexm=j


        if(indexm==0):
            label='eu'
        elif(indexm==1):
            label='ca'
        elif(indexm==2):
            label='gl'
        elif(indexm==3):
            label='es'
        elif(indexm==4):
            label='en'
        elif(indexm==5):
            label='pt'
        if(label==copytweets[i][2]):
            label2="correct"

            numcorrectclass+=1
            if(label=='eu'):
                correctbasque+=1
                confusionmatrix[0][0]+=1
            elif(label=='ca'):
                correctcatalan+=1
                confusionmatrix[1][1] += 1
            elif(label=='gl'):
                correctgalician+=1
                confusionmatrix[2][2] += 1
            elif(label=='es'):
                correctspanish+=1
                confusionmatrix[3][3] += 1
            elif(label=='en'):
                correctenglish+=1
                confusionmatrix[4][4] += 1
            elif(label=='pt'):
                correctportoguse+=1
                confusionmatrix[5][5] += 1
        else:
            label2="wrong"
            if(label=='eu'):
                falsepositivebasque+=1
            elif(label=='ca'):
                falsepositivecatalan+=1
            elif(label=='gl'):
                falsepositivegalician+=1
            elif(label=='es'):
                falsepositivespanish+=1
            elif(label=='en'):
                falsepositiveenglish+=1
            elif(label=='pt'):
                falsepositiveportoguse+=1

            if(copytweets[i][2]=='eu'):
                falsenegativebasque+=1
                if(label=="ca"):
                    confusionmatrix[0][1]+=1
                elif (label=="gl"):
                    confusionmatrix[0][2] += 1
                elif(label=="es"):
                    confusionmatrix[0][3] += 1
                elif(label=="en"):
                    confusionmatrix[0][4]+=1
                elif(label=="pt"):
                    confusionmatrix[0][5]+=1



            elif(copytweets[i][2]=='ca'):
                if (label == "eu"):
                    confusionmatrix[1][0] += 1
                elif (label == "gl"):
                    confusionmatrix[1][2] += 1
                elif (label == "es"):
                    confusionmatrix[1][3] += 1
                elif (label=="en"):
                    confusionmatrix[1][4] += 1
                elif (label=="pt"):
                    confusionmatrix[1][5] += 1
                falsenegativecatalan+=1

            elif(copytweets[i][2]=='gl'):
                falsenegativegalician+=1
                if (label == "eu"):
                    confusionmatrix[2][0] += 1
                elif (label == "ca"):
                    confusionmatrix[2][1] += 1
                elif (label == "es"):
                    confusionmatrix[2][3] += 1
                elif (label=="en"):
                    confusionmatrix[2][4] += 1
                elif (label=="pt"):
                    confusionmatrix[2][5] += 1

            elif(copytweets[i][2]=='es'):
                if (label == "eu"):
                    confusionmatrix[3][0] += 1
                elif (label == "ca"):
                    confusionmatrix[3][1] += 1
                elif (label == "gl"):
                    confusionmatrix[3][2] += 1
                elif (label=="en"):
                    confusionmatrix[3][4] += 1
                elif (label=="pt"):
                    confusionmatrix[3][5] += 1
                falsenegativespanish+=1
            elif(copytweets[i][2]=='en'):
                falsenegativeenglish+=1
                if (label == "eu"):
                    confusionmatrix[4][0] += 1
                elif (label == "ca"):
                    confusionmatrix[4][1] += 1
                elif (label == "gl"):
                    confusionmatrix[4][2] += 1
                elif (label=="es"):
                    confusionmatrix[4][3] += 1
                elif (label=="pt"):
                    confusionmatrix[4][5] += 1
            elif(copytweets[i][2]=='pt'):
                falsenegativeportoguse+=1
                if (label == "eu"):
                    confusionmatrix[5][0] += 1
                elif (label == "ca"):
                    confusionmatrix[5][1] += 1
                elif (label == "gl"):
                    confusionmatrix[5][2] += 1
                elif (label=="es"):
                    confusionmatrix[5][3] += 1
                elif (label=="en"):
                    confusionmatrix[5][4] += 1


        f1.write(copytweets[i][0]+"  "+label+"  "+"{:.2e}".format((scores[indexm]))+"  "+copytweets[i][2]+"  "+label2+"\n")

    f1.close()
    accuracy=(numcorrectclass/len(tweets))


    if((correctbasque+falsepositivebasque) > 0):
        precisionbasque=correctbasque/(correctbasque+falsepositivebasque)
    else:
        precisionbasque="undefined"

    if((correctcatalan+falsepositivecatalan)>0):
        precisioncatalan=correctcatalan/(correctcatalan+falsepositivecatalan)
    else:
        precisioncatalan="undefined"

    if((correctgalician+falsepositivegalician)>0):
        precisiongalician=correctgalician/(correctgalician+falsepositivegalician)
    else:
        precisiongalician="undefined"

    if ((correctspanish+falsepositivespanish)>0):
        precisionspanish=correctspanish/(correctspanish+falsepositivespanish)
    else:
        precisionspanish="undefined"

    if(correctenglish+falsepositiveenglish>0):
        precisionenglish=correctenglish/(correctenglish+falsepositiveenglish)
    else:
        precisionenglish="undefined"

    if((correctportoguse+falsepositiveportoguse)>0):
        precisionportoguse=correctportoguse/(correctportoguse+falsepositiveportoguse)
    else:
        precisionportoguse="undefined"




    if((correctbasque+falsenegativebasque)>0):
        recallbasque = correctbasque/(correctbasque+falsenegativebasque)
    else:
        recallbasque="undefined"
    if((correctcatalan+falsenegativecatalan)>0):
        recallcatalan = correctcatalan/(correctcatalan+falsenegativecatalan)
    else:
        recallcatalan="undefined"
    if((correctgalician+falsenegativegalician)>0):
        recallgalician = correctgalician/(correctgalician+falsenegativegalician)
    else:
        recallgalician="undefined"
    if((correctspanish+falsenegativespanish)>0):
        recallspanish = correctspanish/(correctspanish+falsenegativespanish)
    else:
        recallspanish="undefined"
    if((correctenglish+falsenegativeenglish)>0):
        recallenglish = correctenglish/(correctenglish+falsenegativeenglish)
    else:
        recallenglish="undefined"
    if((correctportoguse+falsenegativeportoguse)>0):
        recallportoguse = correctportoguse/(correctportoguse+falsenegativeportoguse)
    else:
        recallportoguse="undefined"



    testbasque=correctbasque+falsenegativebasque
    testcatalan=correctcatalan+falsenegativecatalan
    testgalician=correctgalician+falsenegativegalician
    testspanish=correctspanish+falsenegativespanish
    testenglish=correctenglish+falsenegativeenglish
    testportoguse=correctportoguse+falsenegativeportoguse
    totaltest=testbasque+testcatalan+testgalician+testspanish+testenglish+testportoguse

    macrof1=0
    waveragef1=0
    numdefined=0

    if(recallbasque!= "undefined" and precisionbasque!="undefined"):
        if((recallbasque+precisionbasque)>0):
            f1basque=(2*precisionbasque*recallbasque)/(recallbasque+precisionbasque)
            macrof1+=f1basque
            waveragef1+=testbasque*f1basque
            numdefined+=1
        else:
            f1basque="undefined"
    else:
        f1basque = "undefined"

    if(recallcatalan!="undefined" and precisioncatalan!="undefined"):
        if((recallcatalan+precisioncatalan)>0):
            f1catalan=(2*precisioncatalan*recallcatalan)/(recallcatalan+precisioncatalan)
            macrof1+=f1catalan
            waveragef1+=testcatalan*f1catalan
            numdefined+=1
        else:
            f1catalan="undefined"
    else:
        f1catalan = "undefined"

    if(recallgalician!="undefined" and precisiongalician!="undefined"):
        if((recallgalician+precisiongalician)>0):
            f1galician=(2*precisiongalician*recallgalician)/(recallgalician+precisiongalician)
            macrof1+=f1galician
            waveragef1+=testgalician*f1galician
            numdefined+=1
        else:
            f1galician="undefined"
    else:
        f1galician = "undefined"

    if(recallspanish!="undefined" and precisionspanish!="undefined"):
        if((recallspanish+precisionspanish)>0):
            f1spanish=(2*precisionspanish*recallspanish)/(recallspanish+precisionspanish)
            macrof1+=f1spanish
            waveragef1+=testspanish*f1spanish
            numdefined+=1
        else:
            f1spanish="undefined"
    else:
        f1spanish = "undefined"

    if(recallenglish!="undefined" and precisionenglish!="undefined"):
        if((recallenglish+precisionenglish)>0):
            f1english=(2*precisionenglish*recallenglish)/(recallenglish+precisionenglish)
            macrof1+=f1english
            waveragef1+=testenglish*f1english
            numdefined+=1
        else:
            f1english="undefined"
    else:
        f1english = "undefined"

    if(recallportoguse!="undefined" and precisionportoguse!="undefined"):
        if((recallportoguse+precisionportoguse)>0):
            f1portoguse=(2*precisionportoguse*recallportoguse)/(recallportoguse+precisionportoguse)
            macrof1+=f1portoguse
            waveragef1+=testportoguse*f1portoguse
            numdefined+=1
        else:
            f1portoguse="undefined"
    else:
        f1portoguse = "undefined"

    macrof1=  (macrof1) / 6
    waveragef1=  (waveragef1) / (testbasque+testcatalan+testgalician+testspanish+testenglish+testportoguse)


    nameoffile2="eval_myModel"+str(v)+"_"+str(n)+"_"+str(delta)+".txt"
    f2 = open(nameoffile2, "w+", encoding="utf8")
    f2.write(str(accuracy)+"\n")
    f2.write(str(precisionbasque)+"  "+str(precisioncatalan)+"  "+str(precisiongalician)+"  "+str(precisionspanish)+"  "+str(precisionenglish)+"  "+str(precisionportoguse)+"\n")
    f2.write(str(recallbasque) + "  " + str(recallcatalan) + "  " + str(recallgalician) + "  " + str(recallspanish) + "  " + str(recallenglish) + "  " + str(recallportoguse) + "\n")
    f2.write(str(f1basque) + "  " + str(f1catalan) + "  " + str(f1galician) + "  " + str(f1spanish) + "  " + str(f1english) + "  " + str(f1portoguse) + "\n")
    f2.write(str(macrof1)+"  "+str(waveragef1))
    print(confusionmatrix)



naivebayes(3,3,0.4,"training-tweets.txt","test-tweets-given.txt")




