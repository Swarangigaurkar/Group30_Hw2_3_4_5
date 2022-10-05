#github-action genshdoc
from csv_parser import the
import math
import random
#!/bin/bash
#@file Numeric Class, summarizes a stream of numbers
class Num:
  
  #@Initialization
  def __init__(self,c=0,s=""):
    self.n=0
    self.at=c
    self.name=s
    self._has=[]
    self.lo=math.inf
    self.hi=-math.inf
    self.isSorted=True
    if(s==""):
      w=0
    elif(s[-1]=='+'):
      w=1
    elif(s[-1]=='-'):
      w=-1
    else:
      w=0
  
  #@Sort the kept list of numbers
  def nums(self):
    if self.isSorted==False:
      self._has.sort()
      self.isSorted=True
    return self._has
  
  #@Keep at most a fixed number of numbers, if we run out of room delete numbers at random
  def add (self, v, nums): 
      if v!="?":
          self.n += 1
          if self.lo > v:  
              self.lo=v
          if self.hi < v: 
              self.hi=v
          if len(self._has) < nums: 
              pos=len(self._has)
          elif random.uniform(0, 1) < nums/self.n:
              pos=random.randint(0, len(self._has) - 1)               
          if 'pos' in locals(): 
              self.isSorted=False
              if pos < len(self._has):
                  self._has[pos]=float(v) 
              else:
                  self._has.insert(pos, float(v)) 
          return
        
  #@Calculate the Standard Deviation of the list of numbers
  def div(self):
    a=self.nums()
    index_90th=int(len(a)*0.9)
    index_10th=int(len(a)*0.1)
    return (a[index_90th]-a[index_10th])/2.58
  
  #@Calculate the Median of the list of numbers
  def mid(self):
    a=self.nums()
    index_50th=int(len(a)*0.5)
    return a[index_50th]
