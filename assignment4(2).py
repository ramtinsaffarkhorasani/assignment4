import random
def besc(a, b, c):
        d = []
        e = random.randint(b, c)
        for x in range(a): 
            while e in d:
               d = random.randint(b, c)  
            d.append(e)   
        d.sort()
        print(d)
        return d
a=int(input("chand ta addad"))
v=int(input("az chand?"))
x=int(input("ta chand"))
besc(a,v,x)