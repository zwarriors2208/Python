class calculator:
    def add(self, *args):
        return sum(args)

calc = calculator()
print(calc.add(1,2,5,5))
print(calc.add(1,2,5,6,3,8,9))
