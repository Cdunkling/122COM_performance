import sys, time
from datetime import datetime

def fast_math_function(a, b):
    time.sleep(0.00001)
    return a + b

def slow_math_function(a, b):
    time.sleep(1)
    return a + b

def main():
    start = datetime.now()
    slow_math_function(42, 69)
    delta = datetime.now() - start
    print( 'Slow math took %fs' % \
        delta.total_seconds() )

    start = datetime.now()
    for i in range(10000):
        fast_math_function(42,69)
    delta = datetime.now() - start
    print( 'Fast math took %fs' % \
        delta.total_seconds() )

if __name__ == '__main__':
    sys.exit(main())
