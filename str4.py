a=input('introduceti primul cuvant')
b=input('introduceti al doilea cuvant')
c=input('introduceti al treilea cuvant')
d=input('introduceti al patrulea cuvant')
if (len(a)<3) or (len(b)<3) or (len(c)<3) or (len(d)<3):
    print("eroare")
l1=a[:1]
l2=a[:2]
l3=b[:1]
l4=c[:1]
l5=c[:2]
l6=c[:3]
l7=d[:(len(d)//2)]
print('cuvintle sunt',a,b,c,d)
print('cuvantul format este',l1+l2+l3+l4+l5+l6+l7)
