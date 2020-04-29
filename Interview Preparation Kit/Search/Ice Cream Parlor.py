import unittest

def whatFlavors(cost, money):
    dic = {}
    for i, a in enumerate(cost):
        if a in dic:
            return (dic[a],i+1)
        else:
            dic[money-a] = i+1
                

class TestMethod(unittest.TestCase):
    def test_whatFlavors(self):
        self.assertEqual(whatFlavors([1, 4, 5, 3, 2], 4),'1 4')
        self.assertEqual(whatFlavors([2, 2, 4, 3], 4),'1 2')

if __name__=="__main__":
    print(whatFlavors([1, 4, 5, 3, 2], 4))
    #unittest.main()