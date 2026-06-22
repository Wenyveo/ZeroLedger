# test_zeroledger.py
"""
Tests for ZeroLedger module.
"""

import unittest
from zeroledger import ZeroLedger

class TestZeroLedger(unittest.TestCase):
    """Test cases for ZeroLedger class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZeroLedger()
        self.assertIsInstance(instance, ZeroLedger)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZeroLedger()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
