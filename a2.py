print('hello world');
a=2;
b=3;
c=a+b;
print(c);
print(str(a) + "+" + str(b) + "=" + str(c));

x = 1 # int
y = 2.8 # float
z = 1j # complex
print(type(x));
print(type(y));
print(type(z));

x = 1.10
y = 1.0
z = -35.59

print(type(x));
print(type(y));
print(type(z));

a = "Hello, World!";
print(a[1]);

b = "Hello, World!";
print(b[2:5]);


a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = " Hello, World! "
print(a) # returns "Hello, World!"


thislist = ["apple", "banana", "cherry"]
print(thislist);
thislist = ["apple", "banana", "cherry"]
if "apple1" in thislist:
    print("Yes, 'apple' is in the fruits list")
    print("1")
    print("2")
    print("3")
else:
    print("nothing")

a = "Hello, World!, hi"
print(b.split(","))