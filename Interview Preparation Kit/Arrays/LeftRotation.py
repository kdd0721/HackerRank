#https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
import unittest

def rotLeft(a, d):
    shifted_arr = [0]*len(a)
    for i in range(len(a)):        
        if len(a)-d+i<len(a):
            shifted_arr[len(a)-d+i]=a[i]
        else:
            shifted_arr[i-d]=a[i]
    return shifted_arr

class TestMethod(unittest.TestCase):
    def test_rotLeft(self):
        self.assertEqual(rotLeft([1,2,3,4,5],4),[5,1,2,3,4])

if __name__=="__main__":
    print(rotLeft([1,2,3,4,5],2))
    unittest.main()