#https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen
import unittest

def alternatingCharacters(s):
    count = 0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count+=1
    return count

class TestMethod(unittest.TestCase):
    def test_alternatingCharacters(self):
        self.assertEqual(alternatingCharacters('AAABBB'),4)
        self.assertEqual(alternatingCharacters('AAAA'),3)
        self.assertEqual(alternatingCharacters('BABABA'),0)

if __name__=="__main__":
    print(alternatingCharacters('AAABBB'))
    unittest.main()