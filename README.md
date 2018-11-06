# README for Python Calculator

## Featurs supported

1. Calculation of different numbers of variables, such as

   - (add 1)
   - (add 1 2 3 4 5 ...)  from one number to whatever you need to calculate

2. Space ignorance between numbers, such as

   - (add 1       5)		would just return the correct result without error

3. Error checking for

   - Unbanlanced Parentheses

   - Invalid Operator (currently support add and multiply only, but it can be extended for other types of calculations)

   - Left space for calculation error for future, for situations such as a number divided by 0


## Architect

Following the concepts of **Object-Oriented Programming** and **RAII** (Resource Acquisition Is Initialization).

As there is no complex functions needed. I created one Calculator class as the object.

Details as below:

- Calculator
  - self.input
  - result(self)      to return calculation result
  - computing(self)     the calculation part. It would divide the whole formula into small sections, and compute them accordingly
  - calculateOne(self, s)    the helper function for calculation that does one calculation at a time, additinoal calculation can be added here
  - add(self, nums)    handling extra space between numbers
  - multiply(self, nums)    handling extra space between numbers



## Extra Test Cases

python3 calculator.py "(add 1 (multiply (add 2 1) 6  (multiply 4 5    2)))"

python3 calculator.py "(add (multiply (add 2 1) 6  (multiply 4 5    2)))"

python3 calculator.py "(add  (multiply (add 2 1) 6  (multiply 4 5    2))"

python3 calculator.py "add (multiply (add 2 1) 6  (multiply 4 5    2)))"

python3 calculator.py "(add (multiply (add 2 1) 6  (Aultiply 4 5    2)))"



### Thanks for your review! Please contact me at audrey.ziwei.hu@gmail.com if you have any question.

