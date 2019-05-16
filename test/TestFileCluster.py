import unittest

from FileCluster import FileCluster


class FileClusterTest(unittest.TestCase):

    def setUp(self):
        self.names = ['./testcases/case1.json']
        self.fileCluster = FileCluster(self.names)

    def test_find_field_by_id(self):
        array = [{'id': 1, 'times': 1, 'step': 1},
                 {'id': 2, 'times': 1, 'step': 1},
                 {'id': 3, 'times': 1, 'step': 1}
                 ]
        self.assertTrue(self.fileCluster.find_field_by_id(1, array) != None,
                        'ID not found mate! Recheck implementation')
        self.assertTrue(self.fileCluster.find_field_by_id(100, array) == None,
                        'Found something odd! Recheck implementation')

    def test_read_file(self):
        content_file = self.fileCluster.read_file('../testcases/case1.json')
        self.assertIsNotNone(content_file)

    def test_convert_order_to_map(self):
        array = {"orderOfFields": [
            {'id': 1, 'step': 1},
            {'id': 2, 'step': 1},
            {'id': 2, 'step': 2},
            {'id': 3, 'step': 1}]
        }

        expected_result = [{'id': 1, 'times': 1, 'step': 1},
                           {'id': 2, 'times': 2, 'step': 1},
                           {'id': 3, 'times': 1, 'step': 1}
                           ]

        self.assertTrue(self.fileCluster.convert_order_to_map(array) == expected_result,
                        'Result does not match with expected.')

    def test_merge(self):
        original_items_array = [{'id': 1, 'times': 2, 'step': 1},
                                {'id': 2, 'times': 1, 'step': 2},
                                {'id': 3, 'times': 2, 'step': 3}]

        new_items_array = [{'id': 3, 'times': 1, 'step': 4},
                           {'id': 6, 'times': 2, 'step': 6},
                           {'id': 7, 'times': 1, 'step': 5}]

        expected_array = [{'id': 1, 'times': 2, 'step': 1},
                          {'id': 2, 'times': 1, 'step': 2},
                          {'id': 3, 'times': 3, 'step': 3},
                          {'id': 6, 'times': 2, 'step': 6},
                          {'id': 7, 'times': 1, 'step': 5}]

        self.assertTrue(self.fileCluster.merge(original_items_array, new_items_array) == expected_array,
                        'Your expectation does not match with your reality')

    def test_cluster_files(self):
        results = self.fileCluster.cluster_files()
        expectations = [{'id': 1, 'times': 1, 'step': 1},
                        {'id': 3, 'times': 1, 'step': 2},
                        {'id': 2, 'times': 1, 'step': 3},
                        {'id': 4, 'times': 1, 'step': 4},
                        {'id': 5, 'times': 1, 'step': 5}]

        self.assertTrue(results == expectations,
                        'Your expectation does not match with your reality on the final stage')


if __name__ == "__main__":
    unittest.main()
