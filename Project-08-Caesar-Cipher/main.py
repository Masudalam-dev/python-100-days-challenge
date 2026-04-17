alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

route = input("Type 'encode' for Encrypt and type 'decode' for Decrypt.\n").lower()
message = input("Type your message!\n").lower()
shift = int(input("Type the shift number: "))

def encrypt(original_text,shift_num):
    output = ""
    for char in original_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_num) % 26
            output += alphabet[new_position]
        else:
            output += char
    print(f"Your encode result: {output}")



def decrypt(original_text,shift_num):
    output = ""
    for char in original_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_num) % 26
            output += alphabet[new_position]
    print(f"Your decode result: {output}")


if route == "encode":
    encrypt(original_text=message, shift_num=shift)

elif route == "decode":
    decrypt(original_text=message, shift_num=shift)
else:
    print("Invalid input!")




