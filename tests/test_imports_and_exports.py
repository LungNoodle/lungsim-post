import os
from unittest import TestCase
import unittest
import numpy as np

import lungsim-post

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'Testdata/Small.exnode')
TESTDATA_FILENAME1 = os.path.join(os.path.dirname(__file__), 'Testdata/Small.exelem')


class Test_import_exnode_exelem(TestCase):
    def test_num_nodes(self):
        nodedata = lungsim-post.import_exnode_tree(TESTDATA_FILENAME)
        self.assertTrue(nodedata['total_nodes'] is 4)

    def test_node_array_setup(self):
        nodedata = lungsim-post.import_exnode_tree(TESTDATA_FILENAME)
        node_array = nodedata['nodes']
        self.assertTrue(np.isclose(node_array[2][2], -0.5000000000000000E+00)) 
