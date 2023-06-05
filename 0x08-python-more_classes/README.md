## Tests : heavy_check_mark:

* [tests](./tests): test file folder. The Holberton School provided it.

## Tasks : page_with_curl:

* **0. Straightforward rectangle**
  * [0-rectangle.py](./0-rectangle.py): A rectangle-defining Python class that is empty.

* **1. The actual definition of a rectangle is as follows: Python class that characterizes a square shape. expands on [0-rectangle.py](./0-rectangle.py) by adding:
    * The "width" attribute of a private instance.
    * Property getter 'def width(self): to obtain width.
    * Setter of properties: width(self, value): ' to set 'width'.
    * "height" is a private instance attribute.
    * Property getter 'def height(self): to attain "height."
    * Setter of properties: height(self, value): to establish height.
    * Instantiation with "width" and "height" options: 'def __init(self, width=0, height=0): * A "TypeError" is thrown with the message "width must be an integer" or "height must be an integer" if either "width" or "height" is not an integer.
  * On the off chance that both of 'width' or 'level' is under '0', a 'ValueError' is raised with the message 'width should be >= 0' or 'level should be >= 0'.

* **2. Perimeter and Area** * [2-rectangle.py](./2-rectangle.py): Python class that characterizes a square shape. builds on [1-rectangle.py] by adding:
    * The public instance method's def area(self): that returns the rectangle's area.
    * The def perimeter(self) attribute of the public instance: that returns the rectangle's permiter (the perimeter is zero if either width or height equal 0).

* **3. Representation as a string** * [3-rectangle.py](./3-rectangle.py): a class in Python that specifies a rectangle. expands upon [2-rectangle.py] (./2-rectangle.py) by adding:
    * Special method __str__ to print the rectangle with the # character (the method returns an empty string if either width or height equals 0).

* **4. Eval works like a charm** * [4-rectangle.py](./4-rectangle.py): a class in Python that specifies a rectangle. expands upon [3-rectangle.py] (./3-rectangle.py) by adding:
    * The special method "__repr__" returns the rectangle's string representation.

* **5. Recognize case deletion**
  * [5-rectangle.py](./5-rectangle.py): a class in Python that specifies a rectangle. Expands on [4-rectangle.py](./4-rectangle.py) with:
    When a "Rectangle" is deleted, the special method "__del__" prints the message "Bye rectangle...."

* **6. How many times? (.6-rectangle.py) * [6-rectangle.py] Python class that characterizes a square shape. expands on [5-rectangle.py] (./5-rectangle.py) by adding:
    * Public class trait 'number_of_instances' that is instated to '0', increased for each new launch, and decremened for each example cancellation.

* **7. Change the representation by adding [7-rectangle.py] to the equation: a class in Python that specifies a rectangle. Expands on [6-rectangle.py](./6-rectangle.py) with:
    * The "class_symbol" public class attribute, which can be any type but is initialized to "#," serves as the symbol for the representation of strings.

* **8. Compare rectangles using the following algorithm: a class in Python that specifies a rectangle. Expands on [7-rectangle.py](./7-rectangle.py) with:
    * Method that is static: def bigger_or_equal(rect_1, rect_2): ' that profits the square shape with the surrounding region (returns 'rect_1' assuming the two regions are equivalent).
    * On the off chance that both of 'rect_1' or 'rect_2' isn't a 'Square shape' case, a 'TypeError' is raised with the message 'rect_1 should be an occurrence of Square shape' or 'rect_2 should be an occasion of Square shape'.

* **9. A rectangle is a square, as shown by the formula: Python class that characterizes a square shape. Expands on [8-rectangle.py](./8-rectangle.py) with:
    * Define square(cls, size=0) in the class method: that returns a new instance of the Rectangle with the dimensions width x height x size
