# Where are the Waldos?

This is a little exercise in the logic of "for all" and "there exists".  It is not directly related to the bit fields project, and maybe it would have been better before the midterm than after, but here we are.  For good measure I am throwing in some practice on accessing elements in matrices (lists of lists, in Python). 


## Universal quantification: All x . P(x)

We often want to know if *all* elements of a collection satisfy some condition *P*, that is, *for all x in collection, P(x)*.  If the collection is empty, this condition is true.   In pseudocode, we can write this as 

```
all_P(collection) -> bool: 
   for x in collection: 
       if not P(x):
           return False
   return True
```

The translation of this pseudocode into code will depend on the organization of the collection, among other things.  For example, sometimes we might need list indexes to access elements, while other times we can use the simpler Python iteration through collection elements. 

## Existential quantificaton: Exists x . P(x)

Often we want to know if *some* element of a collection satisfies some condition *P*, that is *there exists some element x in the collection such that P(x)*. If the collection is empty, this condition is false. A variation on this pattern returns an element *x* satisfying *P* instead of just returning True.  In pseudocode, we can write the version that returns a booolean value as

```
some_P(collection) -> bool: 
    for x in collection: 
        if P(x): 
           return True
    return False
```

## Negating quantified predicates

The negation of "All x . P(x)" is "Exists x . not P(x)". The negation of "Exists x . P(x)" is "All x . not P(x)".  Sometimes it is easier to write code for the negated version of a quantified expression and then negate the result. 

## Nesting quantified predicates

It's usually straightforward to write code for one quantified expression.  Difficulty usually comes from nesting them, but you can work it out by just working on one level of quantification at a time.  For example, the Winter 2019 midterm asked you to implement "for all 
columns in the matrix, there exists an element in the column . element is zero."  It could be solved by essentially putting the "for all" logic in the outer loop and the "there exists" logic in an inner loop.  Many of you did just that, but many others had difficulty combining the logic.  Hence these exercises. 

## All the combinations

For purposes of this exercise, you will define symbolic constants Waldo and Other: 

```python
Waldo = 'W'
Other = '.'
```

You will write functions for all the combinations of "all" and "exists", by row and by column: 

* for all, there exists
    * all_row_exists_waldo:  For all rows in the matrix, Waldo is in some column
    * all_col_exists_waldo:  For all columns in the matrix, Waldo is in some row
* for all, for all   
    * all_row_all_waldo:  For all rows in the matrix, Waldo is in every column
    * all_col_all_waldo:  For all the columns in the matrix, Waldo is in every row
* there exists, for all
    * exists_row_all_waldo:  There is some row in the matrix in which Waldo is in every column
    * exists_col_all_waldo:  There is some column in the matrix in which Waldo is in every row
* there exists, there exists
    * exists_row_exists_waldo: There is some row in the matrix in which Waldo is in some column
    * exists_col_exists_waldo: There is some column in the matrix in which Waldo is in some row
    
You may notice that some of these are redundant.  Which ones?  Why? 

You may also notice that if you have written one of the functions for a pair of quantifiers by row, 
there is a simple and systematic transformation that gives you the function for the same 
pair of quantifiers by column.

Here is a test suite: 

```python
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
```

