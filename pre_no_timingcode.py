import sys, time

def fast_math_function(a, b):
    time.sleep(0.00001)
    return a + b

def slow_math_function(a, b):
    time.sleep(1)
    return a + b

def main():
    print('Running slow_math_function()')
    slow_math_function(42, 69)
    
    print('Running fast_math_function()')
    for i in range(10000):
        fast_math_function(42,69)
    
if __name__ == '__main__':
    sys.exit(main())
