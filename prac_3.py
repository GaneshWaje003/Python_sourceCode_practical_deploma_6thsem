# # Write a program to convert U.S. dollars to Indian rupees

# usd = float(input("Enter amount in U.S. dollars: "))
# usd_to_inr_rate = 73.34
# inr = usd * usd_to_inr_rate
# print("${:.2f} is equivalent to ₹{:.2f}".format(usd, inr))


# # Write a program to convert bits to bytes, MegaBytes, GigaBytes and TeraBytes

# def convert_bits_to_bytes(bits):
#     bytes = bits / 8
#     return bytes

# def convert_bytes_to_Megabytes(bytes):
#     Megabytes = bytes / (1024 * 1024)
#     return Megabytes

# def convert_bytes_to_Gigabytes(bytes):
#     Gigabytes = bytes / (1024 * 1024 * 1024)
#     return Gigabytes

# def convert_bytes_to_Terabytes(bytes):
#     Terabytes = bytes / (1024 * 1024 * 1024 * 1024)
#     return Terabytes

# bits = int(input("Enter the number of bits: "))

# bytes = convert_bits_to_bytes(bits)
# print(f"{bits} bits is equal to {bytes} bytes")

# Megabytes = convert_bytes_to_Megabytes(bytes)
# print(f"{bits} bits is equal to {Megabytes} Megabytes")

# Gigabytes = convert_bytes_to_Gigabytes(bytes)
# print(f"{bits} bits is equal to {Gigabytes} Gigabytes")

# Terabytes = convert_bytes_to_Terabytes(bytes)
# print(f"{bits} bits is equal to {Terabytes} Terabytes")


# # Write a program to Find the square root

# def sqrt(number):

#     guess = number / 2
#     while abs(guess**2 - number) > 0.0001:
#         guess = (guess + number / guess) / 2
#     print(f"Square root of {number} is ",guess)

# sqrt(16)

# # Write a Program to print Area of rectangle

# length = float(input("Enter length of Rectangle: "))
# width = float(input("Enter width of Rectangle: "))
# area = length * width

# print("Area of Rectangle:", area)

# # Write a program to print Area and Perimeter of the square

side_length = float(input("Enter the length of the square's side: "))
area = side_length ** 2
perimeter = 4 * side_length
print(f"The area of the square is {area} units.")
print(f"The perimeter of the square is {perimeter} units.")


# # Write a program to Print Surface area of cylinder and volume also

# pi  = 3.14
# r = float(input("Enter the radius of the cylinder: "))
# h = float(input("Enter the height of the cylinder: "))

# surface_area = 2*pi*r*h + 2*pi*(r**2)
# volume = pi*(r**2)*h

# print("Surface Area of Cylinder =", round(surface_area, 2))
# print("Volume of Cylinder =", round(volume, 2))

# a = input("Enter the value of first variable: ")
# b = input("Enter the value of second variable: ")

# temp = a
# a = b
# b = temp

# print("\nAfter swapping:")
# print("a =", a)
# print("b =", b)
