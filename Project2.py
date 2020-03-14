import numpy as np
import math

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



def calculatecount(train):
    tweets = []
    countbasque=[0]*26
    countcatalan=[0]*26
    countgalician=[0]*26
    countspanish=[0]*26
    countenglish=[0]*26
    countportogeuse=[0]*26
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
            for k in range(3,len(copytweets[i])):
                copystring[i]=copystring[i]+copytweets[i][k]
            if(copytweets[i][2]=='eu'):
                countbasque+=np.array(createcountsoflowercase(copystring[i]))
            elif(copytweets[i][2]=='ca'):
                countcatalan +=np.array(createcountsoflowercase(copystring[i]))
            elif(copytweets[i][2]=='gl'):
                countgalician+=np.array(createcountsoflowercase(copystring[i]))
            elif (copytweets[i][2] == 'es'):
                countspanish += np.array(createcountsoflowercase(copystring[i]))
            elif (copytweets[i][2] == 'en'):
                countenglish +=np.array(createcountsoflowercase(copystring[i]))
            elif (copytweets[i][2] == 'pt'):
                countportogeuse +=np.array(createcountsoflowercase(copystring[i]))
        else:
            copytweets[i] = tweets[i].split()
            for k in range(3, len(copytweets[i])):
                copystring[i] = copystring[i] + copytweets[i][k]
            if (copytweets[i][2] == 'eu'):
                countbasque +=np.array( createcountsoflowercase(copystring[i]))
            elif (copytweets[i][2] == 'ca'):
                countcatalan +=np.array(createcountsoflowercase(copystring[i]))
            elif (copytweets[i][2] == 'gl'):
                countgalician +=np.array(createcountsoflowercase(copystring[i]))
            elif (copytweets[i][2] == 'es'):
                countspanish +=np.array(createcountsoflowercase(copystring[i]))
            elif (copytweets[i][2] == 'en'):
                countenglish += np.array(createcountsoflowercase(copystring[i]))
            elif (copytweets[i][2] == 'pt'):
                countportogeuse += np.array(createcountsoflowercase(copystring[i]))
    results.append(countbasque)
    results.append(countcatalan)
    results.append(countgalician)
    results.append(countspanish)
    results.append(countenglish)
    results.append(countportogeuse)
    return results


myresults=calculatecount("tec.txt")
print(myresults[0])
print(myresults[1])
print(myresults[2])
print(myresults[3])
print(myresults[4])
print(myresults[5])

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