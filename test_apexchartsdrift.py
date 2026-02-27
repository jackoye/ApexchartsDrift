# test_apexchartsdrift.py
"""
Tests for ApexchartsDrift module.
"""

import unittest
from apexchartsdrift import ApexchartsDrift

class TestApexchartsDrift(unittest.TestCase):
    """Test cases for ApexchartsDrift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ApexchartsDrift()
        self.assertIsInstance(instance, ApexchartsDrift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ApexchartsDrift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
