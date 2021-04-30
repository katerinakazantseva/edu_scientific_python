
p=1
N = raw_input('')
x = raw_input('')
s = raw_input('')




def calc_P(string,N, GC):
    p=1
    pGC = float(x) / 2
    pAT = (1 - float(x)) / 2
    for i in range(0,(len(s))):
        if s[i]=="A" or s[i]== "T":
            p=p*pAT
        else:
            p=p*pGC
    print (1-((1-p)**int(N)))

calc_P(s, N, x)