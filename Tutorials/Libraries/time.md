# Time
The `time` library has many time-based uses,  like keeping track of program runtime, waiting a few seconds, and more! This is also a library that will come very usefull in your programming journey.

## How To Use

### Import It
The `time` library should be preinstalled on python, but if you somehow don't have it you can get it with the following command:
```bash
pip install time
```
And for Unix-based systems:
```bash
pip3 install time
```
Next, at the top of your Python project, you can simply add:
```python
import time
```
Now you can use the library!

### Functions
The `time` library comes with many functions we will discuss the 3 most popular below below:
1. `time` gets the time of the program. [Full Info](#get-time)
2. The `sleep` function is probably the most used function from the `time` library. This functions waits the time inputted in the parameters (seconds) before continuing with the script. [Full Info](#sleep)

> For more advanced projects that might need all of the functions, visit [Python Time (Python Docs)](https://docs.python.org/3/library/time.html).

## Functions (Explained Better)

### Get Time
`time` gets the time of the program. Here is how you could use it:
```python
import time
start = time.time()
input()
end = time.time()
print(f"Time Elapsed: {end - start}")
```
Output should be in seconds, for example:
```
Time Elapsed: 5.635627269744873
```

### Sleep
The `sleep` function is probably the most used function from the `time` library. This functions waits the time inputted in the parameters (seconds) before continuing with the script. Here is an example:
```python
import time
time.sleep(10)
print("Thanks for waiting 10 seconds.")
```
And the output is quite obvious, it will wait 10 seconds, and the print: `Thanks for waiting 10 seconds.`.