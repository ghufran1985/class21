def onsquaretime(n):
    iteration = 0
    for i in range(0, n):
        for j in range(0, n):
            print('*',end=' ')
            iteration = iteration + 1
        print('')
    print('when n is ',n,'iteration =',iteration,'\n')
onsquaretime(5)
onsquaretime(14)