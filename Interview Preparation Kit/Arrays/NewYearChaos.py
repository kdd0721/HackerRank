#https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen
import unittest
import math

def minimumBribes(q):
    count = 0
    for i, n in enumerate(q):
        if n-(i+1)>2:
            print("Too chaotic")
            return "Too chaotic"
        for j in range(max(0,n-2),i):
            if q[j]>n:
                count += 1
    print(count)
    return count

class TestMethod(unittest.TestCase):
    def test_minimumBribes(self):
        self.assertEqual(minimumBribes([2,1,5,3,4]),3)
        self.assertEqual(minimumBribes([2,5,1,3,4]),"Too chaotic")

if __name__=="__main__":
    minimumBribes([2,1,5,3,4])
    unittest.main()
