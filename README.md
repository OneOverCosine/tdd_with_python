# Test Driven Development with Python

## What is TDD?
TDD stands for test driven development. As the name suggests, with TDD the code that is developed is dependant on the tests written for it. Traditionally, you'd write code before writing the tests for it, but with TDD it's the other way around. Since you know what you want the code to do *before* you write it, you can start off with writing the tests and then write the code to try and pass those tests.  

(following notes)
**Best Use Case**
- You can use Pytest unittest in Python to implement TDD
- TDD is widely used and is it the cheapest way to test code

## How it's Used
There are five steps to TDD. 
- Understand the functionality/ programming requirements. You can't write code (or tests) if you don't know what it is you are trying to achive.
- Translate the functionality/requirement into a test. Run the test before writing any code to see if it fails. If this is the first cycle, you want the test to fail as you haven't yet built the functionality. If it's not the first cycle, a pass might mean you have already written the code you need.
- Write the code that fulfills the requirement. Run all the tests and they should pass.



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

### Pytest and Unittest
Running with ``python -m unittest descover -v``
```
test_add (test_unittest_simplecalc.CalcTest) ... ok
test_divide (test_unittest_simplecalc.CalcTest) ... ok
test_multiply (test_unittest_simplecalc.CalcTest) ... ok
test_subtract (test_unittest_simplecalc.CalcTest) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

Running with ``python -m pytest -v``
```
==================================== test session starts =====================================
(truncated info)

test_unittest_simplecalc.py::CalcTest::test_add PASSED                                  [ 25%] 
test_unittest_simplecalc.py::CalcTest::test_divide PASSED                               [ 50%] 
test_unittest_simplecalc.py::CalcTest::test_multiply PASSED                             [ 75%] 
test_unittest_simplecalc.py::CalcTest::test_subtract PASSED                             [100%] 

(truncated info)

================================ 4 passed, 1 warning in 0.06s ================================
```