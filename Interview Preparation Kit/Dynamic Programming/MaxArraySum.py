#https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming
import unittest

def maxSubsetSum(arr):
    for i in range(2,len(arr)):
        temp_num = arr[i]
        arr[i]=max(arr[i]+arr[temp] for temp in range(i-1))
        if arr[i]<temp_num:
            arr[i]=temp_num
    print(arr)
    return max(arr)

class TestMethods(unittest.TestCase):
    def test_maxSubsetSum(self):
        self.assertEqual(maxSubsetSum([3,5,-7,8,10]),15)
        self.assertEqual(maxSubsetSum([2,1,5,8,4]),11)
        self.assertEqual(maxSubsetSum([3,7,4,6,5]),13)
        self.assertEqual(maxSubsetSum([-2,1,3,-4,5]),8)

if __name__=="__main__":
    print(maxSubsetSum([-2,1,3,-4,5]))
    unittest.main()