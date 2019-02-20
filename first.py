import myModule
# OR from myModule import printTheString
# OR from myModule import *

# from myFolder import tempFile
# tempFile.temp()
# OR
import myFolder.tempFile

myFolder.tempFile.temp()

print('hello')

str = "dipalamodi"
print('str[2:5] : ', str[2:5])  # pal
print('str*2 : ', str * 2)  # dipalamodidipalamodi
print('str[2:] : ', str[2:])  # palamodi

mylist = ['can', 'be', 'changed']
mytuple = ('cannot', 'be', 'changed')

mydict = {'name': 'dipal', 'lastname': 'modi'}
mydict['occupation'] = 'job'
print('mydict: ', mydict)
print('keys :', mydict.keys())
print('values: ', mydict.values())

print('if: ', 'can' in mylist)

if len(mytuple) == 4:
    print('Length is 4')
elif 'hh' not in mytuple:
    print('\'hh\' not in mytuple')
else:
    print('In else')

for key, value in mydict.items():
    print('Key: ', key, ' Value: ', value)

try:
    key = input('Enter key to search in the mydict: ')
    print('searched result: ', mydict[key])
except KeyError:
    print('key does not exist')

mylist2 = [1, 2, 3]
mylist.extend(mylist2)
print(mylist)

print('Imported from the module: ', myModule.printTheString('Hello', 'world', 'Dipal'))
print('Imported from the module: ', myModule.printTheString('Hello', 'world'))


# Within a module, the module’s name (as a string) is available as the value of the global variable __name__.
def func():
    print('calling function: ', __name__)
    return


func()
