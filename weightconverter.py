weight=float(input('enter weight ='))
m=str(input(f'{weight} is in pound or kg: '))
c='pound'
c1='POUND'
c3='Pound'
d='kg'
d1='KG'
d2='Kg'
d3='kG'
if m==c or m==c1 or m==c3:
    print(f'wieght is{weight/2.205}KG')
elif m==d or m==d1 or m==d2 or m==d3:
    print(f'weight is{weight * 2.205}pounds')
else:
    print('enter correct input')
