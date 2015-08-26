#this test will throw an exception

import sys


def infinity(numerator, denominator):
    try:
        num = numerator/denominator
    except ZeroDivisionError:
        print "Cannot integer divide: Infinity is not an integer =(\n"
        exit(1)
    else:
        print "number is %d" % num

        
x = sys.argv[1]
y = sys.argv[2]

print "Gonna fail now T__T"
infinity(int(x), int(y))