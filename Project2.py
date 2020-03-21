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


# merging two dictionaries
def combinedictionaries(dic1,dic2):
    for i in dic2:
        if(i in dic1):
            dic1[i]=float(dic1[i])+float(dic2[i])
        else:
            dic1[i]=dic2[i]
    return dic1





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

    return results














def countlefttotalbigram(dic,leftchar):
    sum=0
    for i in dic:
        if(i[0]==leftchar):
            sum+=float(dic[i])
    return sum

def countrighttotalbigram(dic,rightchar):
    sum=0
    for i in dic:
        if(i[1]==rightchar):
            sum+=float(dic[i])
    return sum

def counttrigramtotal12(dic,one,two):
    sum=0
    for i in dic:
        if(i[0]==one and i[1]==two):
            sum+=float(dic[i])
    return sum

def counttrigramtotal13(dic,one,three):
    sum=0
    for i in dic:
        if(i[0]==one and i[2]==three):
            sum+=float(dic[i])
    return sum

def counttrigramtotal23(dic,two,three):
    sum=0
    for i in dic:
        if(i[1]==two and i[2]==three):
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
            score+=math.log((traininglist[ord(mystring[i])-97][ord(mystring[i+1])-97]+smoothing)/((totalcountlist(traininglist[ord(mystring[i])-97]))+smoothing*vocabularysize))
    score+=math.log(classsize/totaldocs,10)
    return score


def calculatescoretrigram(mystring, smoothing, classsize, vocabularysize, totaldocs, traininglist):
    score = 0
    for i in range(len(mystring) - 2):
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and ord(mystring[i+1]) >= 97 and ord(mystring[i+1]) <= 122 and ord(mystring[i+2]) >= 97 and ord(mystring[i+2]) <= 122):
            score+=math.log((traininglist[ord(mystring[i])-97][ord(mystring[i+1])-97][ord(mystring[i+2])-97]+smoothing)/((totalcountlist(traininglist[ord(mystring[i])-97][ord(mystring[i+1])-97]))+smoothing*vocabularysize))
    score+=math.log(classsize/totaldocs,10)
    return score
def calculatescorescase(mystring,smoothing,classsize,vocabularysize,totaldocs,traininglist):
    score=0
    for i in range(len(mystring)):
        if((ord(mystring[i])>=97 and ord(mystring[i])<=122)):
            score+=math.log((traininglist[ord(mystring[i])-97]+smoothing)/(totalcountlist(traininglist)+vocabularysize*smoothing),10)
        elif ((ord(mystring[i])>=65 and ord(mystring[i])<=90)):
            score += math.log((traininglist[ord(mystring[i]) - 39]+smoothing) / (totalcountlist(traininglist)+vocabularysize * smoothing), 10)

    score+=math.log(classsize/totaldocs,10)
    return score

def calculatescorebigramcase(mystring,smoothing,classsize,vocabularysize,totaldocs,traininglist):
    score=0
    for i in range(len(mystring)-1):
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and (ord(mystring[i+1]) >= 97 and ord(mystring[i+1]) <= 122)):
            score+=math.log((traininglist[ord(mystring[i])-97][ord(mystring[i+1])-97]+smoothing)/((totalcountlist(traininglist[ord(mystring[i])-97]))+smoothing*vocabularysize))
        if ((ord(mystring[i]) >= 65 and ord(mystring[i]) <= 90) and ord(mystring[i + 1]) >= 65 and ord(mystring[i + 1]) <= 90):
            score+=math.log((traininglist[ord(mystring[i]) - 39][ord(mystring[i + 1]) - 39] + smoothing)/((totalcountlist(traininglist[ord(mystring[i])-39]))+smoothing*vocabularysize))
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and ord(mystring[i + 1]) >= 65 and ord(mystring[i + 1]) <= 90):
            score += math.log((traininglist[ord(mystring[i]) - 97][ord(mystring[i + 1]) - 39] +smoothing)/((totalcountlist(traininglist[ord(mystring[i])-97]))+smoothing*vocabularysize))
        if ((ord(mystring[i]) >= 65 and ord(mystring[i]) <= 90) and ord(mystring[i + 1]) >= 97 and ord(mystring[i + 1]) <= 122):
            score += math.log((traininglist[ord(mystring[i]) - 39][ord(mystring[i + 1]) - 97] +smoothing)/((totalcountlist(traininglist[ord(mystring[i])-39]))+smoothing*vocabularysize))
    score+=math.log(classsize/totaldocs,10)
    return score

def calculatescoretrigramcase(mystring, smoothing, classsize, vocabularysize, totaldocs, traininglist):
    score = 0
    for i in range(len(mystring) - 2):
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and ord(mystring[i+1]) >= 97 and ord(mystring[i+1]) <= 122 and ord(mystring[i+2]) >= 97 and ord(mystring[i+2]) <= 122):
            score += math.log((traininglist[ord(mystring[i]) - 97][ord(mystring[i + 1]) - 97][ord(mystring[i + 2]) - 97] + smoothing)/((totalcountlist(traininglist[ord(mystring[i])-97][ord(mystring[i+1])-97]))+smoothing*vocabularysize))
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and ord(mystring[i + 1]) >= 97 and ord(mystring[i + 1]) <= 122 and ord(mystring[i+2]) >= 65 and ord(mystring[i+2]) <= 90):
            score += math.log((traininglist[ord(mystring[i]) - 97][ord(mystring[i + 1]) - 97][ord(mystring[i + 2]) - 39] + smoothing)/((totalcountlist(traininglist[ord(mystring[i])-97][ord(mystring[i+1])-97]))+smoothing*vocabularysize))
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and ord(mystring[i + 1]) >= 65 and ord(mystring[i + 1]) <= 90 and ord(mystring[i+2]) >= 97 and ord(mystring[i+2]) <= 122):
            score += math.log((traininglist[ord(mystring[i]) - 97][ord(mystring[i + 1]) - 39][ord(mystring[i + 2]) - 97] + smoothing)/((totalcountlist(traininglist[ord(mystring[i])-97][ord(mystring[i+1])-39]))+smoothing*vocabularysize))
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and ord(mystring[i + 1]) >= 65 and ord(mystring[i + 1]) <= 90 and ord(mystring[i + 2]) >= 65 and ord(mystring[i + 2]) <= 90):
            score += math.log((traininglist[ord(mystring[i]) - 97][ord(mystring[i + 1]) - 39][ord(mystring[i + 2]) - 39] + smoothing)/((totalcountlist(traininglist[ord(mystring[i])-97][ord(mystring[i+1])-39]))+smoothing*vocabularysize))
        if ((ord(mystring[i]) >= 65 and ord(mystring[i]) <= 90) and ord(mystring[i+1]) >= 97 and ord(mystring[i+1]) <= 122 and ord(mystring[i+2]) >= 97 and ord(mystring[i+2]) <= 122):
            score += math.log((traininglist[ord(mystring[i]) - 39][ord(mystring[i + 1]) - 97][ord(mystring[i + 2]) - 97] + smoothing)/((totalcountlist(traininglist[ord(mystring[i])-39][ord(mystring[i+1])-97]))+smoothing*vocabularysize))
        if ((ord(mystring[i]) >= 65 and ord(mystring[i]) <= 90) and ord(mystring[i + 1]) >= 97 and ord(mystring[i + 1]) <= 122 and ord(mystring[i+2]) >= 65 and ord(mystring[i+2]) <= 90):
            score += math.log((traininglist[ord(mystring[i]) - 39][ord(mystring[i + 1]) - 97][ord(mystring[i + 2]) - 39] + smoothing)/((totalcountlist(traininglist[ord(mystring[i])-39][ord(mystring[i+1])-97]))+smoothing*vocabularysize))
        if ((ord(mystring[i]) >= 65 and ord(mystring[i]) <= 90) and ord(mystring[i + 1]) >= 65 and ord(mystring[i + 1]) <= 90 and ord(mystring[i+2]) >= 97 and ord(mystring[i+2]) <= 122):
            score += math.log((traininglist[ord(mystring[i]) - 39][ord(mystring[i + 1]) - 39][ord(mystring[i + 2]) - 97] + smoothing)/((totalcountlist(traininglist[ord(mystring[i])-39][ord(mystring[i+1])-39]))+smoothing*vocabularysize))
        if ((ord(mystring[i]) >= 65 and ord(mystring[i]) <= 90) and ord(mystring[i + 1]) >= 65 and ord(mystring[i + 1]) <= 90 and ord(mystring[i + 2]) >= 65 and ord(mystring[i + 2]) <= 90):
            score += math.log((traininglist[ord(mystring[i]) - 39][ord(mystring[i + 1]) - 39][ord(mystring[i + 2]) - 39] + smoothing)/((totalcountlist(traininglist[ord(mystring[i])-39][ord(mystring[i+1])-39]))+smoothing*vocabularysize))
    score+=math.log(classsize/totaldocs,10)
    return score

def calculatescoreisalpha(mystring, smoothing, classsize, vocabularysize, totaldocs, traininglist):
    score = 0
    for i in range(len(mystring)):
        if(mystring[i].isalpha() and (mystring[i] in traininglist)):
            score += math.log((float(traininglist[mystring[i]]) + smoothing) / (countkeys(traininglist) + (vocabularysize+1) * smoothing), 10)
        elif(mystring[i].isalpha() and not(mystring[i] in traininglist)):
            score+=math.log((smoothing) / (countkeys(traininglist)  + (vocabularysize+1) * smoothing), 10)

    score+=math.log(classsize/totaldocs,10)
    return score
def calculatescoreisalphabigram(mystring, smoothing, classsize, vocabularysize, totaldocs, traininglist):
    score = 0
    for i in range(len(mystring)-1):
        if ((mystring[i].isalpha() and (mystring[i] in traininglist)) and (mystring[i+1].isalpha() and (mystring[i+1] in traininglist))):
            bigram=mystring[i]+mystring[i+1]
            score += math.log((float(traininglist[bigram]) + smoothing) / (countlefttotalbigram(traininglist,mystring[i]) + (vocabularysize+1 )* smoothing),10)
        elif  ((mystring[i].isalpha() and (mystring[i] in traininglist)) and (mystring[i+1].isalpha() and not (mystring[i+1] in traininglist))):
            score += math.log((smoothing) / (countlefttotalbigram(traininglist, mystring[i]) + (vocabularysize + 1) * smoothing), 10)
        elif  ((mystring[i].isalpha() and not (mystring[i] in traininglist)) and (mystring[i+1].isalpha() and  (mystring[i+1] in traininglist))):
            score += math.log( (smoothing) / ((vocabularysize + 1) * smoothing), 10)
        elif  ((mystring[i].isalpha() and not (mystring[i] in traininglist)) and (mystring[i+1].isalpha() and not (mystring[i+1] in traininglist))):
            score += math.log((smoothing) / ((vocabularysize + 1) * smoothing), 10)

    score += math.log(classsize / totaldocs, 10)
    return score


def calculatescoreisalphatrigram(mystring, smoothing, classsize, vocabularysize, totaldocs, traininglist):
    score = 0
    for i in range(len(mystring)-2):
        if ((mystring[i].isalpha() and (mystring[i] in traininglist)) and (mystring[i + 1].isalpha() and (mystring[i + 1] in traininglist)) and (mystring[i + 2].isalpha() and (mystring[i + 2] in traininglist))):
            bigram = mystring[i] + mystring[i + 1]+mystring[i+2]
            score += math.log((float(traininglist[bigram]) + smoothing) / (counttrigramtotal12(traininglist,mystring[i],mystring[i+1]) + (vocabularysize + 1) * smoothing), 10)
        elif ((mystring[i].isalpha() and (mystring[i] in traininglist)) and (mystring[i + 1].isalpha() and (mystring[i + 1] in traininglist)) and (mystring[i + 2].isalpha() and  not (mystring[i + 2] in traininglist))):
            score += math.log((smoothing) / (counttrigramtotal12(traininglist, mystring[i], mystring[i + 1]) + (vocabularysize + 1) * smoothing), 10)
        elif ((mystring[i].isalpha() and (mystring[i] in traininglist)) and (mystring[i + 1].isalpha() and not (mystring[i + 1] in traininglist)) and (mystring[i + 2].isalpha() and  not (mystring[i + 2] in traininglist))):
            score += math.log((smoothing) / ( (vocabularysize + 1) * smoothing), 10)
        elif ((mystring[i].isalpha() and (mystring[i] in traininglist)) and (mystring[i + 1].isalpha() and not (mystring[i + 1] in traininglist)) and (mystring[i + 2].isalpha() and   (mystring[i + 2] in traininglist))):
            score += math.log((smoothing) / ( (vocabularysize + 1) * smoothing), 10)
        elif ((mystring[i].isalpha() and not (mystring[i] in traininglist)) and (mystring[i + 1].isalpha() and  (mystring[i + 1] in traininglist)) and (mystring[i + 2].isalpha() and   (mystring[i + 2] in traininglist))):
            score += math.log((smoothing) / ( (vocabularysize + 1) * smoothing), 10)
        elif ((mystring[i].isalpha() and not (mystring[i] in traininglist)) and (mystring[i + 1].isalpha() and  not (mystring[i + 1] in traininglist)) and (mystring[i + 2].isalpha() and   (mystring[i + 2] in traininglist))):
            score += math.log((smoothing) / ( (vocabularysize + 1) * smoothing), 10)
        elif ((mystring[i].isalpha() and not (mystring[i] in traininglist)) and (mystring[i + 1].isalpha() and   (mystring[i + 1] in traininglist)) and (mystring[i + 2].isalpha() and  not  (mystring[i + 2] in traininglist))):
            score += math.log((smoothing) / ( (vocabularysize + 1) * smoothing), 10)
        elif ((mystring[i].isalpha() and not (mystring[i] in traininglist)) and (mystring[i + 1].isalpha() and  not (mystring[i + 1] in traininglist)) and (mystring[i + 2].isalpha() and  not  (mystring[i + 2] in traininglist))):
            score += math.log((smoothing) / ( (vocabularysize + 1) * smoothing), 10)
    score += math.log(classsize / totaldocs, 10)
    return score



def calculatescores(mystring,smoothing,classsize,vocabularysize,totaldocs,traininglist):
    score=0
    for i in range(len(mystring)):
        if(ord(mystring[i])>=97 and ord(mystring[i])<=122):
            score+=math.log((traininglist[ord(mystring[i])-97]+smoothing)/(totalcountlist(traininglist)+vocabularysize*smoothing),10)
    score+=math.log(classsize/totaldocs,10)
    return score

def naivebayes(v,n,delta,train,test):
    nameoftracefile="trace_"+str(v)+"_"+str(n)+"_"+str(delta)+".txt"
    f1 = open(nameoftracefile, "w+", encoding="utf8")
    numcorrectclass=0
    results=[]
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
            scores[0] = calculatescoreisalphatrigram(copystring[i], delta, results[0], results[12], (results[0] +  results[1]+  results[2] +  results[3]+  results[4] +  results[5]), results[6])
            scores[1] = calculatescoreisalphatrigram(copystring[i], delta, results[1], results[13], (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[7])
            scores[2] = calculatescoreisalphatrigram(copystring[i], delta, results[2], results[14], (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[8])
            scores[3] = calculatescoreisalphatrigram(copystring[i], delta, results[3], results[15], (results[0] +  results[1]+  results[2] +  results[3]+  results[4] +  results[5]), results[9])
            scores[4] = calculatescoreisalphatrigram(copystring[i], delta, results[4], results[16], (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[10])
            scores[5] = calculatescoreisalphatrigram(copystring[i], delta, results[5], results[17], (results[0] + results[1] + results[2] + results[3] + results[4] + results[5]), results[11])

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
        else:
            label2="wrong"


        f1.write(copytweets[i][0]+"  "+label+"  "+"{:.2e}".format((scores[indexm]))+"  "+copytweets[i][2]+"  "+label2+"\n")
    f1.close()
    accuracy=(numcorrectclass/len(tweets))
    print(accuracy)
    nameoffile2="eval_"+str(v)+"_"+str(n)+"_"+str(delta)+".txt"
    f2 = open(nameoffile2, "w+", encoding="utf8")










naivebayes(1,2,0.5,"training-tweets.txt","training-tweets.txt")