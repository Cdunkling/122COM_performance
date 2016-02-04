import sys, time

def fast_math_function(a, b):
    time.sleep(0.00001)
    return a + b

def slow_math_function(a, b):
    time.sleep(3)
    return a + b

def main():
    slow_math_function(42, 69)
    
    for i in range(100000):
        fast_math_function(42,69)
    
if __name__ == '__main__':
    sys.exit(main())