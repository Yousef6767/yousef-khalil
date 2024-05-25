dNumber=[]
biNumber=[]
z=0
while True:
    x=input("enter number")
    for i in range(len(x)):
        if x[i]=='0' or x[i]=='1' :
            a=int(x[i])
            z=a*2**(len(x)-i-1)
            biNumber.append(x[i])
            dNumber.append(z)
        else:
            print('invaled input')
            break
    print("the number is:",x[:],sum(dNumber[:]))
    x=input('prees any key to continue or f to finsh')
    desmantNumber.clear()
    if x=='F' or x=='f':
        break
print('finsh')