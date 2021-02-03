

from math import pow

for _ in range(int(input())):

    n, a, b = map(int, input().split())
    p=a+b
    r = (pow(2,0)*(p));  r = r % 10;
    s = (pow(2,1)*(p));  s = s % 10;
    t = (pow(2,2)*(p));  t = t % 10;
    u = (pow(2,3)*(p));  u = u % 10;
    v = (pow(2,4)*(p));  v = v % 10;
    val = (s+t+u+v);
    rem = (k-3)%4;
    ans = (k-3)/4;
    sp = sp + p + r;
    if(rem == 1)  sp = sp + s;
    if(rem == 2)  sp = sp + t + s;
    if(rem == 3)  sp = sp + u + s + t;
    if(sp % 3 == 0):
        
        print("YES")
    else :
        print("NO")

    
    
    
    
    
