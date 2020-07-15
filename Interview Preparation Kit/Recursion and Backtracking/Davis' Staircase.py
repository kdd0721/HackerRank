import unittest
from itertools import permutations, combinations

def memoize(f):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function

@memoize
def stepPerms(n):
    if n<0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:   
        return (stepPerms(n-3) + stepPerms(n-2) + stepPerms(n-1))%10000000007
                

class TestMethod(unittest.TestCase):
    def test_stepPerms(self):
        self.assertEqual(stepPerms(1),1)
        self.assertEqual(stepPerms(3),4)
        self.assertEqual(stepPerms(7),44)

if __name__=="__main__":
    print(stepPerms(36))
    #unittest.main()