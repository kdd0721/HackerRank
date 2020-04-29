import unittest
from itertools import combinations

def minimumAbsoluteDifference(arr):
    arr.sort()
    return min(abs(x-y) for x,y in zip(arr,arr[1:]))
                

class TestMethod(unittest.TestCase):
    def test_minimumAbsoluteDifference(self):
        self.assertEqual(minimumAbsoluteDifference([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]),1)
        self.assertEqual(minimumAbsoluteDifference([1, -3, 71, 68, 17]),3)
        self.assertEqual(minimumAbsoluteDifference([3, -7, 0]),3)

if __name__=="__main__":
    print(minimumAbsoluteDifference([3, -7, 0]))
    unittest.main()