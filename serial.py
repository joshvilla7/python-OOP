"""Python serial number generator."""

from tracemalloc import start


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
    def __init__ (self, start=0):
         """ this function makes a sequential number generator,
    starting from start. Which is set to 0 """
         self.start = start.next = start 

    def generate(self):
        """ generates the 'next' number from the starting number """
        self.next += 1
        return self.next -1

    def reset(self):
        """ resets generator back to start value """
        self.next = self.start

    def __repr__(self):
        """ shows respresentation of what this Class is/does """
        return f"SerialGenerator(start={self.start}, next={self.next})"
    

    


