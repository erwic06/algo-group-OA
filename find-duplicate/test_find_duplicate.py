import unittest
import importlib

m = importlib.import_module("option1")

class TestFindDuplicate(unittest.TestCase):
    def test_simple_dup(self):
        self.assertEqual(m.findDuplicate([1, 3, 4, 2, 2]), 2)
        self.assertEqual(m.findDuplicateAlternative([1, 3, 4, 2, 2]), 2)

    def test_dup_at_end(self):
        self.assertEqual(m.findDuplicate([1, 2, 3, 4, 4]), 4)
        self.assertEqual(m.findDuplicateAlternative([1, 2, 3, 4, 4]), 4)

    def test_many_dups(self):
        self.assertEqual(m.findDuplicate([1, 2, 3, 3, 3, 4, 5]), 3)
        self.assertEqual(m.findDuplicateAlternative([1, 2, 3, 3, 3, 4, 5]), 3)

    def test_no_dupe(self):
        # Spec guarantees a dup, but this keeps behavior explicit.
        self.assertIsNone(m.findDuplicate([1, 2, 3, 4]))
        self.assertIsNone(m.findDuplicateAlternative([1, 2, 3, 4]))

if __name__ == "__main__":
    unittest.main()