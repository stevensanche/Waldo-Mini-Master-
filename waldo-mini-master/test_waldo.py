"""Universal and existential quantifiers """

import unittest
from waldo import *


class TestAE(unittest.TestCase):
    """For all x, there exists y . P(y)"""

    # By row
    def test_exists_waldo_every_row(self):
        """For all rows in matrix, there exists a Waldo in the row"""
        self.assertTrue(all_row_exists_waldo([[Other, Other, Waldo],
                                              [Waldo, Other, Other],
                                              [Waldo, Waldo, Waldo]]))
        self.assertFalse(all_row_exists_waldo([[Other, Other, Waldo],
                                               [Other, Other, Other],
                                               [Waldo, Waldo, Waldo]]))
        # Vacuous: No rows
        self.assertTrue(all_row_exists_waldo([]))
        # Vacuous: No columns
        self.assertFalse(all_row_exists_waldo([[],[]]))

    # By column
    def test_exists_waldo_every_col(self):
        """For all columns in the matrix, there exists a Waldo in the column"""
        self.assertTrue(all_col_exists_waldo([[Other, Waldo, Other],
                                              [Waldo, Other, Other],
                                              [Other, Waldo, Waldo]]))
        self.assertFalse(all_col_exists_waldo([[Waldo, Other, Other],
                                               [Other, Waldo, Other],
                                               [Waldo, Other, Other]]))

        # Vacuous: No rows
        self.assertTrue(all_col_exists_waldo([]))
        # Vacuous: No columns
        self.assertTrue(all_col_exists_waldo([[],[]]))

class TestAA(unittest.TestCase):
    """For all x, for all y . P(y)"""

    # By row
    def test_all_row_all_waldo(self):
        self.assertTrue(all_row_all_waldo([[Waldo, Waldo, Waldo],
                                           [Waldo, Waldo, Waldo],
                                           [Waldo, Waldo, Waldo]]))
        self.assertFalse(all_row_all_waldo([[Waldo, Waldo, Waldo, Waldo],
                                           [Waldo, Waldo, Other, Waldo],
                                           [Waldo, Waldo, Waldo, Waldo]]))
        # Vacuous: No rows
        self.assertTrue(all_row_all_waldo([]))
        # Vacuous: No columns
        self.assertTrue(all_row_all_waldo([[], [], []]))


    # By col
    def test_all_col_all_waldo(self):
        self.assertTrue(all_col_all_waldo([[Waldo, Waldo, Waldo],
                                           [Waldo, Waldo, Waldo],
                                           [Waldo, Waldo, Waldo]]))
        self.assertFalse(all_col_all_waldo([[Waldo, Waldo, Waldo, Waldo],
                                           [Waldo, Waldo, Other, Waldo],
                                           [Waldo, Waldo, Waldo, Waldo]]))
        # Vacuous: No rows
        self.assertTrue(all_row_all_waldo([]))
        # Vacuous: No columns
        self.assertTrue(all_row_all_waldo([[], [], []]))

class TestEE(unittest.TestCase):
    """There exists x such that there exists y . P(y)"""

    # By row
    def test_exists_row_exists_waldo(self):
        self.assertTrue(exists_row_exists_waldo([[Other, Other, Other],
                                                 [Other, Other, Waldo],
                                                 [Other, Other, Other]]))
        self.assertFalse(exists_row_exists_waldo([[Other, Other],
                                              [Other, Other]]))
        # Vacuous: No rows
        self.assertFalse(exists_row_exists_waldo([]))
        # Vacuous: No columns
        self.assertFalse(exists_row_exists_waldo([[], []]))

    # By column
    def test_exists_col_exists_waldo(self):
        self.assertTrue(exists_col_exists_waldo([[Other, Other, Other],
                                              [Other, Other, Waldo],
                                              [Other, Other, Other]]))
        self.assertFalse(exists_col_exists_waldo([[Other, Other],
                                          [Other, Other]]))

        # Vacuous: No rows
        self.assertFalse(exists_col_exists_waldo([]))
        # Vacuous: No columns
        self.assertFalse(exists_col_exists_waldo([[], []]))



class TestEA(unittest.TestCase):
    """There exists x such that all y . P(y)"""

    # By row
    def test_exists_row_all_waldo(self):

        self.assertTrue(exists_row_all_waldo([[Other, Waldo, Other],
                                              [Waldo, Waldo, Waldo],
                                              [Other, Other, Other]]))

        self.assertFalse(exists_row_all_waldo([[Waldo, Other, Waldo],
                                               [Waldo, Other, Waldo],
                                               [Other, Waldo, Waldo]]))

        #Vacuous: No rows
        self.assertFalse(exists_row_all_waldo([]))
        #Vacuous: No columns
        self.assertTrue(exists_row_all_waldo([[], []]))

    # By column
    def tests_exists_col_all_waldo(self):
        self.assertTrue(exists_col_all_waldo([[Other, Waldo, Other],
                                              [Waldo, Waldo, Other],
                                              [Other, Waldo, Waldo]]))

        self.assertFalse(exists_col_all_waldo([[Waldo, Waldo, Waldo],
                                               [Waldo, Other, Waldo],
                                               [Other, Waldo, Other]]))

        # Vacuous: No rows
        self.assertFalse(exists_col_all_waldo([]))
        # Vacuous: No columns
        self.assertFalse(exists_col_all_waldo([[], []]))



if __name__ == "__main__":
    unittest.main()




