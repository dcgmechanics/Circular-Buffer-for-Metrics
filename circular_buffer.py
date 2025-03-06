class CircularBuffer:
    def __init__(self, capacity):
        """
        Initializes a circular buffer with a given capacity.

        Args:
            capacity (int): The maximum number of metrics to store.
        """
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        self.capacity = capacity
        self.buffer = [None] * capacity  # Initialize buffer with None values
        self.head = 0  # Index where the next element will be written
        self.size = 0  # Current number of elements in the buffer

    def is_empty(self):
        """
        Checks if the buffer is empty.

        Returns:
            bool: True if empty, False otherwise.
        """
        return self.size == 0

    def is_full(self):
        """
        Checks if the buffer is full.

        Returns:
            bool: True if full, False otherwise.
        """
        return self.size == self.capacity

    def append(self, metric_data):
        """
        Appends a new metric data point to the circular buffer.
        If the buffer is full, it overwrites the oldest element.

        Args:
            metric_data: The metric data to add.
        """
        self.buffer[self.head] = metric_data  # Write data at head index
        self.head = (self.head + 1) % self.capacity  # Move head to the next position (circularly)

        if self.size < self.capacity:
            self.size += 1  # Increment size until capacity is reached

    def get_all(self):
        """
        Returns a list of all elements currently in the buffer, in the order they were added
        (oldest to newest, or as close to that order as possible in a circular buffer).

        Returns:
            list: A list of metric data points in the buffer.
        """
        if self.is_empty():
            return []

        items = []
        start_index = self.head - self.size  # Calculate starting index for reading in insertion order
        if start_index < 0:
            start_index += self.capacity # Wrap around if negative

        for i in range(self.size):
            index = (start_index + i) % self.capacity # Circular index calculation
            items.append(self.buffer[index])
        return items

    def clear(self):
        """
        Clears the buffer, resetting it to empty.
        """
        self.buffer = [None] * self.capacity
        self.head = 0
        self.size = 0

    def get_latest(self):
        """
        Returns the most recently added metric data (if buffer is not empty).

        Returns:
            The latest metric data, or None if the buffer is empty.
        """
        if self.is_empty():
            return None
        latest_index = (self.head - 1) % self.capacity # Index of the last added element
        return self.buffer[latest_index]


# Example Usage:
if __name__ == "__main__":
    buffer = CircularBuffer(5)  # Create a buffer with capacity 5

    buffer.append(10)
    buffer.append(20)
    buffer.append(30)
    print("Buffer after initial appends:", buffer.get_all()) # Output: [10, 20, 30]
    print("Is full:", buffer.is_full()) # Output: False

    buffer.append(40)
    buffer.append(50)
    print("Buffer when full:", buffer.get_all()) # Output: [10, 20, 30, 40, 50]
    print("Is full:", buffer.is_full()) # Output: True

    buffer.append(60) # Overwrite oldest element (10)
    print("Buffer after overwrite:", buffer.get_all()) # Output: [20, 30, 40, 50, 60] (10 is gone, 60 is added)
    print("Latest metric:", buffer.get_latest()) # Output: 60

    buffer.clear()
    print("Buffer after clear:", buffer.get_all()) # Output: []
    print("Is empty:", buffer.is_empty()) # Output: True