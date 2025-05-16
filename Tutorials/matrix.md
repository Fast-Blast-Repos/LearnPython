# Matrix
A matrix is an array of data (usually numbers), that can be in different dimentions.

> See [Matrix (Wikipedia)](https://en.wikipedia.org/wiki/Matrix_(mathematics)) for more information about matrices.

The easiest way to use matices in Python is nestled list, for example, a 1D matrix would literally just be a list. But then a 2D matrix would be a list of lists, and a 3D matrix would be a list of lists of lists. This is how it would look:
```python
oneD = ["A", "B", "C"] # 1D matrix, just a list
twoD = [["1A", "1B", "1C"], ["2A", "2B", "2C"], ["3A", "3B", "3C"]] # 2D matrix, 3x3
threeD = [[["1A1", "1B1", "1C1"], ["2A1", "2B1", "2C1"], ["3A1", "3B1", "3C1"]], [["1A2", "1B2", "1C2"], ["2A2", "2B2", "2C2"], ["3A2", "3B2", "3C2"]], [["1A3", "1B3", "1C3"], ["2A3", "2B3", "2C3"], ["3A3", "3B3", "3C3"]]] # 3D matrix, 3x3x3
```
As you can see, matrices can get big easy and hard to read. So, we can use the `numpy` library to make it easier to work with matrices. The `numpy` library is a powerful library for numerical computing in Python. It provides support for arrays, matrices, and many mathematical functions. [NumPy Tutorial](Libraries/numpy.md)

We will continue with lists here. Lets start with a few uses for matrices:
- You could use a 1D matrix to store a list of items, like a shopping list or a list of names.
- You could use a 2D matrix to store a table of data, like a spreadsheet or a database.
- A 2D or 3D matrix can be used to store maps for games, like a 2D map of a game world or a 3D map of a game level.
- And a lot more!

It is also handy to know how to get data from matices. Here is how its done:
```python
# same matrices as above
print(oneD[0]) # prints "A"
print(twoD[0][0]) # prints "1A"
print(threeD[0][0][0]) # prints "1A1"
print(oneD[3]) # prints "C"
print(twoD[3][3]) # prints "3C"
print(threeD[3][3][3]) # prints "3C3"
```
And that should work for any matrix, even if you go 4D, 5D or even further! Below you can find the matrices 1-3D in more detail.

**1D Matrix**

A 1D matrix is just a list. You can use it to store a list of items, like a shopping list or a list of names. You can also use it to store a list of numbers, like a list of grades or a list of prices.
```python
oneD = ["A", "B", "C"]
```
The data from 1D matrices can be fetched using this simple code:
```python
print(oneD[0]) # prints "A"
# or
print(oneD[3]) # prints "C"
```

**2D Matrix**

A 2D matrix is a list of lists. You can use it to store a table of data, like a spreadsheet or a database. You can also use it to store a map, like a 2D map of a game world.
```python
twoD = [["1A", "1B", "1C"], ["2A", "2B", "2C"], ["3A", "3B", "3C"]]
```
The data from 2D matrices can be fetched using this simple code:
```python
print(twoD[0][0]) # prints "1A"
# or
print(twoD[3][3]) # prints "3C"
```

**3D Matrix**

A 3D matrix is a list of lists of lists. You can use it to store a 3D map, like a 3D map of a game level. You can also use it to store a list of 2D matrices, like a list of images.
```python
threeD = [[["1A1", "1B1", "1C1"], ["2A1", "2B1", "2C1"], ["3A1", "3B1", "3C1"]], [["1A2", "1B2", "1C2"], ["2A2", "2B2", "2C2"], ["3A2", "3B2", "3C2"]], [["1A3", "1B3", "1C3"], ["2A3", "2B3", "2C3"], ["3A3", "3B3", "3C3"]]]
```
The data from 3D matrices can be fetched using this simple code:
```python
print(threeD[0][0][0]) # prints "1A1"
# or
print(threeD[3][3][3]) # prints "3C3"
```

## Conclusion
In this tutorial, we learned about matrices and how to use them in Python. We learned about 1D, 2D, and 3D matrices, and how to fetch data from them. We also learned about the `numpy` library and how it can help us work with matrices. If you want to learn more about `numpy`, check out the [NumPy Tutorial](Libraries/numpy.md).