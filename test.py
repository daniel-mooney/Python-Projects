

with open("test.txt", "wb") as binary_file:
    i = 123456789
    binary_file.write(i.to_bytes(4, byteorder="big"))

x = "1234"

print(x[0:2])