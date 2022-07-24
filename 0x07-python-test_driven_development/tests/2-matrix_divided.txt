====================================================================
                                                                   =
Generating Test Cases for ``2-matrix_divided`` module.             =
                                                                   =
====================================================================

====================================================================
                                                                   =
File: 2-matrix_divided.txt                                         =
Desc: This file contains most possible edge cases for the function =
      ``matrix_divided`` in the ``2-matrix_divided`` module        =
Author: Gizachew Bayness (Elec Crazy)                              =
Date Created: Jul 24 2022                                          =
                                                                   =
====================================================================

Result: All elements of the ``matrix`` should be divided by ``div``,
rounded to 2 decimal places.

>>> matrix_divided = __import__('2-matrix_divided').matrix_divided

Let's test the function by giving the expected inputs. Note that, the
function returns the new matrix with the operation original_matrix
divided by the parameter ``div``, which is the divisor.

>>> matrix = [
...	[9, 3, 12, 15],
...	[12, 9, 24, 18],
...	[54, 75, 84, 99]
...	]
>>> matrix_divided(matrix, 3)
[[3.0, 1.0, 4.0, 5.0], [4.0, 3.0, 8.0, 6.0], [18.0, 25.0, 28.0, 33.0]]

>>> matrix = [
...     [3, 6, 9],
...     [12, 15, 18]
... 	]
>>> matrix_divided(matrix, 3)
[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]

The function performs the required operation without changing the content
of the original matrix. Therefore, let's verify that.

>>> matrix
[[3, 6, 9], [12, 15, 18]]

>>> matrix = [
...	[-1, -2, -3],
...	[-4, -5, -6]
...	]
>>> matrix_divided(matrix, -3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

>>> matrix = [
...     [-1, -2, 3],
...     [4, -5, 6]
...     ]

>>> matrix_divided(matrix, 3)
[[-0.33, -0.67, 1.0], [1.33, -1.67, 2.0]]

>>> matrix = [
...     [-1, -2, 3],
...     [4, -5, 6]
...     ]

>>> matrix_divided(matrix, -1)
[[1.0, 2.0, -3.0], [-4.0, 5.0, -6.0]]

>>> matrix = [
...	[7.2, -8],
...	[-2.1, 0]
...	]

>> matrix_divided(matrix, 2.7)
[[2.67, -2.96], [-0.78, 0]]

>>> matrix = [
...     [7.2, -8],
...     [-2.1, 0]
...     ]

>> matrix_divided(matrix, -2.7)
[[-2.67, 2.96], [0.78, 0]]


Let's test the function with empty matrix or empty list of lists and not
empty list. This operation will return empty list of lists itself.

>>> matrix_divided([[]], 5)
[[]]

Let's test the function with empty list and not empty list of list.

>>> matrix_divided([], 3)
Traceback (most recent call last):
...
TypeError: matrix must be a matrix (list of lists) of integers/floats

Let's test the function by passing invalid arguments as ``matrix``

>>> matrix_divided("Hello World", 7)
Traceback (most recent call last):
...
TypeError: matrix must be a matrix (list of lists) of integers/floats

>>> matrix_divided(None, 3)
Traceback (most recent call last):
...
TypeError: matrix must be a matrix (list of lists) of integers/floats

>>> matrix_divided([(1, 2, 3), (4, 5, 6)], 2)
Traceback (most recent call last):
...
TypeError: matrix must be a matrix (list of lists) of integers/floats

Let's test the function with a list of lists having the elements that
are not actually floats or ints.

>>> matrix = [
...	[1, "H", None],
...	[-2, 3.3, 5],
...	["Elec", "Crazy", (2+5j)]
...	]
>>> matrix_divided(matrix, -3)
Traceback (most recent call last):
...
TypeError: matrix must be a matrix (list of lists) of integers/floats

>>> matrix = [
...	[987, 8],
...	[-7.9, 'love']
...	]
>>> matrix_divided(matrix, 1.1)
Traceback (most recent call last):
...
TypeError: matrix must be a matrix (list of lists) of integers/floats

Let's test the function with a different size of rows of a matrix.
Notice that, this operation will result in a type error.

>>> matrix = [
...	[1, 2, 3],
...	[4, 5, 6],
...	[7, 8]
...	]
>>> matrix_divided(matrix, 2)
Traceback (most recent call last):
...
TypeError: Each row of the matrix must have the same size

>>> matrix = [
...	[3, 33],
...	[4, 5, -8.7]
...	]
>>> matrix_divided(matrix, 1.5)
Traceback (most recent call last):
...
TypeError: Each row of the matrix must have the same size

Let's test the function with an invalid divisor (Neither a type of integer
nor a type of floating point).

>>> matrix = [
...     [-1, -2, 3],
...     [4, -5, 6]
...     ]

>>> matrix_divided(matrix, None)
Traceback (most recent call last):
...
TypeError: div must be a number

>>> matrix_divided(matrix, "Elec Crazy")
Traceback (most recent call last):
...
TypeError: div must be a number

>>> matrix_divided(matrix, (2+5j))
Traceback (most recent call last):
...
TypeError: div must be a number

>>> matrix_divided(matrix, -1)
[[1.0, 2.0, -3.0], [-4.0, 5.0, -6.0]]

Let's test the function with an invalid divisor with ``div`` = 0

>>> matrix_divided(matrix, 0)
Traceback (most recent call last):
...
ZeroDivisionError: division by zero

>>> matrix_divided(matrix, -1)
[[1.0, 2.0, -3.0], [-4.0, 5.0, -6.0]]
