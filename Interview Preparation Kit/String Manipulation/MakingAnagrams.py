#https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
import unittest

def makeAnagram(a, b):
    intersec = set(a).intersection(b)
    anagram = sum(min(a.count(c),b.count(c)) for c in intersec)
    return len(a)+len(b)-2*anagram

class TestMethod(unittest.TestCase):
    def test_makeAnagram(self):
        self.assertEqual(makeAnagram('fcrxzwscanmligyxyvym','jxwtrhvujlmrpdoqbisbwhmgpmeoke'),30)

if __name__=="__main__":
    print(makeAnagram('fcrxzwscanmligyxyvym','jxwtrhvujlmrpdoqbisbwhmgpmeoke'))
    unittest.main()