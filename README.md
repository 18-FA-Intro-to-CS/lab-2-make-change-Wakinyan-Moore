# Introductiong to Computer Science - Fall 2018

## Lab 2 - Making Change

**Purpose:** The purpose of this lab is to get some more experience doing computations in Python. You will design and write a simple program that computes the number of coins and their denominations that might be used in making change.

**Practice:** Study the examples in Chapter 2 of the text and on the [course website](http://itech190.erickuha.com).

**Instructions:** Create a Python script called _makeChange.py_ that serves as a way to convert any number of pennies into as few coins as possible, using quarters, dimes, and nickels. The program should start out with a brief description of what it does.

The program should next prompt the user for input. It should ask the user to enter some number of pennies.

The program should then display the following information:

* The minimum number of coins required to make change
* How many of those are quarters
* How many of those are dimes
* How many of those are nickels
* How many of those are pennies

For example, if the user entered 57 pennies, the output would look something like:

```
The total number of coins is 5. They are distributed as follows:
- 2 quarters
- 0 dimes
- 1 nickels
- 2 pennies
```

**Tips and Hints:** If you want to find the maximum number of quarters that can make a certain amount of change, the integer division operator (`//`) can help. Let's say that `pennies` has a value of 57. If you calculate `pennies / 25` in Python, you will get something like 2.28. That is not quite the right answer because you can never have 0.28 quarters. However, integer division `pennies // 25` gives exactly 2, which is the number of quarters in 57 cents. With a little tweaking, you can do something similar for all of the other coins.
