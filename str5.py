cnp=str(input('introdu CNP'))
n=0
if ((len(cnp<13))or(len(cnp>13))):
    print('cnp-ul nu corespunde cerintelor')
else:
    for n in cnp:
        if ord(n) in range(48,58):
            n+=1
        if(n==13):
            print('cnp-ul corespunde cerintelor')
        else:
            print('cnp-ul nu corespunde cerintelor')