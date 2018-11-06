import sys


class CalculationError(Exception):
    # for future integratino of division...
    #e.g. 1/0 is not valid
    pass

class InvalidNumber(Exception):
    pass

class InvalidOperator(Exception):
    pass

class UnbalancedParens(Exception):
    pass


class Calculator(object):

    def __init__(self, arg):
        if(len(arg)!=2):
            sys.exit("Wrong input! Please input a single number or string.")
        self.input = arg[1]

    def result(self):
        return self.computing()

    def computing(self):
        s = self.input
        while ")" in s:
            right = s.index(")")
            try:
                left = s[:right].rindex("(") # will raise ValueError if not found
            except ValueError:
                raise UnbalancedParens(s)

            cur = self.calculateOne(s[left+1:right])

            if left == 0 and right == len(s)-1:
                return cur
            else:
                s = s[:left] + str(cur) + s[right+1:]

        if "(" in s:
            raise UnbalancedParens(s)
        return s

    #Extendable. Additional types of calculation can be added.
    def calculateOne(self, s):

        op = s.split(" ")[0]
        nums = s.split(" ")[1:]

        if op == "add":
            return self.add(nums)
        if op == "multiply":
            return self.multiply(nums)

        # additional calculation can be added here

        raise InvalidOperator("ERRROR: Unsupported operator '"+ op +"'. Please use ‘add’ or ‘multiply’ only.")

    def add(self, nums):
        return sum(int(a) for a in nums if a!='')

    def multiply(self, nums):
        res = 1
        for a in nums:
            if a!= '':
                res *= int(a)
        return res


def main():
    cal = Calculator(sys.argv)
    print(cal.result())

if __name__ == '__main__':
    main()
