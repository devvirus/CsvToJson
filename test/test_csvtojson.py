import os
from csvtojson import make_json_tree
import unittest
from utils import utils

dirname = os.path.dirname(__file__)
csv_path= os.path.join(dirname,'data','input.csv')
json_path=os.path.join(dirname,'data','output.json')

class TestCsvtojson(unittest.TestCase):

    def test_nest_small_csv(self):
        actual_result = make_json_tree(csv_path)
        expected_result = utils.parse_json_file(json_path)
        self.assertListEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()


