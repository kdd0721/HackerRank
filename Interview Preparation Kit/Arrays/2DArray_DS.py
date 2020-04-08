#https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
import unittest

def hourglassSum(arr):
    sum = -9999
    for a in range(len(arr)-2):
        for b in range(len(arr)-2):
            temp = arr[a][b]+arr[a][b+1]+arr[a][b+2]\
                    +arr[a+1][b+1]\
                    +arr[a+2][b]+arr[a+2][b+1]+arr[a+2][b+2]
            if temp>sum:
                sum=temp
    return sum

class TestMethods(unittest.TestCase):
    def test_hourglassSum(self):
        self.assertEqual(hourglassSum([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]),19)

if __name__=="__main__":
    print(hourglassSum([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]))
    unittest.main()