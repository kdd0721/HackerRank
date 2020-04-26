#https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import unittest

def isValid(s):
    f_list = []
    for i in set(s):
        f_list.append(s.count(i))

    f_map = {}
    for i in set(f_list):
        f_map[i] = f_list.count(i)
    
    max_value = max(f_map.keys())
    min_value = min(f_map.keys())
    if len(f_map)==1:
        return 'YES'
    elif len(f_map)==2:
        if max_value-min_value==1 and f_map[max_value]==1:
            return 'YES'
        elif f_map[min_value]==1:
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'

class TestMethod(unittest.TestCase):
    def test_isValid(self):
        self.assertEqual(isValid('aabbcd'),'NO')
        self.assertEqual(isValid('aabbccddeefghi'),'NO')
        self.assertEqual(isValid('abcdefghhgfedecba'),'YES')

if __name__=="__main__":
    print(isValid('xxxaabbccrry'))
    unittest.main()