# Test Driven Development with Python

## What is TDD?
TDD stands for test driven development. As the name suggests, with TDD the code that is developed is dependant on the tests written for it. Traditionally, you'd write code before writing the tests for it, but with TDD it's the other way around. Since you know what you want the code to do *before* you write it, you can start off with writing the tests and then write the code to try and pass those tests.  

(following notes)
**Best Use Case**
- You can use Pytest unittest in Python to implement TDD
- TDD is widely used and is it the cheapest way to test code

## How it's Used
- Write 

## Unit Tests

|Method |   Checks that|   New in |
|:---|:---|:---|
|assertEqual(a, b)        |     a == b              ||
|assertNotEqual(a, b)     |     a != b              ||  
|assertTrue(x)            |    bool(x) is True     ||  
|assertFalse(x)           |    bool(x) is False    ||  
|assertIs(a, b)           |    a is b              |3.1|
|assertIsNot(a, b)        |    a is not b          |3.1|
|assertIsNone(x)          |    x is None           |3.1|
|assertIsNotNone(x)       |    x is not None       |3.1|
|assertIn(a, b)           |    a in b              |3.1|
|assertNotIn(a, b)        |    a not in b          |3.1|
|assertIsInstance(a, b)   |    isinstance(a, b)    |3.2|
|assertNotIsInstance(a, b)|    not isinstance(a, b)|3.2|