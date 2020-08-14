import itertools
a=input("")    
s=input("")
t=list(itertools.permutations(s,len(s)))
t.reverse()

res = [(t[0])]
print(str(res))






