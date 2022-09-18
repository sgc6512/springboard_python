"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=10):
        self.start = start
        self.current_seq = start

    def generate(self):
        """Returns the next number in the sequence"""
        result = self.current_seq
        self.current_seq += 1
        return result

    def reset(self):
        """Resets the sequence back to the starting value"""
        self.current_seq = self.start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.current_seq + 1}>"
