# Random
The library `random` is used for generating a bunch of random occurances. You can do a lot with this (and you will need it a lot on your coding journey). So lets get started.

## How to use

### Import It
The `random` library should be preinstalled on python, but if you somehow don't have it you can get it with the following command:
```bash
pip install random
```
And for Unix-based systems:
```bash
pip3 install random
```
Next, at the top of your Python project, you can simply add:
```python
import random
```
Now you can use the library!

### Functions
The `random` library comes with many functions we will discuss the 3 most popular below below:
1. `randint` is by far the most common function from the library, as it simply chooses a random number in a range. [Full Info](#randint)
2. `choice` is also an often used function, as it chooses a random item from a list. [Full Info](#choice)
3. Another useful function is `shuffle`, which just shuffles the contents of a list. [Full Info](#shuffle)

> For more advanced projects that might need all of the functions, visit [Python Random (W3 Schools)](https://www.w3schools.com/python/module_random.asp).

## Functions (Explained better.)

### Randint

> Did you know `randint` is short for `random` and `integer`?

`randint` is by far the most common function from the library, as it simply chooses a random number in a range. Here is an example use for it:
```python
import random
print(f"Number generated: {random.randint(1, 10)}")
```
And an example of the output could be:
```
Number generated: 7
```
Or:
```
Number generated: 4
```
Or basically any other number in the range 1-10.

> If you are interested, the first number is called `start`, and the second one `stop`.

### Choice
`choice` is also an often used function, as it chooses a random item from a list. Here is an example use for it:
```python
import random
print(f"Random fruit: {random.choice(["apple", "banana", "cherry"])}")
```
And an example of the output could be:
```
Random fruit: banana
```
Of course, it can also be `apple` or `cherry`.

> The only parameter for the `choice` function is called `sequence`.

### Shuffle
Another useful function is `shuffle`, which just shuffles the contents of a list. Here is an example use for it:
```python
import random
print(f"Random order: {random.shuffle(["apple", "banana", "cherry"])}")
```
And an example of the output could be:
```
Random order: ["banana", "cherry", "apple"]
```
Of course, it can also be in any other order of the three items.

> Just like in `choice`, the only parameter here is called `sequence`.