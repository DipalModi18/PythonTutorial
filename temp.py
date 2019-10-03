import time

date = time.strptime("2019-06-24 06:32:48.0", "%Y-%m-%d %H:%M:%S.%f")
print(int(time.mktime(date))*1000)

class Temp:
    number = None

    @classmethod
    def get_number(cls):
        if cls.number is None:
            print('Number is None')
            cls.number = 5
        else:
            print('Number not none')
        return cls.number


temp1 = Temp()
temp1.get_number()

temp2 = Temp()
temp2.get_number()

temp3 = Temp()
temp3.get_number()


class Rule:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

rules = []

for i in range(1,5):
    rules.append(Rule(i, i+2, i+3))

rules = [{"a": dat.a, "b": dat.b} for dat in rules]
print("rules: {}".format(rules))