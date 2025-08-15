#!/usr/bin/env python3
import unittest
from hello import hello_world, add_numbers

class TestHello(unittest.TestCase):
    
    def test_hello_world(self):
        """Test the hello_world function."""
        result = hello_world()
        self.assertEqual(result, "Hello, World from Jenkins K8s CI/CD!")
        self.assertIsInstance(result, str)
    
    def test_add_numbers(self):
        """Test the add_numbers function."""
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)
    
    def test_add_numbers_floats(self):
        """Test add_numbers with float values."""
        self.assertAlmostEqual(add_numbers(1.5, 2.5), 4.0)

if __name__ == "__main__":
    unittest.main()
