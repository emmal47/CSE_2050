from math import sqrt, cos, sin, atan

class Vector:
    """Class for methods that have been factored out from Rectangluar and Polar Vectors"""
    def __init__(self, *args):
        """Users should specify rectangular or polar instead"""
        raise NotImplementedError("Specify RectangularVector or PolarVector.")
    
    # Define "getters" for x, y, mag, and angle
    def get_x(self):
        """Returns x-component of vector."""
        return self._x

class RectangularVector(Vector):
    """Rectangular vectors have an x and y component."""
    def __init__(self, x, y):
        """Creates a new vector with given x- and y- attributes."""
        self._x = x
        self._y = y
        self._update() # add self._mag and self._ang