def CS(l):
   if not l or len(l) == 1:
      return l
   else:
      return cs(l,1)
""" def cs(l,d):
   if d == len(l)+1:
    return l
   else:
    for i in range(d,len(l)):
        l[i]=l[i-d]+l[i]
    
    return cs(l,d+1) """
def cs(l, d):
    if d == len(l) + 1:
        return l
    else:
        for i in range(d, len(l)):
            l[i] = l[i - d] + l[i]

        return cs(l, d + 1) 


a=[1,2,3,4,5,6,7,8]
print (sum(a))
print(CS(a))

