while True:
    print('''1 for addition
2 for subtraction
3 for multiplication
4 for division
5 for modulus
6 quit''')
    a=int(input('enter your choice:'))
    if a==6:
        break 
    print('enter two numbers:')
    n1=float(input())
    n2=float(input())
    
    if a==1:
        print('the sum is:',n1+n2)
    elif a==2:
        print('the difference is:',n1-n2)
    elif a==3:
        print('the product is:',n1*n2)
    elif a==4:
        print('the quotient is:',n1/n2)
    elif a==5:
        print('the remainder is:',n1%n2)
    else:        
        print('invalid choice')
