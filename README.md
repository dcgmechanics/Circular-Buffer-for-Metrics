# Circular Buffer for Metrics

A Python implementation of a circular buffer (ring buffer) data structure designed for storing and managing metric data efficiently.

## Overview

The Circular Buffer is a fixed-size buffer that operates in a First-In, First-Out (FIFO) manner. When the buffer reaches its capacity, new elements overwrite the oldest ones, making it ideal for:

- Tracking the most recent N metrics
- Time series data with limited history requirements
- Implementing sliding window algorithms
- Memory-efficient data collection in embedded systems

## Features

- Fixed-size buffer with O(1) operations
- Automatic overwriting of oldest data when capacity is reached
- Methods to check if buffer is empty or full
- Ability to retrieve all elements in order from oldest to newest
- Function to get the most recently added element
- Buffer clearing functionality

## Installation

### Method 1: Install with pip

```bash
pip install -e .
```

### Method 2: Manual Installation

```bash
# Clone the repository
git clone https://github.com/dcgmechanics/circular-buffer-for-metrics.git
cd circular-buffer-for-metrics

# Run the install script
python setup.py install
```

## Usage

```python
from circular_buffer import CircularBuffer

# Create a buffer with capacity 5
buffer = CircularBuffer(5)

# Add some metrics
buffer.append(10)
buffer.append(20)
buffer.append(30)

# Get all elements in the buffer
print(buffer.get_all())  # Output: [10, 20, 30]

# Check if buffer is full
print(buffer.is_full())  # Output: False

# Add more elements until full
buffer.append(40)
buffer.append(50)
print(buffer.get_all())  # Output: [10, 20, 30, 40, 50]
print(buffer.is_full())  # Output: True

# Adding more elements overwrites the oldest ones
buffer.append(60)
print(buffer.get_all())  # Output: [20, 30, 40, 50, 60]

# Get the most recent metric
print(buffer.get_latest())  # Output: 60

# Clear the buffer
buffer.clear()
print(buffer.get_all())  # Output: []
print(buffer.is_empty())  # Output: True
```

## API Reference

### `CircularBuffer(capacity)`

Creates a new circular buffer with the specified capacity.

#### Parameters:
- `capacity` (int): The maximum number of metrics to store.

#### Methods:

- `append(metric_data)`: Add a new metric to the buffer.
- `get_all()`: Get all metrics in the buffer from oldest to newest.
- `get_latest()`: Get the most recently added metric.
- `is_empty()`: Check if the buffer is empty.
- `is_full()`: Check if the buffer is full.
- `clear()`: Remove all metrics from the buffer.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 