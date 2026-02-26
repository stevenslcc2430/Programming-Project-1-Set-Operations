import unittest

from Part1_Set_Operations import Part1_OrdinarySets
from Part1_Set_Operations import empty_test
class MyTestCase(unittest.TestCase):
    def setUp(self):
            self.test1 = Part1_OrdinarySets()
            self.test2 = Part1_OrdinarySets()
            self.test3 = Part1_OrdinarySets()
            self.empty = empty_test()
    def test_complement(self):
            #expected values
            self.complement1 = self.test1.complement_a
            self.complement2 = self.test2.complement_a
            self.complement3 = self.test3.complement_a
            #operation process
            self.complement_a = [not value for value in self.test1.bool_a]
            self.complement_a2 = [not value for value in self.test2.bool_a]
            self.complement_a3 = [not value for value in self.test3.bool_a]
            #test
            self.assertEqual(self.complement_a,self.complement1)
            self.assertEqual(self.complement_a2, self.complement2)
            self.assertEqual(self.complement_a3, self.complement3)

        #UNION TEST CASES
    def test_union(self):
            # expected
            self.union1_results = self.test1.union
            self.union2_results = self.test2.union
            self.union3_results = self.test3.union
            #operation
            self.union1 = [self.test1.bool_a[i] or self.test1.bool_b[i] for i in range(self.test1.n)]
            self.union2 = [self.test2.bool_a[i] or self.test2.bool_b[i] for i in range(self.test2.n)]
            self.union3 = [self.test3.bool_a[i] or self.test3.bool_b[i] for i in range(self.test3.n)]
            #test
            self.assertEqual(self.union1, self.union1_results)
            self.assertEqual(self.union2, self.union2_results)
            self.assertEqual(self.union3, self.union3_results)
        #INTERSECTION TEST
    def test_intersection(self):
            #expected results
            self.results1 = self.test1.intersection
            self.results2 = self.test2.intersection
            self.results3 = self.test3.intersection
            #operations
            self.intersection1 = [self.test1.bool_a[i] and self.test1.bool_b[i] for i in range(self.test1.n)]
            self.intersection2 = [self.test2.bool_a[i] and self.test2.bool_b[i] for i in range(self.test2.n)]
            self.intersection3 = [self.test3.bool_a[i] and self.test3.bool_b[i] for i in range(self.test3.n)]
            #results
            self.assertEqual(self.intersection1, self.results1)
            self.assertEqual(self.intersection2, self.results2)
            self.assertEqual(self.intersection3, self.results3)
        #DIFFERENCE TEST
    def test_difference(self):
            #expected results
            self.difference1 = self.test1.difference_a_minus_b
            self.difference2 = self.test2.difference_a_minus_b
            self.difference3 = self.test3.difference_a_minus_b
            #operations
            self.difference_a_minus_b1 = [self.test1.bool_a[i] and not self.test1.bool_b[i] for i in range(self.test1.n)]
            self.difference_a_minus_b2 = [self.test2.bool_a[i] and not self.test2.bool_b[i] for i in range(self.test2.n)]
            self.difference_a_minus_b3 = [self.test3.bool_a[i] and not self.test3.bool_b[i] for i in range(self.test3.n)]
            #test
            self.assertEqual(self.difference_a_minus_b1, self.difference1)
            self.assertEqual(self.difference_a_minus_b2, self.difference2)
            self.assertEqual(self.difference_a_minus_b3, self.difference3)
        #SYMMETRIC TEST
    def test_symmetric(self):
            # expected results
            self.symmetric1 = self.test1.symmetric_difference
            self.symmetric2 = self.test2.symmetric_difference
            self.symmetric3 = self.test3.symmetric_difference
            # operations
            self.symmetric_difference1 = [self.test1.bool_a[i] ^ self.test1.bool_b[i] for i in range(self.test1.n)]
            self.symmetric_difference2 = [self.test2.bool_a[i] ^ self.test2.bool_b[i] for i in range(self.test2.n)]
            self.symmetric_difference3 = [self.test3.bool_a[i] ^ self.test3.bool_b[i] for i in range(self.test3.n)]
            # test cases
            self.assertEqual(self.symmetric_difference1, self.symmetric1)
            self.assertEqual(self.symmetric_difference2, self.symmetric2)
            self.assertEqual(self.symmetric_difference3, self.symmetric3)
    def test_edge_cases(self):
            #complement
            self.complement = self.empty.complement_a
            self.complement_empty = [not value for value in self.empty.empty1]
            self.assertEqual(self.complement, self.complement)
            # union test
            self.union_results = self.empty.union
            self.union = [self.empty.empty1[i] or self.empty.empty2[i] for i in range(self.empty.n)]
            self.assertEqual(self.union, self.union_results)
            # intersection
            self.results = self.empty.intersection
            self.intersection = [self.empty.empty1[i] and self.empty.empty2[i] for i in range(self.empty.n)]
            self.assertEqual(self.intersection, self.results)
            # difference
            self.difference = self.empty.difference_a_minus_b
            self.difference_a_minus_b = [self.empty.empty1[i] and not self.empty.empty2[i] for i in range(self.empty.n)]
            self.assertEqual(self.difference_a_minus_b, self.difference)
            # SYMMETRIC TEST
            self.symmetric = self.empty.symmetric_difference
            self.symmetric_difference = [self.empty.empty1[i] ^ self.empty.empty2[i] for i in range(self.empty.n)]
            self.assertEqual(self.symmetric_difference, self.symmetric)