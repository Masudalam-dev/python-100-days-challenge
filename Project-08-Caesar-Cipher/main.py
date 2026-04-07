alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
route = input("Type 'encode' for Encrypt and type 'decode' for Decrypt.\n").lower()
message = input("Type your message!\n").lower()
shift_num = int(input("Type the shift number: "))

output = ""
for char in message:
    if char in alphabet:
        shifted_value = (alphabet.index(char) + shift_num) % 26
        output += alphabet[shifted_value]
    else:
        output += char
print("Your encode result is",output)

