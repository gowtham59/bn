a1=int(input())
b2=0
while 2**b2 < a1:
    b2=b2+1
if 2**b2 == a1:
    print(0)
elif a1-2**(b2-1)<=2**b2-a1:
    print(a1-2**(b2-1))
else:
    print(2**b2-a1)
