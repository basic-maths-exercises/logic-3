import numpy as np

def numberLessThan( data, n ) :
  nnn = 0
  for i in range(len(data)) :
    if data[i]<n : nnn = nnn + 1
  return nnn
  
def numberMoreThan( data, n ) :
  nnn = 0
  for i in range(len(data)) :
    if data[i]>n : nnn = nnn + 1
  return nnn  
  
data = np.loadtxt("mydata.dat") 
# You need to fix the code in the loop below so that the propositions printed out 
# by the code are true.
nnn, mmm, kkk = 0, 0, 0   
for i in range(len(data)) : 
  if data[i] < 5 : nnn = nnn + 1
  elif data[i] > 4 : mmm = mmm + 1
  else : kkk = kkk + 1
  
print("If code is working correctly", nnn, "should equal", numberLessThan(data,5))
print("If code is working correctly", mmm, "should equal", numberMoreThan(data,4))
print("If code is working correctly", kkk, "should equal", len(data) - numberLessThan(data,5))
