
stockprices = [10, 11, 12, 16, 9, 11, 13]

def BiggestGains(a):
    minvalue = a[0]
    maxdiff = 0
    for i in range(len(a)):
        # takes min value vmin on the left, compare with values to the right of it & store max diff
        # when new min value appears, it will take that new min value and compare with val to the right
        if (a[i] < minvalue):
            minvalue = a[i]
        elif (a[i] - minvalue > maxdiff):
            maxdiff = a[i] - minvalue
    return maxdiff



print ("Maximum possible gain is: " + str(BiggestGains(stockprices)))