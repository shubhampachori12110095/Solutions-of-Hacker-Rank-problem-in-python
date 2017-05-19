K = int(raw_input())
for i in range(K):
    s = list(str(raw_input().strip().split())[2:-2])
    if  list(reversed(s))==s:
        print -1
    else:
        for j in range(len(s)//2):
            if (s[j] != s[len(s)- j -1]):
                 break
        del s[j]
        if list(reversed(s))==s:
            print j
        else:
            print len(s)-j               