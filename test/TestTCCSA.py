import unittest

from TCCSA import get_place_to_swap, swap, value


class FieldTest(unittest.TestCase):

    def test_placeToSwap(self):
        array = [0, 1, 2, 3, 4]
        self.assertTrue(get_place_to_swap(array, 5, True) == 0, 'Review the entry. Should be 0 for Right')
        self.assertTrue(get_place_to_swap(array, 0, False) == 4, 'Review the entry. Should be 5 for Left')
        self.assertTrue(get_place_to_swap(array, 4, True) == 4, 'Review the entry. Should be 5 for Right')

    def test_swapItself(self):
        array = [0, 1, 2, 3, 4]
        self.assertTrue(swap(array, 5, True) == [4, 1, 2, 3, 0], 'Review the entry. Should be [4,1,2,3,0] for Right')
        self.assertTrue(swap(array, 3, True) == [0, 1, 2, 4, 3],
                        'Review the entry. Should be [0, 1, 2, 4, 3] for Right')
        self.assertTrue(swap(array, 0, False) == [4, 1, 2, 3, 0], 'Review the entry. Should be [4,1,2,3,0] for Left')

    def test_value(self):
        # considerando 10 usuários
        field1 = {"times": 8, "step": 4}
        field2 = {"times": 7, "step": 3}
        field3 = {"times": 8, "step": 1}
        field4 = {"times": 2, "step": 2}
        field5 = {"times": 1, "step": 5}

        self.assertEqual(value([field1, field2, field3, field4, field5]), 6, 'Not equal')
        self.assertEqual(value([field5, field4, field3, field1, field2]), 12, 'Not equal')

    def test_case1(self):
        fields = [{'id': 4, 'times': 3, 'step': 4},
                  {'id': 11, 'times': 3, 'step': 8},
                  {'id': 1, 'times': 6, 'step': 3},
                  {'id': 2, 'times': 6, 'step': 5},
                  {'id': 5, 'times': 3, 'step': 5},
                  {'id': 3, 'times': 3, 'step': 2}]

        self.assertEqual(value(fields), 6)


if __name__ == "__main__":
    unittest.main()
