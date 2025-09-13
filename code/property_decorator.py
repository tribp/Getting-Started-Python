class rectangle:
    def __init__(self, width, height):
        self._width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, new_width):
        if new_width <= 0:
            raise ValueError("Width must be positive")
        self._width = new_width
    
    @height.setter
    def height(self, new_height):
        if new_height <= 0:
            raise ValueError("Height must be positive")
        self._height = new_height
        
    @width.deleter
    def width(self):
        del self._width
    
    @height.deleter
    def height(self):
        del self._height

    
    

# Example usage
table = rectangle(5, 10)
print(table.width)   # Output: 5
print(table.height)  # Output: 10

door = rectangle(2, -1)

# Remove width attribute
del table.width