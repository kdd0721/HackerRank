import unittest
from itertools import combinations 

def miniMaxSum(arr):
    com = list(sum(a) for a in combinations(arr,4))
    print(min(com),max(com))
    return min(com),max(com)

class TestMethod(unittest.TestCase):
    def test_miniMaxSum(self):
        self.assertEqual(miniMaxSum([1,2,3,4,5]),(10, 14))

if __name__=="__main__":
    print(miniMaxSum([1,2,3,4,5]))
    unittest.main()