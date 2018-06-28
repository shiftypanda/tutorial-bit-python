# A regular polygon has n number of sides. Each side has length s.
#
# The area of a regular polygon is:

# The perimeter of a polygon is: length of the boundary of the polygon

# Write a function called polysum that takes 2 arguments, n and s.
# This function should sum the area
# and square of the perimeter of the regular polygon.

# The function returns the sum, rounded to 4 decimal places.
#
# Hint: What to import?
# Which library should you be importing at the beginning of your code in order to
# call the tan function and to get the pi constant?

from unittest import TestCase
import math

def polysum(n, s):
    """
    :param n: int number of sides of the polygon
    :param s: int or float length size of each side in the polygon
    :return: sum of area and sqaure of the perimter rounded to 4 decimal places
    """
    def area_poly(n, s):
        """
        :param n: int number of sides of the polygon
        :param s: int or float length size of each side in the polygon
        :return: sum of area of polygon
        """
        area_top =  0.25 * n * s**2
        area_bottom = math.tan(math.pi/n)
        area = area_top / area_bottom
        area_new = (0.25 * n * s**2) / math.tan(math.pi/n)

        return area

    def peri_poly(n, s):
        """
        :param n: int number of sides of the polygon
        :param s: int or float length size of each side in the polygon
        :return: length of boundary of polygon squared
        """
        perimeter = 0
        for sides in range(n):
            perimeter += s
        return perimeter**2


    return round((area_poly(n, s) + peri_poly(n, s)), 4)

class TestPolysum(TestCase):

    def test_polysum_53_sides_length_78(self):
        n = 53
        s = 78
        response = polysum(n, s)
        self.assertEqual(18448338.3266, response)