import unittest

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
                

class TestMethod(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(3),2)

if __name__=="__main__":
    print(fibonacci(3))
    unittest.main()