import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

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
        else:
            output += char
    print(f"Your decode result: {output}")



while True:
    route = input("Type 'encode' for Encrypt and type 'decode' for Decrypt.\n").lower()
    if route not in ["encode","decode"]:
        print("Invalid input")
        continue

    message = input("Type your message!\n").lower()

    while True:
        shift = input("Type the shift number: ")
        if shift.isdigit():
            int_shift = int(shift) % 26
            break
        print("Please enter number.")

    if route == "encode":
        encrypt(original_text=message, shift_num=int_shift)
    else:
        decrypt(original_text=message, shift_num=int_shift)

    user_exit = input("Type 'Yes' to continue and 'No' to exit.")
    if  user_exit.lower() == "no":
        print("Goodbye 🙋‍♂️.")
        break

