import sys, timeit, time

def n_sum(sequence):
    total = 0
    for i in range(len(sequence)):
        total += sequence[i]
        time.sleep(0.001)
    return total

def n2_sum(sequence):
    total = 0
    for i in range(len(sequence)):
        counter = 0
        while counter < i:
            counter += 1
        total += sequence[counter]

    return total


if __name__ == '__main__':
    
    
    n = 1
    for i in range(100):
        n *= 2

        a = [ i for i in range(n) ]

        nStart = timeit.default_timer()
        n_sum( a )
        nTook = timeit.default_timer() - nStart

        n2Start = timeit.default_timer()
        n2_sum( a )
        n2Took = timeit.default_timer() - n2Start

        print('%d\t%f\t%f' % (n,nTook,n2Took))