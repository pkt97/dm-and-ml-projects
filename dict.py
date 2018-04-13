import pprint as pp
from collections import Counter
import math
dict1={}
dict2={}
dict3={}

m={"hello","to","all"}

f=open("1.txt","r")
a=Counter(f.read().split())
dict1=dict(a)
pp.pprint(dict1)

g=open("2.txt","r")
b=Counter(g.read().split())
dict2=dict(b)
pp.pprint(dict2)

h=open("3.txt","r")
c=Counter(h.read().split())
dict3=dict(c)
pp.pprint(dict3)

d=0 #for refering the dictionary
e=0 #for refering the files

def score1():
  score11={}
  score1=0
#  d=0
 # e=0
  for d in m: #m is the dictionary created and d points to the created dictionary
    for e in dict1: #dict1 is the dictionary of 1.txt e points to 1.txt's dictionary
      if (e==d):
        score1=score1+1
    score11[d]=score1    
  return score11
  
def score2():
  score21={}
  score2=0
  #d=0
  #e=0
  for d in m:
    for e in dict2:
      if(e==d):
        score2=score2+1
    score21[d]=score2
  return score21
  
def score3():
  score31={}
  score3=0
  #d=0
  #e=0
  for d in m:#searching for dictionary created
    for e in dict3: #searching for dictionary due to text files 
      if(e==d):
        score3=score3+1
    score31[d]=score3  
  return score31
  
def Cosine(o,p):
  num=0
  den1=0
  den2=0
  
  for e in p:
    num=num+(o[e]*p[e])
    den1=den1+(o[e]**1/2)
    den2=den2+(p[e]**1/2)
  
  return (num/(den1*den2))
  
print("Score for first file is",score1())
print("Score for second file is",score2())
print("Score for third file is",score3())

final=Cosine(score1(),score2())


"""final1=math.cos(score1())
final2=math.cos(score2())
final=final1+final2
"""
if (final>0.5):
  print("Files are similar because final value is",str(final))
else:
  print("Files are dissimilar because final value is",str(final))
  
  

