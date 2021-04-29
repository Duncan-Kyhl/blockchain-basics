import hashlib
x = 5
y = 0  # We don't know what y should be yet...
#while sha256('0'.encode()).hexdigest()[-1] != "0":
#    y += 1
# print(f"The solution is y = {y}")

output = hashlib.sha256("105")
output.update(b"update")
#print(output.digest_size)
#print(output.digest())

hex = output.hexdigest()
print(hex)
print(hex.encode())
