def contador(i):
    if i <= 0:
        return 0
    else:
        print(i, end=' ')
        return contador(i-1)

contador(10) # 10 9 8 7 6 5 4 3 2 1
    