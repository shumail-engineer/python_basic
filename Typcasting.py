print("=== Implicit Typecasting ===")
a = 10      
b = 5.5    

c = a + b     
print(f"Type of a: {type(a)}")
print(f"Type of b: {type(b)}")
print(f"Result (c): {c}")
print(f"Type of c: {type(c)}")

print("\n=== Explicit Typecasting ===")

# Explicit Typecasting
x = 15.67
y = int(x)  
print(f"Float value: {x}")
print(f"After converting to int: {y}")

# String to int
str_num = "123"
int_num = int(str_num)
print(f"String value: {str_num} (type: {type(str_num)})")
print(f"Converted to int: {int_num} (type: {type(int_num)})")

# Int to string
num = 456
str_converted = str(num)
print(f"Integer value: {num} (type: {type(num)})")
print(f"Converted to string: {str_converted} (type: {type(str_converted)})")

# Float to string
f = 3.14
s = str(f)
print(f"Float to string: {s} (type: {type(s)})")

# Boolean to int
b = True
i = int(b)
print(f"Boolean value: {b} converted to int: {i}")
