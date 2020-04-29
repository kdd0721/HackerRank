import unittest

def pairs(k, arr):
    return len(set(a+k for a in arr).intersection(set(arr))) 
                

class TestMethod(unittest.TestCase):
    def test_pairs(self):
        self.assertEqual(pairs(2,[1, 5, 3, 4, 2]),3)

if __name__=="__main__":
    print(pairs(2,[1, 5, 3, 4, 2]))
    unittest.main()