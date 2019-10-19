def song(count_line=3, count_la=3, sign=0):

    for count_l in range(0,count_line-1):
        for count_j in range(0,count_la-1):
            print ('la','', sep='-',end='')

        print ("la",end='\n')
    for count_j in range(0, count_la - 1):
        print('la','', sep='-',end='')

    if (sign==0):
        print("la.")
    else:
        print("la!")

l=song(3,3,1)
print('s','v', sep='-')
    # if sign==0:
    #     retu