'''author - Kunal Singh'''

import nltk
import math
import os
from nltk.tokenize import RegexpTokenizer


def readfile(path):
    file=open(path,'r',encoding='utf8')
    p1=''
    for lines in file:
        p1+=lines
    file.close()
    return p1

def readdata(p1):
    p1=p1.lower()
    tokenizer=RegexpTokenizer(r'\w+')
    t1=tokenizer.tokenize(p1)
    return t1
def cossim(t1,t2,t3):

    li1=[0 for i in range(0,len(t3))]
    li2=[0 for i in range(0,len(t3))]
    for i in range(0,len(t3)):
        if(t3[i] in t1):
            count=0
            for j in t1:
                if(j == t3[i]):
                    count+=1
            li1[i]+=count
        if(t3[i] in t2):
            count=0
            for j in t2:
                if(j == t3[i]):
                    count+=1
            li2[i]+=count
    mag1=0
    mag2=0
    sum1=0
    sum2=0
    for i in li1:
        sum1+=i*i
    for i in li2:
        sum2+=i*i
    mag1=math.sqrt(sum1)
    mag2=math.sqrt(sum2)
    dot=0
    for i in range(0,len(t3)):
        dot+=li1[i]*li2[i]
    sim=dot/(mag1*mag2)
    return sim
    
path1=os.getcwd()+"\\text\\t1.txt"
path2=os.getcwd()+"\\text\\t2.txt"
path3=os.getcwd()+"\\text\\t3.txt"
p1=readfile(path1)
p2=readfile(path2)
p3=readfile(path3)
t1=readdata(p1)
t2=readdata(p2)
t3=readdata(p3)
head=set(t1+t2+t3)
head=list(t3)
lis=[t1,t2,t3]
for i in range(0,3):
    for j in range(0,3):
        print('similarity for doc',i+1,' and doc',j+1,' is ',cossim(lis[i],lis[j],head))





