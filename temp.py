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
