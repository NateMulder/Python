# While Loops
While loops are different from For loops.  While a For loop will continue to iterate over a block of code until the seqence ends, a while loop will only iterate over a sequence as long as a condition is met.


```python
number = 1

while number < 5:
    print(number)
    number = number + 1
```

    1
    2
    3
    4
    

In the above loop, the loop ended once the number was no longer < 5


```python
number = -5

while number < 5:
    print(number)
    if number == 3:
        break
    number = number + 1
```

    -5
    -4
    -3
    -2
    -1
    0
    1
    2
    3
    

break statements can be used to stop the loop from continuing at a specific point

number = -5

while number < 5:
    print(number)
    if number == 3:
        continue
    number = number + 1

The above code would create an infinite loop becase the "continue" command would tell the code to stay at the number three and keep printing it forever


```python
number = 0

while number < 5:
    number = number + 1
    if number == 3:
        continue
    print(number)
else:
    print('No longer <5')
```

    1
    2
    4
    5
    No longer <5
    
