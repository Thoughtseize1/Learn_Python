from collections import UserDict
from collections import UserList
from collections import UserString


class NumberString(UserString):
    '''Створіть клас NumberString, успадкуйте його від класу UserString, визначте для нього метод number_count(self), який буде рахувати кількість цифр у рядку.'''

    def number_count(self):
        count_of_numbers = 0
        for char in self.data:
            if char.isdigit():
                count_of_numbers += 1
        return count_of_numbers


class AmountPaymentList(UserList):
    def amount_payment(self):
        return sum(filter(lambda x: x > 0, self.data))


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        keys = []
        for key, values in self.data.items():
            if values == value:
                keys.append(key)
        return keys


a = LookUpKeyDict()

a["1"] = "Test"
a['2'] = "Test1"
a['3'] = "Test1"
a['4'] = "Test2"
a['5'] = "Test3"
a['6'] = "Test4"

print(a.lookup_key('Test1'))
