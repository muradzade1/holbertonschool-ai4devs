# Bug Descriptions

## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.
**Issue Type**: Syntax error.
**Notes**: Missing colon at the end of function definition.

## Bug 2 – bug2.py
**Intended Behavior**: Check if a number is prime.
**Issue Type**: Logical error.
**Notes**: Returns True when divisor found (should return False).

## Bug 3 – bug3.js
**Intended Behavior**: Print greeting in uppercase.
**Issue Type**: Runtime exception.
**Notes**: Cannot read property 'name' of null.

## Bug 4 – bug4.js
**Intended Behavior**: Sum all numbers in array.
**Issue Type**: Off-by-one error.
**Notes**: Loop goes out of bounds with <=.

## Bug 5 – bug5.java
**Intended Behavior**: Convert string to int and add 10.
**Issue Type**: Misuse of data type.
**Notes**: String + int causes concatenation.

## Bug 6 – bug6.py
**Intended Behavior**: Count down from n to 1.
**Issue Type**: Recursion error.
**Notes**: Infinite recursion (n never decreases).
