import random
n = int(input("Enter the number of friends joining (including you):\n"))
if n<=0:
    print("\nNo one is joining for the party")
else:
    d=dict()
    print("\nEnter the name of every friend (including you), each on a new line:")
    for i in range(n):
        d[input()]=''
    m = int(input("\nEnter the total bill value:\n"))
    for i in d:
        d[i]=round(m/n, 2)
    print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    winner = random.choice(list(d.keys()))

    if input()=='Yes':
        print(f'{winner} is the lucky one!\n')
        for i in d:
            if i!=winner:
                d[i]=round(m/(n-1), 2)
            else:
                d[i]=0
        print(f'\n{d}')
    else:
         print(f'No one is going to be lucky\n{d}')
