#1
print("Number 1: ")
#A
print("A:")

print ("""
1
    2
        3
""" )
#B
print("B:")
text = "Text.\nNext line."
print (text)
#C
print("C:")
print ('One', ' Two ' * 2)
print ('One ' + 'Two' * 2)
print (len('0123456789'))
#D
print("D: ")
s = '0123456789'
print(s[3], ", ", s[0 : 3],"-", s[2 : 5])

print(s[:3], " - ", s[3:], " , ", s[3:100])

print(s[20:], s[2:1], s[1:1])
#E
print("E: ")
s = '987654321'
print(s[-1], s[-3])
print(s[-3:], s[:-3])
print(s[-100:-3], s[-100:3])

#2.
print("2: ")
#A
print("A: ")
y = str(123)
x = "hello" * 3
print(x, y)
x = "hello" + "world"
y = len(x)
print(y, x)
#B
print("B: ")
x = "hello" + \
    "to Python" + \
    "world"
for char in x:
    y = char
    print(y, ':', end='')
#C
print("C: ")

x = "hello world"
print(x[:2], x[:-2], x[-2:])
print(x[6], x[2:4])
print(x[2:-3], x[-4:-2])

#3.
print("3: ")

theStr = "This is a test."
inputStr = input("Enter integer: ")
inputInt = int(inputStr)
testStr = theStr
while inputInt >= 0:
    testStr = testStr[1:-1]
    inputInt = inputInt - 1
testBool = "t" in testStr
print(theStr)    # Line 1
print(testStr)   # Line 2
print(inputInt)  # Line 3
print(testBool)  # Line 4

#4
print("4: ")
testStr = "abcdefghi"
inputStr = input("Enter integer: ")
inputInt = int(inputStr)
count = 2
newStr = ""
while count <= inputInt:
    newStr = newStr + testStr[0:count]
    testStr = testStr[2:] #Line 1
    count = count + 1
print(newStr)             # Line 2
print(testStr)            # Line 3
print(count)              # Line 4
print(inputInt)           # Line 5





















