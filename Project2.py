import numpy as np
import math


def totalcountlist(mylist):
    sum=0
    for i in range(len(mylist)):
        sum+=float(mylist[i])
    return sum

def totalcountbigramlist(mylist):
    sum=0
    for i in range(len(mylist)):
        for j in range(len(mylist[0])):
            sum+=float(mylist[i][j])
    return sum


def totalcounttrigramlist(mylist):
    sum=0
    for i in range(len(mylist)):
        for j in range(len(mylist[0])):
            for k in range(len(mylist[i][j])):
                sum+=float(mylist[i][j][k])
    return sum



def createcountsoflowercase(mystring):
    mystring=mystring.lower()
    mylist=[0]*26
    for char in mystring:
        if(ord(char)>=97 and ord(char)<=122):
            mylist[ord(char)-97]+=1
    return mylist

def createcountsofloweranduppercase(mystring):
    mylist=[0]*52
    for char in mystring:
        if(ord(char)>=65 and ord(char)<=90):
            mylist[ord(char)-39]+=1
        if (ord(char) >= 97 and ord(char) <= 122):
            mylist[ord(char) - 97] += 1
    return mylist


def createbigramlower(mystring):
    mystring = mystring.lower()
    mylist=np.array([[0]*26]*26)
    for i in range(len(mystring)-1):
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and ord(mystring[i+1]) >= 97 and ord(mystring[i+1]) <= 122):
            mylist[ord(mystring[i])-97][ord(mystring[i+1])-97]+=1
    return mylist

def createtrigramlower(mystring):
    mystring = mystring.lower()
    mylist=np.array([[[0]*26]*26]*26)
    for i in range(len(mystring)-2):
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and ord(mystring[i+1]) >= 97 and ord(mystring[i+1]) <= 122 and ord(mystring[i+2]) >= 97 and ord(mystring[i+2]) <= 122):
            mylist[ord(mystring[i])-97][ord(mystring[i+1])-97][ord(mystring[i+2])-97]+=1
    return mylist


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



def createcountisalpha(mystring):
        mydictionary={}
        for char in mystring:
            if (char.isalpha()):
                if(not (char in mydictionary)):
                    mydictionary[char]=1
                elif(char in mydictionary):
                    mydictionary[char]=(int(mydictionary[char])+1)
        return mydictionary

def createbigramisalpha(mystring):
    mybigramdic={}
    for i in range(len(mystring)-1):
        if(mystring[i].isalpha() and mystring[i+1].isalpha()):
            bigramkey=(mystring[i]+mystring[i+1])
            if(not(bigramkey in mybigramdic)):
                mybigramdic[bigramkey]=1
            elif(bigramkey in mybigramdic):
                mybigramdic[bigramkey]=int(mybigramdic[bigramkey])+1
    return mybigramdic


def createtrigramisalpha(mystring):
    mytrigramdic={}
    for i in range(len(mystring)-2):
        if(mystring[i].isalpha() and mystring[i+1].isalpha() and mystring[i+2].isalpha()):
            trigramkey=(mystring[i]+mystring[i+1]+mystring[i+2])
            if(not(trigramkey in mytrigramdic)):
                mytrigramdic[trigramkey]=1
            elif(trigramkey in mytrigramdic):
                mytrigramdic[trigramkey]=int(mytrigramdic[trigramkey])+1
    return mytrigramdic

def combinedictionaries(dic1,dic2):
    for i in dic2:
        if(i in dic1):
            dic1[i]=int(dic1[i])+int(dic2[i])
        else:
            dic1[i]=dic2[i]
    return dic1



def calculatecount(train):
    tweets = []

    numtweetbasque = 0
    numtweetcatalan = 0
    numtweetgalician = 0
    numtweetspanish = 0
    numtweetenglish = 0
    numtweetportoguse = 0

    countbasque=[0]*26
    countcatalan=[0]*26
    countgalician=[0]*26
    countspanish=[0]*26
    countenglish=[0]*26
    countportogeuse = [0] * 26



    countbasquecasesensitive=[0]*52
    countcatalancasesensitive = [0] * 52
    countgaliciancasesensitive = [0] * 52
    countspanishcasesensitive = [0] * 52
    countenglishcasesensitive = [0] * 52
    countportogusecasesensitive = [0] * 52

    countbasquebigram=np.array([[0]*26]*26)
    countcatalanbigram=np.array([[0]*26]*26)
    countgalicianbigram=np.array([[0]*26]*26)
    countspanishbigram=np.array([[0]*26]*26)
    countenglishbigram=np.array([[0]*26]*26)
    countportogusebigram=np.array([[0]*26]*26)

    countbasquebigramcase = np.array([[0] * 52] * 52)
    countcatalanbigramcase = np.array([[0] * 52] * 52)
    countgalicianbigramcase = np.array([[0] * 52] * 52)
    countspanishbigramcase = np.array([[0] * 52] * 52)
    countenglishbigramcase = np.array([[0] * 52] * 52)
    countportogusebigramcase = np.array([[0] * 52] * 52)

    countbasquetrigram = np.array([[[0]*26]*26]*26)
    countcatalantrigram = np.array([[[0]*26]*26]*26)
    countgaliciantrigram = np.array([[[0]*26]*26]*26)
    countspanishtrigram = np.array([[[0]*26]*26]*26)
    countenglishtrigram = np.array([[[0]*26]*26]*26)
    countportogusetrigram = np.array([[[0]*26]*26]*26)

    countbasquetrigramcase = np.array([[[0]*52]*52]*52)
    countcatalantrigramcase = np.array([[[0]*52]*52]*52)
    countgaliciantrigramcase = np.array([[[0]*52]*52]*52)
    countspanishtrigramcase = np.array([[[0]*52]*52]*52)
    countenglishtrigramcase = np.array([[[0]*52]*52]*52)
    countportogusetrigramcase = np.array([[[0]*52]*52]*52)

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
    with open(train,encoding="utf8") as f:
        for line in f:
            tweets.append(line)
    copystring=[''] * (len(tweets))
    copytweets=[''] * (len(tweets))
    for i in range(len(tweets)):
        if (i < (len(tweets) - 1)):
            tweets[i] = tweets[i][:-1]
            copytweets[i] = tweets[i].split()
            index=tweets[i].index(copytweets[i][3])
            copystring[i]=tweets[i][index:]
            if(copytweets[i][2]=='eu'):
                countbasque+=np.array(createcountsoflowercase(copystring[i]))
                numtweetbasque+=1
                countbasquecasesensitive+=np.array(createcountsofloweranduppercase(copystring[i]))
                countbasquebigram+=createbigramlower(copystring[i])
                countbasquebigramcase+=createbigram(copystring[i])
                countbasquetrigram+=createtrigramlower(copystring[i])
                countbasquetrigramcase+=createtrigram(copystring[i])
                countalphabasque=combinedictionaries(countalphabasque,createcountisalpha(copystring[i]))
                countalphabigrambasque = combinedictionaries(countalphabigrambasque, createbigramisalpha(copystring[i]))
                countalphatrigrambasque = combinedictionaries(countalphatrigrambasque, createtrigramisalpha(copystring[i]))
            elif(copytweets[i][2]=='ca'):
                countcatalan +=np.array(createcountsoflowercase(copystring[i]))
                numtweetcatalan+=1
                countcatalancasesensitive += np.array(createcountsofloweranduppercase(copystring[i]))
                countcatalanbigram += createbigramlower(copystring[i])
                countcatalanbigramcase += createbigram(copystring[i])
                countcatalantrigram += createtrigramlower(copystring[i])
                countcatalantrigramcase += createtrigram(copystring[i])
                countalphacatalan = combinedictionaries(countalphacatalan, createcountisalpha(copystring[i]))
                countalphabigramcatalan = combinedictionaries(countalphabigramcatalan, createbigramisalpha(copystring[i]))
                countalphatrigramcatalan = combinedictionaries(countalphatrigramcatalan, createtrigramisalpha(copystring[i]))
            elif(copytweets[i][2]=='gl'):
                countgalician+=np.array(createcountsoflowercase(copystring[i]))
                numtweetgalician+=1
                countgaliciancasesensitive += np.array(createcountsofloweranduppercase(copystring[i]))
                countgalicianbigram += createbigramlower(copystring[i])
                countgalicianbigramcase += createbigram(copystring[i])
                countgaliciantrigram += createtrigramlower(copystring[i])
                countgaliciantrigramcase += createtrigram(copystring[i])
                countalphagalician = combinedictionaries(countalphagalician, createcountisalpha(copystring[i]))
                countalphabigramgalician = combinedictionaries(countalphabigramgalician,createbigramisalpha(copystring[i]))
                countalphatrigramgalician = combinedictionaries(countalphatrigramgalician,createtrigramisalpha(copystring[i]))
            elif (copytweets[i][2] == 'es'):
                countspanish += np.array(createcountsoflowercase(copystring[i]))
                numtweetspanish+=1
                countspanishcasesensitive += np.array(createcountsofloweranduppercase(copystring[i]))
                countspanishbigram += createbigramlower(copystring[i])
                countspanishbigramcase += createbigram(copystring[i])
                countspanishtrigram += createtrigramlower(copystring[i])
                countspanishtrigramcase += createtrigram(copystring[i])
                countalphaspanish = combinedictionaries(countalphaspanish, createcountisalpha(copystring[i]))
                countalphabigramspanish = combinedictionaries(countalphabigramspanish,createbigramisalpha(copystring[i]))
                countalphatrigramspanish = combinedictionaries(countalphatrigramspanish,createtrigramisalpha(copystring[i]))
            elif (copytweets[i][2] == 'en'):
                countenglish +=np.array(createcountsoflowercase(copystring[i]))
                numtweetenglish+=1
                countenglishcasesensitive += np.array(createcountsofloweranduppercase(copystring[i]))
                countenglishbigram += createbigramlower(copystring[i])
                countenglishbigramcase += createbigram(copystring[i])
                countenglishtrigram += createtrigramlower(copystring[i])
                countenglishtrigramcase += createtrigram(copystring[i])
                countalphaenglish = combinedictionaries(countalphaenglish, createcountisalpha(copystring[i]))
                countalphabigramenglish = combinedictionaries(countalphabigramenglish,createbigramisalpha(copystring[i]))
                countalphatrigramenglish = combinedictionaries(countalphatrigramenglish,createtrigramisalpha(copystring[i]))
            elif (copytweets[i][2] == 'pt'):
                countportogeuse +=np.array(createcountsoflowercase(copystring[i]))
                numtweetportoguse+=1
                countportogusecasesensitive += np.array(createcountsofloweranduppercase(copystring[i]))
                countportogusebigram += createbigramlower(copystring[i])
                countportogusebigramcase += createbigram(copystring[i])
                countportogusetrigram += createtrigramlower(copystring[i])
                countportogusetrigramcase += createtrigram(copystring[i])
                countalphaportoguse = combinedictionaries(countalphaportoguse, createcountisalpha(copystring[i]))
                countalphabigramportoguse = combinedictionaries(countalphabigramportoguse,createbigramisalpha(copystring[i]))
                countalphatrigramportoguse = combinedictionaries(countalphatrigramportoguse,createtrigramisalpha(copystring[i]))
        else:
            copytweets[i] = tweets[i].split()
            index=tweets[i].index(copytweets[i][3])
            copystring[i]=tweets[i][index:]
            if (copytweets[i][2] == 'eu'):
                countbasque += np.array(createcountsoflowercase(copystring[i]))
                numtweetbasque += 1
                countbasquecasesensitive += np.array(createcountsofloweranduppercase(copystring[i]))
                countbasquebigram += createbigramlower(copystring[i])
                countbasquebigramcase += createbigram(copystring[i])
                countbasquetrigram += createtrigramlower(copystring[i])
                countbasquetrigramcase += createtrigram(copystring[i])
                countalphabasque=combinedictionaries(countalphabasque,createcountisalpha(copystring[i]))
                countalphabigrambasque = combinedictionaries(countalphabigrambasque, createbigramisalpha(copystring[i]))
                countalphatrigrambasque = combinedictionaries(countalphatrigrambasque, createtrigramisalpha(copystring[i]))

            elif (copytweets[i][2] == 'ca'):
                countcatalan += np.array(createcountsoflowercase(copystring[i]))
                numtweetcatalan += 1
                countcatalancasesensitive += np.array(createcountsofloweranduppercase(copystring[i]))
                countcatalanbigram += createbigramlower(copystring[i])
                countcatalanbigramcase += createbigram(copystring[i])
                countcatalantrigram += createtrigramlower(copystring[i])
                countcatalantrigramcase += createtrigram(copystring[i])
                countalphacatalan = combinedictionaries(countalphacatalan, createcountisalpha(copystring[i]))
                countalphabigramcatalan = combinedictionaries(countalphabigramcatalan, createbigramisalpha(copystring[i]))
                countalphatrigramcatalan = combinedictionaries(countalphatrigramcatalan, createtrigramisalpha(copystring[i]))

            elif (copytweets[i][2] == 'gl'):
                countgalician += np.array(createcountsoflowercase(copystring[i]))
                numtweetgalician += 1
                countgaliciancasesensitive += np.array(createcountsofloweranduppercase(copystring[i]))
                countgalicianbigram += createbigramlower(copystring[i])
                countgalicianbigramcase += createbigram(copystring[i])
                countgaliciantrigram += createtrigramlower(copystring[i])
                countgaliciantrigramcase += createtrigram(copystring[i])
                countalphagalician = combinedictionaries(countalphagalician, createcountisalpha(copystring[i]))
                countalphabigramgalician = combinedictionaries(countalphabigramgalician,createbigramisalpha(copystring[i]))
                countalphatrigramgalician = combinedictionaries(countalphatrigramgalician,createtrigramisalpha(copystring[i]))

            elif (copytweets[i][2] == 'es'):
                countspanish += np.array(createcountsoflowercase(copystring[i]))
                numtweetspanish += 1
                countspanishcasesensitive += np.array(createcountsofloweranduppercase(copystring[i]))
                countspanishbigram += createbigramlower(copystring[i])
                countspanishbigramcase += createbigram(copystring[i])
                countspanishtrigram += createtrigramlower(copystring[i])
                countspanishtrigramcase += createtrigram(copystring[i])
                countalphaspanish = combinedictionaries(countalphaspanish, createcountisalpha(copystring[i]))
                countalphabigramspanish = combinedictionaries(countalphabigramspanish,createbigramisalpha(copystring[i]))
                countalphatrigramspanish = combinedictionaries(countalphatrigramspanish,createtrigramisalpha(copystring[i]))

            elif (copytweets[i][2] == 'en'):
                countenglish += np.array(createcountsoflowercase(copystring[i]))
                numtweetenglish += 1
                countenglishcasesensitive += np.array(createcountsofloweranduppercase(copystring[i]))
                countenglishbigram += createbigramlower(copystring[i])
                countenglishbigramcase += createbigram(copystring[i])
                countenglishtrigram += createtrigramlower(copystring[i])
                countenglishtrigramcase += createtrigram(copystring[i])
                countalphaenglish = combinedictionaries(countalphaenglish, createcountisalpha(copystring[i]))
                countalphabigramenglish = combinedictionaries(countalphabigramenglish,createbigramisalpha(copystring[i]))
                countalphatrigramenglish = combinedictionaries(countalphatrigramenglish,createtrigramisalpha(copystring[i]))

            elif (copytweets[i][2] == 'pt'):
                countportogeuse +=np.array(createcountsoflowercase(copystring[i]))
                numtweetportoguse+=1
                countportogusecasesensitive += np.array(createcountsofloweranduppercase(copystring[i]))
                countportogusebigram += createbigramlower(copystring[i])
                countportogusebigramcase += createbigram(copystring[i])
                countportogusetrigram += createtrigramlower(copystring[i])
                countportogusetrigramcase += createtrigram(copystring[i])
                countalphaportoguse = combinedictionaries(countalphaportoguse, createcountisalpha(copystring[i]))
                countalphabigramportoguse = combinedictionaries(countalphabigramportoguse, createbigramisalpha(copystring[i]))
                countalphatrigramportoguse = combinedictionaries(countalphatrigramportoguse,createtrigramisalpha(copystring[i]))

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
    results.append(countportogeuse)

    results.append(countbasquecasesensitive)
    results.append(countcatalancasesensitive)
    results.append(countgaliciancasesensitive)
    results.append(countspanishcasesensitive)
    results.append(countenglishcasesensitive)
    results.append(countportogusecasesensitive)

    results.append(countbasquebigram)
    results.append(countcatalanbigram)
    results.append(countgalicianbigram)
    results.append(countspanishbigram)
    results.append(countenglishbigram)
    results.append(countportogusebigram)

    results.append(countbasquebigramcase)
    results.append(countcatalanbigramcase)
    results.append(countgalicianbigramcase)
    results.append(countspanishbigramcase)
    results.append(countenglishbigramcase)
    results.append(countportogusebigramcase)

    results.append(countbasquetrigram)
    results.append(countcatalantrigram)
    results.append(countgaliciantrigram)
    results.append(countspanishtrigram)
    results.append(countenglishtrigram)
    results.append(countportogusetrigram)

    results.append(countbasquetrigramcase)
    results.append(countcatalantrigramcase)
    results.append(countgaliciantrigramcase)
    results.append(countspanishtrigramcase)
    results.append(countenglishtrigramcase)
    results.append(countportogusetrigramcase)

    results.append(countalphabasque)
    results.append(countalphacatalan)
    results.append(countalphagalician)
    results.append(countalphaspanish)
    results.append(countalphaenglish)
    results.append(countalphaportoguse)

    results.append(countalphabigrambasque)
    results.append(countalphabigramcatalan)
    results.append(countalphabigramgalician)
    results.append(countalphabigramspanish)
    results.append(countalphabigramenglish)
    results.append(countalphabigramportoguse)

    results.append(countalphatrigrambasque)
    results.append(countalphatrigramcatalan)
    results.append(countalphatrigramgalician)
    results.append(countalphatrigramspanish)
    results.append(countalphatrigramenglish)
    results.append(countalphatrigramportoguse)

    totalnumtweets=numtweetbasque+numtweetcatalan+numtweetgalician+numtweetspanish+numtweetenglish+numtweetportoguse

    pbasque=numtweetbasque/(totalnumtweets)
    pcatalan=numtweetcatalan/(totalnumtweets)
    pgalician=numtweetgalician/(totalnumtweets)
    pspanish=numtweetspanish/(totalnumtweets)
    penglish=numtweetenglish/(totalnumtweets)
    pportoguse=numtweetcatalan/(totalnumtweets)


    results.append(pbasque)
    results.append(pcatalan)
    results.append(pgalician)
    results.append(pspanish)
    results.append(penglish)
    results.append(pportoguse)


    totalcharcountbasqe=totalcountlist(countbasque)
    totalcharcountcatalan = totalcountlist(countcatalan)
    totalcharcountgalician = totalcountlist(countgalician)
    totalcharcountspanish = totalcountlist(countspanish)
    totalcharcountenglish = totalcountlist(countenglish)
    totalcharcountportoguse = totalcountlist(countportogeuse)

    results.append(totalcharcountbasqe)
    results.append(totalcharcountcatalan)
    results.append(totalcharcountgalician)
    results.append(totalcharcountspanish)
    results.append(totalcharcountenglish)
    results.append(totalcharcountportoguse)
    return results




def calculatescores(mystring,smoothing,classsize,vocabularysize,totaldocs,traininglist):
    score=0
    for i in range(len(mystring)):
        if(ord(mystring[i]>=97 and ord(mystring[i]<=122))):
            score+=math.log((traininglist[ord(mystring[i])-97]+smoothing)/(classsize+vocabularysize*smoothing),10)
    score+=math.log(classsize/totaldocs,10)
    return score

def calculatescorescase(mystring,smoothing,classsize,vocabularysize,totaldocs,traininglist):
    score=0
    for i in range(len(mystring)):
        if((ord(mystring[i]>=97 and ord(mystring[i]<=122)))):
            score+=math.log((traininglist[ord(mystring[i])-97]+smoothing)/(classsize+vocabularysize*smoothing),10)
        elif ((ord(mystring[i]>=65 and ord(mystring[i]<=90)))):
            score += math.log((traininglist[ord(mystring[i]) - 39]+smoothing) / (classsize+vocabularysize * smoothing), 10)

    score+=math.log(classsize/totaldocs,10)
    return score

def calculatescorebigram(mystring,smoothing,classsize,vocabularysize,totaldocs,traininglist):
    score=0
    for i in range(len(mystring)-1):
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and (ord(mystring[i+1]) >= 97 and ord(mystring[i+1]) <= 122)):
            score+=math.log((traininglist[ord(mystring[i])-97][ord(mystring[i+1])-97]+smoothing)/((totalcountlist(traininglist[ord(mystring[i])-97]))+smoothing*vocabularysize))
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

def calculatescoretrigram(mystring, smoothing, classsize, vocabularysize, totaldocs, traininglist):
    score = 0
    for i in range(len(mystring) - 2):
        if ((ord(mystring[i]) >= 97 and ord(mystring[i]) <= 122) and ord(mystring[i+1]) >= 97 and ord(mystring[i+1]) <= 122 and ord(mystring[i+2]) >= 97 and ord(mystring[i+2]) <= 122):
            score+=math.log((traininglist[ord(mystring[i])-97][ord(mystring[i+1])-97][ord(mystring[i+2])-97]+smoothing)/((totalcountlist(traininglist[ord(mystring[i])-97][ord(mystring[i+1])-97]))+smoothing*vocabularysize))
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
            score += math.log((int(traininglist[mystring[i]]) + smoothing) / (classsize + vocabularysize * smoothing), 10)
        elif(mystring[i].isalpha() and not(mystring[i] in traininglist)):
            score+=math.log((smoothing) / (classsize + vocabularysize * smoothing), 10)

    score+=math.log(classsize/totaldocs,10)
    return score

def countlefttotalbigram(dic,leftchar):
    sum=0
    for i in dic:
        if(i[0]==leftchar):
            sum+=int(dic[i])
    return sum

def countrighttotalbigram(dic,rightchar):
    sum=0
    for i in dic:
        if(i[1]==rightchar):
            sum+=int(dic[i])
    return sum

def counttrigramtotal12(dic,one,two):
    sum=0
    for i in dic:
        if(i[0]==one and i[1]==two):
            sum+=int(dic[i])
    return sum

def counttrigramtotal13(dic,one,three):
    sum=0
    for i in dic:
        if(i[0]==one and i[2]==three):
            sum+=int(dic[i])
    return sum

def counttrigramtotal23(dic,two,three):
    sum=0
    for i in dic:
        if(i[1]==two and i[2]==three):
            sum+=int(dic[i])
    return sum




def calculatescoreisalphabigram(mystring, smoothing, classsize, vocabularysize, totaldocs, traininglist):
    score = 0
    for i in range(len(mystring)-1):
        if ((mystring[i].isalpha() and (mystring[i] in traininglist)) and (mystring[i+1].isalpha() and (mystring[i+1] in traininglist))):
            bigram=mystring[i]+mystring[i+1]
            score += math.log((int(traininglist[bigram]) + smoothing) / (countlefttotalbigram(traininglist,mystring[i]) + (vocabularysize+1 )* smoothing),10)
        elif  ((mystring[i].isalpha() and (mystring[i] in traininglist)) and (mystring[i+1].isalpha() and not (mystring[i+1] in traininglist))):
            score += math.log((smoothing) / (countlefttotalbigram(traininglist, mystring[i]) + (vocabularysize + 1) * smoothing), 10)
        elif  ((mystring[i].isalpha() and not (mystring[i] in traininglist)) and (mystring[i+1].isalpha() and  (mystring[i+1] in traininglist))):
            score += math.log( (smoothing) / ((vocabularysize + 1) * smoothing), 10)
        elif  ((mystring[i].isalpha() and not (mystring[i] in traininglist)) and (mystring[i+1].isalpha() and not (mystring[i+1] in traininglist))):
            score += math.log((smoothing) / ((vocabularysize + 1) * smoothing), 10)

    score += math.log(classsize / totaldocs, 10)
    return score




def calculatescoreisalphabigram(mystring, smoothing, classsize, vocabularysize, totaldocs, traininglist):
    score = 0
    for i in range(len(mystring)-2):
        if ((mystring[i].isalpha() and (mystring[i] in traininglist)) and (mystring[i + 1].isalpha() and (mystring[i + 1] in traininglist)) and (mystring[i + 2].isalpha() and (mystring[i + 2] in traininglist))):
            bigram = mystring[i] + mystring[i + 1]+mystring[i+2]
            score += math.log((int(traininglist[bigram]) + smoothing) / (counttrigramtotal12(traininglist,mystring[i],mystring[i+1]) + (vocabularysize + 1) * smoothing), 10)
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



'''
def naivebayes(v,n,delta,train,test):
    tweets= []
    with open(train) as f:
        for line in f:
            tweets.append(line)
    for i in range(len(tweets)):
        if (i < (len(tweets) - 1)):
            tweets[i] = tweets[i][:-1]
        tweets[i] = tweets[i].split()
    Basquecount=0
    Basquebigram
'''