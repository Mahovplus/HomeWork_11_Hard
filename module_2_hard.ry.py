def zagadka(n):
    key_ = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                key_ += str(i) + str(j)
    return key_
print('Enter number: ')
print(zagadka(int(input())))