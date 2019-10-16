import unittest
import leetcode_solutions as ls

class test_moviesOnFlight(unittest.TestCase):
    print("Test moviesOnFlight")
    def test_one(self):
        movieDurations = [10,20, 50,30, 90,100]    #[60,75,85,90,120,125,150]
        d = 150
        pair = ls.moviesOnFlight(movieDurations, d)
        self.assertEqual(pair,[1,5])

    def test_two(self):
        movieDurations = [10,20, 50,30, 90,100]    #[60,75,85,90,120,125,150]
        d = 140
        pair = ls.moviesOnFlight(movieDurations, d)
        self.assertEqual(pair,[0,5])

class test_isValid(unittest.TestCase):
    def test_zero(self):
        s = ""
        self.assertTrue(ls.isValid(s))
    def test_one(self):
        s = "()[]{}"
        self.assertTrue(ls.isValid(s))
    def test_two(self):
        s = "(]"
        self.assertFalse(ls.isValid(s))
    def test_three(self):
        s = "([)]"
        self.assertFalse(ls.isValid(s))
    def test_four(self):
        s = "{[]}"
        self.assertTrue(ls.isValid(s))

class TestMaxSubArray(unittest.TestCase):
    def test_five(self):
        lst = [-2,1,-3,4,-1,2,1,-5,4]
        self.assertEquals(6, ls.maxSubArray(lst))


class test_groupAnagrams(unittest.TestCase):
    def test_one(self):
        lst = ["eat", "tea", "tan", "ate", "nat", "bat"]
        self.assertEquals([['tan', 'nat'], ['bat'], ['eat', 'tea', 'ate']], ls.groupAnagrams(lst))

if __name__ == '__main__':
    unittest.main()