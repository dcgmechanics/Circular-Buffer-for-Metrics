import unittest
from circular_buffer_metrics import CircularBuffer

class TestCircularBuffer(unittest.TestCase):
    def test_initialization(self):
        """Test that the buffer initializes correctly."""
        buffer = CircularBuffer(5)
        self.assertEqual(buffer.capacity, 5)
        self.assertTrue(buffer.is_empty())
        self.assertFalse(buffer.is_full())
        
    def test_append_and_get_all(self):
        """Test appending items and retrieving them."""
        buffer = CircularBuffer(3)
        buffer.append(10)
        buffer.append(20)
        
        self.assertEqual(buffer.get_all(), [10, 20])
        self.assertEqual(buffer.size, 2)
        
    def test_full_buffer(self):
        """Test that the buffer correctly identifies when it's full."""
        buffer = CircularBuffer(2)
        buffer.append(10)
        buffer.append(20)
        
        self.assertTrue(buffer.is_full())
        
    def test_overwrite(self):
        """Test that the buffer correctly overwrites oldest elements when full."""
        buffer = CircularBuffer(3)
        buffer.append(10)
        buffer.append(20)
        buffer.append(30)
        buffer.append(40)  # This should overwrite 10
        
        self.assertEqual(buffer.get_all(), [20, 30, 40])
        
    def test_get_latest(self):
        """Test retrieving the latest element."""
        buffer = CircularBuffer(3)
        buffer.append(10)
        buffer.append(20)
        
        self.assertEqual(buffer.get_latest(), 20)
        
    def test_clear(self):
        """Test clearing the buffer."""
        buffer = CircularBuffer(3)
        buffer.append(10)
        buffer.append(20)
        buffer.clear()
        
        self.assertTrue(buffer.is_empty())
        self.assertEqual(buffer.get_all(), [])
        
    def test_empty_buffer_operations(self):
        """Test operations on an empty buffer."""
        buffer = CircularBuffer(3)
        
        self.assertEqual(buffer.get_all(), [])
        self.assertIsNone(buffer.get_latest())
        
    def test_invalid_capacity(self):
        """Test that initializing with invalid capacity raises ValueError."""
        with self.assertRaises(ValueError):
            CircularBuffer(0)
        with self.assertRaises(ValueError):
            CircularBuffer(-1)

if __name__ == "__main__":
    unittest.main() 
