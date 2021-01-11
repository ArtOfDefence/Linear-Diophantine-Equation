print("Primer a+b=c")
print("Ukucajte vrednost a")
a = int(input())
print("Ukucajte operaciju - ili +")
v=input()
print("Ukucajte vrednost b")
b = int(input())
print("Ukucajte vrednost c")
c = int(input())
d=a
f=b
if v=="-":
    print(a, "-", b, "=", c)
else:
    print(a, "+", b, "=", c)
q=-1
lista1=[]
lista2=[]
lista3=[]
lista4=[]
while q !=0:
    lista1.append(a)
    lista2.append(b)
    lista4.append(a//b)
    q= a%b
    lista3.append(q)
    a=b
    b=q
w=0
while w!=len(lista1):
    print (lista1[w], "=", lista4[w], "*", lista2[w], "+", lista3[w])
    w+=1
print("NZD je " ,lista3[-2])
if c%lista3[-2]==0:
    print(lista3[-2],"je deljivo sa",c,"jednacina moze da se nastavi.")
else:
    print(lista3[-2],"nije deljivo sa ",c,"jednacina ne moze da se nastavi.")
    input()
def f1(n):
    return n* -1
lista5=list(map(f1,lista4[::-1]))
e=lista3[-2]
r=1
t=2
y=-2
u=lista5[1]
lista6=[u]
p=0
s=1
while y!=-len(lista1):
    print(e,"=", r,"*",lista1[y],u,"*",lista2[y])
    if lista5[t]>=0:
        print(e, "=", r, "*", lista1[y], u, "*", "(", s, "*", lista1[y - 1],"+", lista5[t], "*", lista2[y - 1], ")")
    else:
        print(e, "=", r, "*",lista1[y],u,"*", "(", s, "*", lista1[y-1], lista5[t],"*",lista2[y-1],")")
    if (u*lista5[t])>=0:
        print(e,"=",r,"*",lista1[y],u,"*",lista1[y-1],"+",(u*lista5[t]),"*",lista2[y-1])
    else:
        print(e, "=", r, "*", lista1[y], u, "*", lista1[y - 1],(u * lista5[t]), "*",lista2[y - 1])
    u=r+(u*lista5[t])
    lista6.append(u)
    r=lista6[p]
    p+=1
    y-=1
    t+=1
if len(lista6)==1:
    print(e,"=",1,"*",d,lista6[-1],"*",f)
    print(e, "=", 1, "*", d, lista6[-1], "*", f, "/","*",int(c/e))
    print(int(c/e),"*",d,int(lista6[-1]*c/e),"*",f,"=",c)
    k=c/e*1
    if v=="-":
        uu=-lista6[-1]*c/e
    else:
        uu=lista6[-1]*c/e
    print("Xo= ",int(k))
    print("Yo = ", int(uu))
    if v=="-":
        print("X = ", int(k),"-", int(f),"t")
        x=k-f*1
    else:
        x=k+f*1
        print("X = ", int(k), "+", int(f), "t")
    y=uu-d
    print("Y = ", int(uu), "-", d,"t")
    if v == "-":
        print(d, "*", int(x), "-", f, "*", int(y), "=", c)
        if (d * x - f * y) == c:
            print("Jednacina je diofantska")
    else:
        print(d, "*", int(x), "+", f, "*", int(y), "=", c)
        if (d * x + f * y) == c:
            print("Jednacina je diofantska")
    input()
if lista6[-1]>0:
    print(e,"=",lista6[-2],"*",d,"+",lista6[-1],"*",f)
else:
    print(e, "=", lista6[-2], "*", d, lista6[-1], "*", f)
if lista6[-1]>0:
    print(lista6[-2],"*",d,"+",lista6[-1],"*",f,"/","*",int(c/e))
else:
    print(lista6[-2], "*", d, lista6[-1], "*", f,"/","*",int(c/e))
if lista6[-1]>0:
    print(lista6[-2]*int(c/e), "*", d,"+",lista6[-1] * int(c/e),"*",f,"=",c )
else:
    print(lista6[-2] * int(c / e), "*", d, lista6[-1] * int(c / e), "*",f, "=", c)
l=(lista6[-2] * int(c / e))
if v=="-":
    m=-(lista6[-1] * int(c / e))
else:
    m =(lista6[-1] * int(c / e))
print("Xo = ", l)
print("Yo = ", m)
if v=="-" :
    print("X = " ,l,"-",int(f/e),"t")
    x=l-f/e*1
else:
    x=l+f/e*1
    print("X = ", l, "+", int(f / e), "t")
print("Y = ", m, "-", int(d / e), "t")
y=m-d/e*1
if v=="-":
    print(d,"*",int(x),"-", f,"*",int(y), "=", c)
    if(d*x - f*y)==c:
        print("Jednacina je diofantska")
else:
    print(d,"*",int(x), "+",f,"*",int(y), "=", c)
    if(d*x + f*y)==c:
        print("Jednacina je diofantska")
print("Pritisnite ENTER da izadjete.")
input()









