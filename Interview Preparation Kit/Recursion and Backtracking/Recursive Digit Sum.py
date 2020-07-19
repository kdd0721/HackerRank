import unittest

def superDigit(n, k):
    return recursive(str(sum(int(s) for s in n) * k))

def recursive(n):
    if len(n)==1:
        return n
    else:
        return recursive(str(sum([int(s) for s in list(n)])))
                

class TestMethod(unittest.TestCase):
    def test_superDigit(self):
        self.assertEqual(superDigit('9875', 4),'8')
        self.assertEqual(superDigit('123', 3),'9')

if __name__=="__main__":
    print(superDigit('9875',4))
    unittest.main()