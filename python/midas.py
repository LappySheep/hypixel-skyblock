import random as z
def midas():
 if z.choices([1,0],weights=[1,99]):r,l=10**4,5000;A=z.randint(0,9999);return z.randint(*[(100*r,l*r),(25*r,100*r),(5*r,25*r),(l,5*r),(1000,l),(100,1000)][min([i if(A<b)else 9for i,b in enumerate([1,9,90,400,2500,r])])])
