a="abcdeabc"
b="abc"
lista=list(a)
listb=list(b)
x=len(b)
y=len(lista)
i=0
num=0
x1=""
while i<=y-2:
    if listb==lista[i:i+3]:
        num=num+1
    else:
        pass
    i=i+1
print(num)

