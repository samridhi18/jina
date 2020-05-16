import unittest
import numpy as np

from jina.executors.crafters.numeric.convert import ArrayConverter
from tests import JinaTestCase


class MyTestCase(JinaTestCase):
    def test_array_converter(self):
        size = 8
        sample_array = np.random.rand(size).astype("float32")
        raw_bytes = ",".join([str(x) for x in sample_array]).encode("utf8")

        converter = ArrayConverter()
        crafted_chunk = converter.craft(raw_bytes, 0)[0]

        np.testing.assert_array_equal(crafted_chunk["blob"], sample_array)

if __name__ == '__main__':
    unittest.main()
