n=input()
l=list(n.split())
for i in range(len(l)):
    l[i]=l[i][::-1]
    print(l[i],"",end ="")    