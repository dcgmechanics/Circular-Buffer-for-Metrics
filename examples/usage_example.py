#!/usr/bin/env python3
"""
Example usage of the CircularBuffer for metrics.
"""

from circular_buffer_metrics import CircularBuffer

def main():
    # Create a buffer with capacity 5
    buffer = CircularBuffer(5)
    
    print("Adding metrics to buffer...")
    buffer.append(10)
    buffer.append(20)
    buffer.append(30)
    print(f"Buffer after initial appends: {buffer.get_all()}")
    print(f"Is buffer full? {buffer.is_full()}")
    
    print("\nFilling the buffer...")
    buffer.append(40)
    buffer.append(50)
    print(f"Buffer when full: {buffer.get_all()}")
    print(f"Is buffer full? {buffer.is_full()}")
    
    print("\nOverwriting oldest element...")
    buffer.append(60)  # This will overwrite 10
    print(f"Buffer after overwrite: {buffer.get_all()}")
    print(f"Latest metric: {buffer.get_latest()}")
    
    print("\nClearing the buffer...")
    buffer.clear()
    print(f"Buffer after clear: {buffer.get_all()}")
    print(f"Is buffer empty? {buffer.is_empty()}")
    
    # Example with different data types
    print("\nExample with string metrics:")
    str_buffer = CircularBuffer(3)
    str_buffer.append("CPU: 45%")
    str_buffer.append("Memory: 60%")
    str_buffer.append("Disk: 30%")
    print(f"String metrics: {str_buffer.get_all()}")
    
    # Example with dictionary metrics
    print("\nExample with dictionary metrics:")
    dict_buffer = CircularBuffer(2)
    dict_buffer.append({"cpu": 45, "timestamp": "2023-01-01T12:00:00"})
    dict_buffer.append({"cpu": 60, "timestamp": "2023-01-01T12:01:00"})
    print(f"Dictionary metrics: {dict_buffer.get_all()}")

if __name__ == "__main__":
    main() 
