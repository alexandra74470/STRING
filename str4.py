a=input('introduceti primul cuvant')
b=input('introduceti al doilea cuvant')
c=input('introduceti al treilea cuvant')
d=input('introduceti al patrulea cuvant')
if (len(a)<3) or (len(b)<3) or (len(c)<3) or (len(d)<3):
    print("eroare")
l1=a[:2]
l2=b[0]
l3=c[:3]
l4=d[:(len(d)//2)]
print('cuvintle sunt',a,b,c,d)
print('cuvantul format este',l1+l2+l3+l4)
