import numpy as np
import math

#a method to sum all elements of a list
def totalcountlist(mylist):
    sum=0
    for i in range(len(mylist)):
        sum+=float(mylist[i])
    return sum

# creating unigram only lower case letters a-z
def createcountsoflowercase(mystring):
    mystring=mystring.lower()
    mylist=[0]*26
    for char in mystring:
        if(ord(char)>=97 and ord(char)<=122):
            mylist[ord(char)-97]+=1
    return mylist

# creating unigrams lower case and upper case
def createcountsofloweranduppercase(mystring):
    mylist=[0]*52
    for char in mystring:
        if(ord(char)>=65 and ord(char)<=90):
            mylist[ord(char)-39]+=1
        if (ord(char) >= 97 and ord(char) <= 122):
            mylist[ord(char) - 97] += 1
    return mylist


# creating bigrams lower case a-z
def createbigramlower(mystring):
    mystring = mystring.lower()
    mylist=np.array([[0]*26]*26)
    for i in range(len(mystring)-1):
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and ord(mystring[i+1]) >= 97 and ord(mystring[i+1]) <= 122):
            mylist[ord(mystring[i])-97][ord(mystring[i+1])-97]+=1
    return mylist

# creating trigram lower case a-z
def createtrigramlower(mystring):
    mystring = mystring.lower()
    mylist=np.array([[[0]*26]*26]*26)
    for i in range(len(mystring)-2):
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and ord(mystring[i+1]) >= 97 and ord(mystring[i+1]) <= 122 and ord(mystring[i+2]) >= 97 and ord(mystring[i+2]) <= 122):
            mylist[ord(mystring[i])-97][ord(mystring[i+1])-97][ord(mystring[i+2])-97]+=1
    return mylist

# creating bigrams a-z and A-Z
def createbigram(mystring):
    mylist=np.array([[0]*52]*52)
    for i in range(len(mystring)-1):
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and ord(mystring[i+1]) >= 97 and ord(mystring[i+1]) <= 122):
            mylist[ord(mystring[i])-97][ord(mystring[i+1])-97]+=1
        if ((ord(mystring[i]) >= 65 and ord(mystring[i]) <= 90) and ord(mystring[i + 1]) >= 65 and ord(mystring[i + 1]) <= 90):
            mylist[ord(mystring[i]) - 39][ord(mystring[i + 1]) - 39] += 1
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and ord(mystring[i + 1]) >= 65 and ord(mystring[i + 1]) <= 90):
                mylist[ord(mystring[i]) - 97][ord(mystring[i + 1]) - 39] += 1
        if ((ord(mystring[i]) >= 65 and ord(mystring[i]) <= 90) and ord(mystring[i + 1]) >= 97 and ord(mystring[i + 1]) <= 122):
                    mylist[ord(mystring[i]) - 39][ord(mystring[i + 1]) - 97] += 1
    return mylist

# CREATING TRIGRAMS A-Z AND a-z
def createtrigram(mystring):
    mylist=np.array([[[0]*52]*52]*52)
    for i in range(len(mystring)-2):
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and ord(mystring[i+1]) >= 97 and ord(mystring[i+1]) <= 122 and ord(mystring[i+2]) >= 97 and ord(mystring[i+2]) <= 122):
            mylist[ord(mystring[i])-97][ord(mystring[i+1])-97][ord(mystring[i+2])-97]+=1
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and ord(mystring[i + 1]) >= 97 and ord(mystring[i + 1]) <= 122 and ord(mystring[i+2]) >= 65 and ord(mystring[i+2]) <= 90):
            mylist[ord(mystring[i]) - 97][ord(mystring[i + 1]) - 97][ord(mystring[i+2])-39] += 1
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and ord(mystring[i + 1]) >= 65 and ord(mystring[i + 1]) <= 90 and ord(mystring[i+2]) >= 97 and ord(mystring[i+2]) <= 122):
            mylist[ord(mystring[i]) - 97][ord(mystring[i + 1]) - 39][ord(mystring[i+2])-97]  += 1
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and ord(mystring[i + 1]) >= 65 and ord(mystring[i + 1]) <= 90 and ord(mystring[i + 2]) >= 65 and ord(mystring[i + 2]) <= 90):
            mylist[ord(mystring[i]) - 97][ord(mystring[i + 1]) - 39][ord(mystring[i + 2]) - 39] += 1
        if ((ord(mystring[i]) >= 65 and ord(mystring[i]) <= 90) and ord(mystring[i+1]) >= 97 and ord(mystring[i+1]) <= 122 and ord(mystring[i+2]) >= 97 and ord(mystring[i+2]) <= 122):
            mylist[ord(mystring[i])-39][ord(mystring[i+1])-97][ord(mystring[i+2])-97]+=1
        if ((ord(mystring[i]) >= 65 and ord(mystring[i]) <= 90) and ord(mystring[i + 1]) >= 97 and ord(mystring[i + 1]) <= 122 and ord(mystring[i+2]) >= 65 and ord(mystring[i+2]) <= 90):
            mylist[ord(mystring[i]) - 39][ord(mystring[i + 1]) - 97][ord(mystring[i+2])-39]+= 1
        if ((ord(mystring[i]) >= 65 and ord(mystring[i]) <= 90) and ord(mystring[i + 1]) >= 65 and ord(mystring[i + 1]) <= 90 and ord(mystring[i+2]) >= 97 and ord(mystring[i+2]) <= 122):
            mylist[ord(mystring[i]) - 39][ord(mystring[i + 1]) - 39][ord(mystring[i+2])-97]+= 1
        if ((ord(mystring[i]) >= 65 and ord(mystring[i]) <= 90) and ord(mystring[i + 1]) >= 65 and ord(mystring[i + 1]) <= 90 and ord(mystring[i + 2]) >= 65 and ord(mystring[i + 2]) <= 90):
            mylist[ord(mystring[i]) - 39][ord(mystring[i + 1]) - 39][ord(mystring[i + 2]) - 39] += 1


    return mylist


# creating unigram with isalpha
def createcountisalpha(mystring):
        mydictionary={}
        for char in mystring:
            if (char.isalpha()):
                if(not (char in mydictionary)):
                    mydictionary[char]=1
                elif(char in mydictionary):
                    mydictionary[char]=(float(mydictionary[char])+1)
        return mydictionary

#creating bigram with isalpha
def createbigramisalpha(mystring):
    mybigramdic={}
    for i in range(len(mystring)-1):
        if(mystring[i].isalpha() and mystring[i+1].isalpha()):
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
        if(mystring[i].isalpha() and mystring[i+1].isalpha() and mystring[i+2].isalpha()):
            trigramkey=(mystring[i]+mystring[i+1]+mystring[i+2])
            if(not(trigramkey in mytrigramdic)):
                mytrigramdic[trigramkey]=1
            elif(trigramkey in mytrigramdic):
                mytrigramdic[trigramkey]=float(mytrigramdic[trigramkey])+1
    return mytrigramdic


def create4gramisalpha(mystring):
    my4gramdic={}
    for i in range(len(mystring)-3):
        if(mystring[i].isalpha() and mystring[i+1].isalpha() and mystring[i+2].isalpha() and mystring[i+3].isalpha()):
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


def trainv1(train,n):
    tweets = []
    numtweetbasque = 0
    numtweetcatalan = 0
    numtweetgalician = 0
    numtweetspanish = 0
    numtweetenglish = 0
    numtweetportoguse = 0

    countbasque = [0] * 26
    countcatalan = [0] * 26
    countgalician = [0] * 26
    countspanish = [0] * 26
    countenglish = [0] * 26
    countportoguse = [0] * 26

    countbasquebigram = np.array([[0] * 26] * 26)
    countcatalanbigram = np.array([[0] * 26] * 26)
    countgalicianbigram = np.array([[0] * 26] * 26)
    countspanishbigram = np.array([[0] * 26] * 26)
    countenglishbigram = np.array([[0] * 26] * 26)
    countportogusebigram = np.array([[0] * 26] * 26)

    countbasquetrigram = np.array([[[0] * 26] * 26] * 26)
    countcatalantrigram = np.array([[[0] * 26] * 26] * 26)
    countgaliciantrigram = np.array([[[0] * 26] * 26] * 26)
    countspanishtrigram = np.array([[[0] * 26] * 26] * 26)
    countenglishtrigram = np.array([[[0] * 26] * 26] * 26)
    countportogusetrigram = np.array([[[0] * 26] * 26] * 26)
    results = []
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
                countbasque += np.array(createcountsoflowercase(copystring[i]))
                numtweetbasque += 1
            elif (copytweets[i][2] == 'ca'):
                countcatalan += np.array(createcountsoflowercase(copystring[i]))
                numtweetcatalan += 1
            elif (copytweets[i][2] == 'gl'):
                countgalician += np.array(createcountsoflowercase(copystring[i]))
                numtweetgalician += 1
            elif (copytweets[i][2] == 'es'):
                countspanish += np.array(createcountsoflowercase(copystring[i]))
                numtweetspanish += 1
            elif (copytweets[i][2] == 'en'):
                countenglish += np.array(createcountsoflowercase(copystring[i]))
                numtweetenglish += 1
            elif (copytweets[i][2] == 'pt'):
                countportoguse += np.array(createcountsoflowercase(copystring[i]))
                numtweetportoguse += 1
        elif(n==2):

            if (copytweets[i][2] == 'eu'):
                countbasquebigram += np.array(createbigramlower(copystring[i]))
                numtweetbasque += 1
            elif (copytweets[i][2] == 'ca'):
                countcatalanbigram += np.array(createbigramlower(copystring[i]))
                numtweetcatalan += 1
            elif (copytweets[i][2] == 'gl'):
                countgalicianbigram += np.array(createbigramlower(copystring[i]))
                numtweetgalician += 1
            elif (copytweets[i][2] == 'es'):
                countspanishbigram += np.array(createbigramlower(copystring[i]))
                numtweetspanish += 1
            elif (copytweets[i][2] == 'en'):
                countenglishbigram += np.array(createbigramlower(copystring[i]))
                numtweetenglish += 1
            elif (copytweets[i][2] == 'pt'):
                countportogusebigram += np.array(createbigramlower(copystring[i]))
                numtweetportoguse += 1
        elif(n==3):

            if (copytweets[i][2] == 'eu'):
                countbasquetrigram += np.array(createtrigramlower(copystring[i]))
                numtweetbasque += 1
            elif (copytweets[i][2] == 'ca'):
                countcatalantrigram += np.array(createtrigramlower(copystring[i]))
                numtweetcatalan += 1
            elif (copytweets[i][2] == 'gl'):
                countgaliciantrigram += np.array(createtrigramlower(copystring[i]))
                numtweetgalician += 1
            elif (copytweets[i][2] == 'es'):
                countspanishtrigram += np.array(createtrigramlower(copystring[i]))
                numtweetspanish += 1
            elif (copytweets[i][2] == 'en'):
                countenglishtrigram += np.array(createtrigramlower(copystring[i]))
                numtweetenglish += 1
            elif (copytweets[i][2] == 'pt'):
                countportogusetrigram += np.array(createtrigramlower(copystring[i]))
                numtweetportoguse += 1

    if(n==1):
        results.append(numtweetbasque)
        results.append(numtweetcatalan)
        results.append(numtweetgalician)
        results.append(numtweetspanish)
        results.append(numtweetenglish)
        results.append(numtweetportoguse)

        results.append(countbasque)
        results.append(countcatalan)
        results.append(countgalician)
        results.append(countspanish)
        results.append(countenglish)
        results.append(countportoguse)

    elif(n==2):
        results.append(numtweetbasque)
        results.append(numtweetcatalan)
        results.append(numtweetgalician)
        results.append(numtweetspanish)
        results.append(numtweetenglish)
        results.append(numtweetportoguse)

        results.append(countbasquebigram)
        results.append(countcatalanbigram)
        results.append(countgalicianbigram)
        results.append(countspanishbigram)
        results.append(countenglishbigram)
        results.append(countportogusebigram)

    elif(n==3):

        results.append(numtweetbasque)
        results.append(numtweetcatalan)
        results.append(numtweetgalician)
        results.append(numtweetspanish)
        results.append(numtweetenglish)
        results.append(numtweetportoguse)

        results.append(countbasquetrigram)
        results.append(countcatalantrigram)
        results.append(countgaliciantrigram)
        results.append(countspanishtrigram)
        results.append(countenglishtrigram)
        results.append(countportogusetrigram)

    return results



def trainv2(train,n):
    tweets = []
    numtweetbasque = 0
    numtweetcatalan = 0
    numtweetgalician = 0
    numtweetspanish = 0
    numtweetenglish = 0
    numtweetportoguse = 0

    countbasquecasesensitive=[0]*52
    countcatalancasesensitive = [0] * 52
    countgaliciancasesensitive = [0] * 52
    countspanishcasesensitive = [0] * 52
    countenglishcasesensitive = [0] * 52
    countportogusecasesensitive = [0] * 52

    countbasquebigramcase = np.array([[0] * 52] * 52)
    countcatalanbigramcase = np.array([[0] * 52] * 52)
    countgalicianbigramcase = np.array([[0] * 52] * 52)
    countspanishbigramcase = np.array([[0] * 52] * 52)
    countenglishbigramcase = np.array([[0] * 52] * 52)
    countportogusebigramcase = np.array([[0] * 52] * 52)

    countbasquetrigramcase = np.array([[[0]*52]*52]*52)
    countcatalantrigramcase = np.array([[[0]*52]*52]*52)
    countgaliciantrigramcase = np.array([[[0]*52]*52]*52)
    countspanishtrigramcase = np.array([[[0]*52]*52]*52)
    countenglishtrigramcase = np.array([[[0]*52]*52]*52)
    countportogusetrigramcase = np.array([[[0]*52]*52]*52)

    results = []

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
                countbasquecasesensitive += np.array(createcountsofloweranduppercase(copystring[i]))
                numtweetbasque += 1
            elif (copytweets[i][2] == 'ca'):
                countcatalancasesensitive += np.array(createcountsofloweranduppercase(copystring[i]))
                numtweetcatalan += 1
            elif (copytweets[i][2] == 'gl'):
                countgaliciancasesensitive += np.array(createcountsofloweranduppercase(copystring[i]))
                numtweetgalician += 1
            elif (copytweets[i][2] == 'es'):
                countspanishcasesensitive += np.array(createcountsofloweranduppercase(copystring[i]))
                numtweetspanish += 1
            elif (copytweets[i][2] == 'en'):
                countenglishcasesensitive += np.array(createcountsofloweranduppercase(copystring[i]))
                numtweetenglish += 1
            elif (copytweets[i][2] == 'pt'):
                countportogusecasesensitive += np.array(createcountsofloweranduppercase(copystring[i]))
                numtweetportoguse += 1
        elif(n==2):

            if (copytweets[i][2] == 'eu'):
                countbasquebigramcase += np.array(createbigram(copystring[i]))
                numtweetbasque += 1
            elif (copytweets[i][2] == 'ca'):
                countcatalanbigramcase += np.array(createbigram(copystring[i]))
                numtweetcatalan += 1
            elif (copytweets[i][2] == 'gl'):
                countgalicianbigramcase += np.array(createbigram(copystring[i]))
                numtweetgalician += 1
            elif (copytweets[i][2] == 'es'):
                countspanishbigramcase += np.array(createbigram(copystring[i]))
                numtweetspanish += 1
            elif (copytweets[i][2] == 'en'):
                countenglishbigramcase += np.array(createbigram(copystring[i]))
                numtweetenglish += 1
            elif (copytweets[i][2] == 'pt'):
                countportogusebigramcase += np.array(createbigram(copystring[i]))
                numtweetportoguse += 1
        elif(n==3):

            if (copytweets[i][2] == 'eu'):
                countbasquetrigramcase += np.array(createtrigram(copystring[i]))
                numtweetbasque += 1
            elif (copytweets[i][2] == 'ca'):
                countcatalantrigramcase += np.array(createtrigram(copystring[i]))
                numtweetcatalan += 1
            elif (copytweets[i][2] == 'gl'):
                countgaliciantrigramcase += np.array(createtrigram(copystring[i]))
                numtweetgalician += 1
            elif (copytweets[i][2] == 'es'):
                countspanishtrigramcase += np.array(createtrigram(copystring[i]))
                numtweetspanish += 1
            elif (copytweets[i][2] == 'en'):
                countenglishtrigramcase += np.array(createtrigram(copystring[i]))
                numtweetenglish += 1
            elif (copytweets[i][2] == 'pt'):
                countportogusetrigramcase += np.array(createtrigram(copystring[i]))
                numtweetportoguse += 1

    if(n==1):
        results.append(numtweetbasque)
        results.append(numtweetcatalan)
        results.append(numtweetgalician)
        results.append(numtweetspanish)
        results.append(numtweetenglish)
        results.append(numtweetportoguse)

        results.append(countbasquecasesensitive)
        results.append(countcatalancasesensitive)
        results.append(countgaliciancasesensitive)
        results.append(countspanishcasesensitive)
        results.append(countenglishcasesensitive)
        results.append(countportogusecasesensitive)

    elif(n==2):
        results.append(numtweetbasque)
        results.append(numtweetcatalan)
        results.append(numtweetgalician)
        results.append(numtweetspanish)
        results.append(numtweetenglish)
        results.append(numtweetportoguse)

        results.append(countbasquebigramcase)
        results.append(countcatalanbigramcase)
        results.append(countgalicianbigramcase)
        results.append(countspanishbigramcase)
        results.append(countenglishbigramcase)
        results.append(countportogusebigramcase)

    elif(n==3):
        results.append(numtweetbasque)
        results.append(numtweetcatalan)
        results.append(numtweetgalician)
        results.append(numtweetspanish)
        results.append(numtweetenglish)
        results.append(numtweetportoguse)

        results.append(countbasquetrigramcase)
        results.append(countcatalantrigramcase)
        results.append(countgaliciantrigramcase)
        results.append(countspanishtrigramcase)
        results.append(countenglishtrigramcase)
        results.append(countportogusetrigramcase)

    return results

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



def calculatescorebigram(mystring,smoothing,classsize,vocabularysize,totaldocs,traininglist):
    score=0
    for i in range(len(mystring)-1):
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and (ord(mystring[i+1]) >= 97 and ord(mystring[i+1]) <= 122)):
            if((traininglist[ord(mystring[i])-97][ord(mystring[i+1])-97]+smoothing)>0 and ((totalcountlist(traininglist[ord(mystring[i])-97]))+smoothing*vocabularysize) >0):
                score+=math.log(((traininglist[ord(mystring[i])-97][ord(mystring[i+1])-97]+smoothing)/((totalcountlist(traininglist[ord(mystring[i])-97]))+smoothing*vocabularysize)),10)
            else:
                score=(-99999999)
    score+=math.log((classsize/totaldocs),10)
    return score


def calculatescoretrigram(mystring, smoothing, classsize, vocabularysize, totaldocs, traininglist):
    score = 0
    for i in range(len(mystring) - 2):
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and ord(mystring[i+1]) >= 97 and ord(mystring[i+1]) <= 122 and ord(mystring[i+2]) >= 97 and ord(mystring[i+2]) <= 122):
            if((traininglist[ord(mystring[i])-97][ord(mystring[i+1])-97][ord(mystring[i+2])-97]+smoothing)>0 and ((totalcountlist(traininglist[ord(mystring[i])-97][ord(mystring[i+1])-97]))+smoothing*vocabularysize)>0 ):


                score+=math.log(((traininglist[ord(mystring[i])-97][ord(mystring[i+1])-97][ord(mystring[i+2])-97]+smoothing)/((totalcountlist(traininglist[ord(mystring[i])-97][ord(mystring[i+1])-97]))+smoothing*vocabularysize)),10)
            else:
                score=(-99999999)
    score+=math.log((classsize/totaldocs),10)
    return score

def calculatescorescase(mystring,smoothing,classsize,vocabularysize,totaldocs,traininglist):
    score=0
    for i in range(len(mystring)):
        if((ord(mystring[i])>=97 and ord(mystring[i])<=122)):
            if((traininglist[ord(mystring[i])-97]+smoothing)>0 and (totalcountlist(traininglist)+vocabularysize*smoothing)>0):
                score+=math.log(((traininglist[ord(mystring[i])-97]+smoothing)/(totalcountlist(traininglist)+vocabularysize*smoothing)),10)
            else:
                score=(-99999999)
        elif ((ord(mystring[i])>=65 and ord(mystring[i])<=90)):
            if((traininglist[ord(mystring[i]) - 39]+smoothing) >0 and (totalcountlist(traininglist)+vocabularysize * smoothing)>0 ):
                score += math.log(((traininglist[ord(mystring[i]) - 39]+smoothing) / (totalcountlist(traininglist)+vocabularysize * smoothing)), 10)
            else:
                score=(-99999999)

    score+=math.log((classsize/totaldocs),10)
    return score

def calculatescorebigramcase(mystring,smoothing,classsize,vocabularysize,totaldocs,traininglist):
    score=0
    for i in range(len(mystring)-1):
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and (ord(mystring[i+1]) >= 97 and ord(mystring[i+1]) <= 122)):
            if((traininglist[ord(mystring[i])-97][ord(mystring[i+1])-97]+smoothing)>0 and ((totalcountlist(traininglist[ord(mystring[i])-97]))+smoothing*vocabularysize)>0 ):
                score+=math.log(((traininglist[ord(mystring[i])-97][ord(mystring[i+1])-97]+smoothing)/((totalcountlist(traininglist[ord(mystring[i])-97]))+smoothing*vocabularysize)),10)
            else:
                score=(-99999999)
        if ((ord(mystring[i]) >= 65 and ord(mystring[i]) <= 90) and ord(mystring[i + 1]) >= 65 and ord(mystring[i + 1]) <= 90):
            if( (traininglist[ord(mystring[i]) - 39][ord(mystring[i + 1]) - 39] + smoothing)>0 and ((totalcountlist(traininglist[ord(mystring[i])-39]))+smoothing*vocabularysize)>0 ):
                score+=math.log(((traininglist[ord(mystring[i]) - 39][ord(mystring[i + 1]) - 39] + smoothing)/((totalcountlist(traininglist[ord(mystring[i])-39]))+smoothing*vocabularysize)),10)
            else:
                score=(-99999999)
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and ord(mystring[i + 1]) >= 65 and ord(mystring[i + 1]) <= 90):
            if((traininglist[ord(mystring[i]) - 97][ord(mystring[i + 1]) - 39] +smoothing)>0 and  ((totalcountlist(traininglist[ord(mystring[i])-97]))+smoothing*vocabularysize)>0):
                score += math.log(((traininglist[ord(mystring[i]) - 97][ord(mystring[i + 1]) - 39] +smoothing)/((totalcountlist(traininglist[ord(mystring[i])-97]))+smoothing*vocabularysize)),10)
            else:
                score=(-99999999)
        if ((ord(mystring[i]) >= 65 and ord(mystring[i]) <= 90) and ord(mystring[i + 1]) >= 97 and ord(mystring[i + 1]) <= 122):
            if((traininglist[ord(mystring[i]) - 39][ord(mystring[i + 1]) - 97] +smoothing)>0 and ((totalcountlist(traininglist[ord(mystring[i])-39]))+smoothing*vocabularysize)>0 ):
                score += math.log(((traininglist[ord(mystring[i]) - 39][ord(mystring[i + 1]) - 97] +smoothing)/((totalcountlist(traininglist[ord(mystring[i])-39]))+smoothing*vocabularysize)),10)
            else:
                score=(-99999999)
    score+=math.log((classsize/totaldocs),10)
    return score

def calculatescoretrigramcase(mystring, smoothing, classsize, vocabularysize, totaldocs, traininglist):
    score = 0
    for i in range(len(mystring) - 2):
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and ord(mystring[i+1]) >= 97 and ord(mystring[i+1]) <= 122 and ord(mystring[i+2]) >= 97 and ord(mystring[i+2]) <= 122):
            if((traininglist[ord(mystring[i]) - 97][ord(mystring[i + 1]) - 97][ord(mystring[i + 2]) - 97] + smoothing)>0 and ((totalcountlist(traininglist[ord(mystring[i])-97][ord(mystring[i+1])-97]))+smoothing*vocabularysize)>0):
                score += math.log(((traininglist[ord(mystring[i]) - 97][ord(mystring[i + 1]) - 97][ord(mystring[i + 2]) - 97] + smoothing)/((totalcountlist(traininglist[ord(mystring[i])-97][ord(mystring[i+1])-97]))+smoothing*vocabularysize)),10)
            else:
                score=(-99999999)

        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and ord(mystring[i + 1]) >= 97 and ord(mystring[i + 1]) <= 122 and ord(mystring[i+2]) >= 65 and ord(mystring[i+2]) <= 90):
            if((traininglist[ord(mystring[i]) - 97][ord(mystring[i + 1]) - 97][ord(mystring[i + 2]) - 39] + smoothing)>0 and ((totalcountlist(traininglist[ord(mystring[i])-97][ord(mystring[i+1])-97]))+smoothing*vocabularysize)>0):
                score += math.log(((traininglist[ord(mystring[i]) - 97][ord(mystring[i + 1]) - 97][ord(mystring[i + 2]) - 39] + smoothing)/((totalcountlist(traininglist[ord(mystring[i])-97][ord(mystring[i+1])-97]))+smoothing*vocabularysize)),10)
            else:
                score=(-99999999)
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and ord(mystring[i + 1]) >= 65 and ord(mystring[i + 1]) <= 90 and ord(mystring[i+2]) >= 97 and ord(mystring[i+2]) <= 122):
            if((traininglist[ord(mystring[i]) - 97][ord(mystring[i + 1]) - 39][ord(mystring[i + 2]) - 97] + smoothing)>0 and ((totalcountlist(traininglist[ord(mystring[i])-97][ord(mystring[i+1])-39]))+smoothing*vocabularysize)>0 ):
                score += math.log(((traininglist[ord(mystring[i]) - 97][ord(mystring[i + 1]) - 39][ord(mystring[i + 2]) - 97] + smoothing)/((totalcountlist(traininglist[ord(mystring[i])-97][ord(mystring[i+1])-39]))+smoothing*vocabularysize)),10)
            else:
                score=(-99999999)
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and ord(mystring[i + 1]) >= 65 and ord(mystring[i + 1]) <= 90 and ord(mystring[i + 2]) >= 65 and ord(mystring[i + 2]) <= 90):
            if((traininglist[ord(mystring[i]) - 97][ord(mystring[i + 1]) - 39][ord(mystring[i + 2]) - 39] + smoothing)>0 and ((totalcountlist(traininglist[ord(mystring[i])-97][ord(mystring[i+1])-39]))+smoothing*vocabularysize) >0):
                score += math.log(((traininglist[ord(mystring[i]) - 97][ord(mystring[i + 1]) - 39][ord(mystring[i + 2]) - 39] + smoothing)/((totalcountlist(traininglist[ord(mystring[i])-97][ord(mystring[i+1])-39]))+smoothing*vocabularysize)),10)
            else:
                score=(-99999999)
        if ((ord(mystring[i]) >= 65 and ord(mystring[i]) <= 90) and ord(mystring[i+1]) >= 97 and ord(mystring[i+1]) <= 122 and ord(mystring[i+2]) >= 97 and ord(mystring[i+2]) <= 122):
            if((traininglist[ord(mystring[i]) - 39][ord(mystring[i + 1]) - 97][ord(mystring[i + 2]) - 97] + smoothing)>0 and ((totalcountlist(traininglist[ord(mystring[i])-39][ord(mystring[i+1])-97]))+smoothing*vocabularysize) >0):
                score += math.log(((traininglist[ord(mystring[i]) - 39][ord(mystring[i + 1]) - 97][ord(mystring[i + 2]) - 97] + smoothing)/((totalcountlist(traininglist[ord(mystring[i])-39][ord(mystring[i+1])-97]))+smoothing*vocabularysize)),10)
            else:
                score=(-99999999)
        if ((ord(mystring[i]) >= 65 and ord(mystring[i]) <= 90) and ord(mystring[i + 1]) >= 97 and ord(mystring[i + 1]) <= 122 and ord(mystring[i+2]) >= 65 and ord(mystring[i+2]) <= 90):
            if((traininglist[ord(mystring[i]) - 39][ord(mystring[i + 1]) - 97][ord(mystring[i + 2]) - 39] + smoothing)>0 and ((totalcountlist(traininglist[ord(mystring[i])-39][ord(mystring[i+1])-97]))+smoothing*vocabularysize)>0):
                score += math.log(((traininglist[ord(mystring[i]) - 39][ord(mystring[i + 1]) - 97][ord(mystring[i + 2]) - 39] + smoothing)/((totalcountlist(traininglist[ord(mystring[i])-39][ord(mystring[i+1])-97]))+smoothing*vocabularysize)),10)
            else:
                score=(-99999999)
        if ((ord(mystring[i]) >= 65 and ord(mystring[i]) <= 90) and ord(mystring[i + 1]) >= 65 and ord(mystring[i + 1]) <= 90 and ord(mystring[i+2]) >= 97 and ord(mystring[i+2]) <= 122):
            if((traininglist[ord(mystring[i]) - 39][ord(mystring[i + 1]) - 39][ord(mystring[i + 2]) - 97] + smoothing)>0 and ((totalcountlist(traininglist[ord(mystring[i])-39][ord(mystring[i+1])-39]))+smoothing*vocabularysize)>0):
                score += math.log(((traininglist[ord(mystring[i]) - 39][ord(mystring[i + 1]) - 39][ord(mystring[i + 2]) - 97] + smoothing)/((totalcountlist(traininglist[ord(mystring[i])-39][ord(mystring[i+1])-39]))+smoothing*vocabularysize)),10)
            else:
                score=(-99999999)
        if ((ord(mystring[i]) >= 65 and ord(mystring[i]) <= 90) and ord(mystring[i + 1]) >= 65 and ord(mystring[i + 1]) <= 90 and ord(mystring[i + 2]) >= 65 and ord(mystring[i + 2]) <= 90):
            if((traininglist[ord(mystring[i]) - 39][ord(mystring[i + 1]) - 39][ord(mystring[i + 2]) - 39] + smoothing)>0 and ((totalcountlist(traininglist[ord(mystring[i])-39][ord(mystring[i+1])-39]))+smoothing*vocabularysize)>0):
                score += math.log(((traininglist[ord(mystring[i]) - 39][ord(mystring[i + 1]) - 39][ord(mystring[i + 2]) - 39] + smoothing)/((totalcountlist(traininglist[ord(mystring[i])-39][ord(mystring[i+1])-39]))+smoothing*vocabularysize)),10)
            else:
                score=(-99999999)
    score+=math.log((classsize/totaldocs),10)
    return score

def calculatescoreisalpha(mystring, smoothing, classsize, vocabularysize, totaldocs, traininglist):
    score = 0
    for i in range(len(mystring)):
        if(mystring[i].isalpha() and (mystring[i] in traininglist)):
            if((float(traininglist[mystring[i]]) + smoothing)>0 and (countkeys(traininglist) + (vocabularysize+1) * smoothing)>0):
                score += math.log(((float(traininglist[mystring[i]]) + smoothing) / (countkeys(traininglist) + (vocabularysize+1) * smoothing)), 10)
            else:
                scre=(-99999999)

        elif(mystring[i].isalpha() and not(mystring[i] in traininglist)):
            if((smoothing)>0 and (countkeys(traininglist) + (vocabularysize+1) * smoothing)>0):
                score+=math.log(((smoothing) / (countkeys(traininglist) + (vocabularysize+1) * smoothing)), 10)
            else:
                score=(-99999999)


    score+=math.log((classsize/totaldocs),10)
    return score

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





def calculatescoreisalphabigram(mystring, smoothing, classsize, vocabularysize, totaldocs, traininglist):
    score = 0
    myfirst=getingfirstletofbigram(traininglist)
    for i in range(len(mystring)-1):
        bigram = mystring[i] + mystring[i + 1]
        if ((mystring[i].isalpha())and (mystring[i+1].isalpha())and (bigram in traininglist)):
            if((float(traininglist[bigram]) + smoothing) >0 and (countlefttotalbigram(traininglist,mystring[i]) + (vocabularysize+1) * smoothing)>0 ):
                score += math.log((float(traininglist[bigram]) + smoothing) / (countlefttotalbigram(traininglist,mystring[i]) + (vocabularysize+1) * smoothing),10)
            else:
                score=(-99999999)
        elif  ((mystring[i].isalpha()) and (mystring[i+1].isalpha()) and (not (bigram in traininglist)) and (mystring[i] in myfirst)):
            if((smoothing)>0 and (countlefttotalbigram(traininglist, mystring[i]) + (vocabularysize + 1) * smoothing)>0 ):
                score += math.log((smoothing) / (countlefttotalbigram(traininglist, mystring[i]) + (vocabularysize + 1) * smoothing), 10)
            else:
                score=(-99999999)
        elif  ((mystring[i].isalpha() )  and  (mystring[i+1].isalpha()) and   (not (mystring[i] in myfirst))):
            if((smoothing)>0 and ((vocabularysize + 1) * smoothing)>0):
                score += math.log( (smoothing) / ((vocabularysize + 1) * smoothing), 10)
            else:
                score=(-99999999)
    score += math.log(classsize / totaldocs, 10)
    return score


def calculatescoreisalphatrigram(mystring, smoothing, classsize, vocabularysize, totaldocs, traininglist,bigramlist):
    score = 0
    for i in range(len(mystring)-2):
        trigram=mystring[i] + mystring[i + 1]+mystring[i+2]
        bigram=mystring[i] + mystring[i + 1]
        if ((mystring[i].isalpha()) and (mystring[i + 1].isalpha()) and (mystring[i + 2].isalpha() ) and (trigram in traininglist)):
            if((float(traininglist[trigram]) + smoothing) >0 and (counttrigramtotal12(traininglist,mystring[i],mystring[i+1]) + (vocabularysize + 1) * smoothing)>0):

                score += math.log(((float(traininglist[trigram]) + smoothing) / (counttrigramtotal12(traininglist,mystring[i],mystring[i+1]) + (vocabularysize + 1) * smoothing)), 10)
            else:
                score=(-99999999)
        elif ((mystring[i].isalpha() )and  (mystring[i + 1].isalpha()) and  (mystring[i + 2].isalpha()) and  (not (trigram in traininglist)) and (bigram in bigramlist) ):
            if((smoothing)>0 and (counttrigramtotal12(traininglist, mystring[i], mystring[i + 1]) + (vocabularysize + 1) * smoothing)>0 ):
                score += math.log(((smoothing) / (counttrigramtotal12(traininglist, mystring[i], mystring[i + 1]) + (vocabularysize + 1) * smoothing)), 10)
            else:
                score=(-99999999)
        elif ((mystring[i].isalpha()) and  (mystring[i + 1].isalpha()) and  (mystring[i + 2].isalpha())  and (not (bigram in bigramlist) )):
            if((smoothing)>0 and ( (vocabularysize + 1) * smoothing)>0):

                score += math.log((smoothing) / ( (vocabularysize + 1) * smoothing), 10)
            else:
                score=(-99999999)

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
        if ((mystring[i].isalpha()) and (mystring[i + 1].isalpha()) and (mystring[i + 2].isalpha() ) and(mystring[i+3].isalpha()) and (fourgram in traininglist)):
            if((float(traininglist[fourgram]) + smoothing) >0 and (count4gramtotal123(traininglist,mystring[i],mystring[i+1],mystring[i+2]) + (vocabularysize + 1) * smoothing)>0):

                score += math.log(((float(traininglist[fourgram]) + smoothing) / (count4gramtotal123(traininglist,mystring[i],mystring[i+1],mystring[i+2]) + (vocabularysize + 1) * smoothing)), 10)
            else:
                score=(-99999999)
        elif ((mystring[i].isalpha() )and  (mystring[i + 1].isalpha()) and  (mystring[i + 2].isalpha()) and(mystring[i+3].isalpha()) and  (not (fourgram in traininglist)) and (trigram in trigramlist) ):
            if((smoothing)>0 and (count4gramtotal123(traininglist, mystring[i], mystring[i + 1],mystring[i+2]) + (vocabularysize + 1) * smoothing)>0 ):
                score += math.log(((smoothing) / (count4gramtotal123(traininglist, mystring[i], mystring[i + 1],mystring[i+2]) + (vocabularysize + 1) * smoothing)), 10)
            else:
                score=(-99999999)
        elif ((mystring[i].isalpha()) and  (mystring[i + 1].isalpha()) and  (mystring[i + 2].isalpha())  and (mystring[i+3].isalpha()) and (not (trigram in trigramlist) )):
            if((smoothing)>0 and ( (vocabularysize + 1) * smoothing)>0):

                score += math.log((smoothing) / ( (vocabularysize + 1) * smoothing), 10)
            else:
                score=(-99999999)

    score += math.log((classsize / totaldocs), 10)
    return score




def calculatescores(mystring,smoothing,classsize,vocabularysize,totaldocs,traininglist):
    score=0
    for i in range(len(mystring)):
        if(ord(mystring[i])>=97 and ord(mystring[i])<=122):
            if((traininglist[ord(mystring[i])-97]+smoothing)>0 and (totalcountlist(traininglist)+vocabularysize*smoothing)>0):
                score+=math.log((traininglist[ord(mystring[i])-97]+smoothing)/(totalcountlist(traininglist)+vocabularysize*smoothing),10)
            else:
                score=(-99999999)
    score+=math.log(classsize/totaldocs,10)
    return score

def naivebayes(v,n,delta,train,test):
    nameoftracefile="trace_"+str(v)+"_"+str(n)+"_"+str(delta)+".txt"
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


    nameoffile2="eval_"+str(v)+"_"+str(n)+"_"+str(delta)+".txt"
    f2 = open(nameoffile2, "w+", encoding="utf8")
    f2.write(str(accuracy)+"\n")
    f2.write(str(precisionbasque)+"  "+str(precisioncatalan)+"  "+str(precisiongalician)+"  "+str(precisionspanish)+"  "+str(precisionenglish)+"  "+str(precisionportoguse)+"\n")
    f2.write(str(recallbasque) + "  " + str(recallcatalan) + "  " + str(recallgalician) + "  " + str(recallspanish) + "  " + str(recallenglish) + "  " + str(recallportoguse) + "\n")
    f2.write(str(f1basque) + "  " + str(f1catalan) + "  " + str(f1galician) + "  " + str(f1spanish) + "  " + str(f1english) + "  " + str(f1portoguse) + "\n")
    f2.write(str(macrof1)+"  "+str(waveragef1))
    print(confusionmatrix)
    print(testbasque)
    print(testcatalan)
    print(testgalician)
    print(testspanish)
    print(testenglish)
    print(testportoguse)



naivebayes(3,4,1.0,"training-tweets.txt","test-tweets-given.txt")
print("completed")




'''
decim=[]
decim.append(str(0))
decim.append(str(0.1))
decim.append(str(0.2))
decim.append(str(0.3))
decim.append(str(0.4))
decim.append(str(0.5))
decim.append(str(0.6))
decim.append(str(0.7))
decim.append(str(0.8))
decim.append(str(0.9))
decim.append(str(1))
#naivebayes(3,2,0.2,"training-tweets.txt","test-tweets-given.txt")
precision=[]
recall=[]
f1=[]
contents=[]

for v in range(1,4):
    for n in range(1,4):

        for d in range(11):

            filename="eval_"+str(v)+"_"+str(n)+"_"+str(decim[d])+".txt"


            with open(filename, encoding="utf8") as f:
                for line in f:
                    contents.append(line)











copys = [''] * (len(contents))
for i in range(len(contents)):
    if (i < (len(contents) - 1)):
        contents[i] = contents[i][:-1]
    copys[i] = contents[i].split()



ya=[]

yp1=[]
yp2=[]
yp3=[]
yp4=[]
yp5=[]
yp6=[]
yr1=[]
yr2=[]
yr3=[]
yr4=[]
yr5=[]
yr6=[]
yf1=[]
yf2=[]
yf3=[]
yf4=[]
yf5=[]
yf6=[]
ymacro=[]
yave=[]
for p in range(165,220):

    for z in range(len(copys[p])):
        if (copys[p][z] == "undefined"):
             copys[p][z] = 0
    if(p%5==1):

        yp1.append(float(copys[p][0]))
        yp2.append(float(copys[p][1]))
        yp3.append(float(copys[p][2]))
        yp4.append(float(copys[p][3]))
        yp5.append(float(copys[p][4]))
        yp6.append(float(copys[p][5]))
    if(p%5==2):

        yr1.append(float(copys[p][0]))
        yr2.append(float(copys[p][1]))
        yr3.append(float(copys[p][2]))
        yr4.append(float(copys[p][3]))
        yr5.append(float(copys[p][4]))
        yr6.append(float(copys[p][5]))
    if(p%5==3):
        yf1.append(float(copys[p][0]))
        yf2.append(float(copys[p][1]))
        yf3.append(float(copys[p][2]))
        yf4.append(float(copys[p][3]))
        yf5.append(float(copys[p][4]))
        yf6.append(float(copys[p][5]))
    if (p % 5 == 4):
        ymacro.append(float(copys[p][0]))
        yave.append(float(copys[p][1]))
    if(p%5==0):
        ya.append(float(copys[p][0]))


    



x=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

plt.title("V=2,n=1")
plt.xlabel("smoothing factor")

plt.ylabel("class recall")

plt.scatter(x,yr1,color='red',label="basque")
plt.scatter(x,yr2,color='blue',label="catalan")
plt.scatter(x,yr3,color='black',label="galician")
plt.scatter(x,yr4,color='green',label="spanish")
plt.scatter(x,yr5,color='yellow',label="english")
plt.scatter(x,yr6,color='brown',label="portoguse")


plt.scatter(x,ymacro,color='red',label="macrof1")
plt.scatter(x,yave,color='blue',label="weighted_average_f1")


plt.scatter(x,ya,color='red',label="accuracy")

ax = plt.subplot(111)
chartBox = ax.get_position()
ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.6, chartBox.height])
ax.legend(loc='upper center', bbox_to_anchor=(1.45, 0.8), shadow=True, ncol=1)
plt.show()
'''
