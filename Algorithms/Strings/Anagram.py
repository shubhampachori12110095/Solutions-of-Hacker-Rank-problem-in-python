K = int(raw_input())
for i in xrange(K):
    j = str(raw_input().strip().split())[2:-2]
    a = [0]*26
    b = [0]*26
    if (len(j) % 2 != 0):
        print -1
    else:
        x = j[:len(j)//2]
        y = j[len(j)//2:]
        for i in range(len(x)):
            a[ord(x[i]) -  ord('a')] = a[ord(x[i]) -  ord('a')] + 1
        for i in range(len(y)):
            b[ord(y[i]) -  ord('a')] = b[ord(y[i]) -  ord('a')] + 1  
        for i in range(len(a)):
             a[i] = a[i] - b[i]
        a = filter(lambda x : x>0, a)        
        print(sum(a))    