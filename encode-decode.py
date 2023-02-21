import base64

def encode_input(input_data):
    encoded = base64.b64encode(input_data)
    return encoded.decode('utf-8')

def encode_file(file_in):
    with open(file_in, 'rb') as f_in:
        encoded = base64.b64encode(f_in.read())
        return encoded.decode('utf-8')

def decode_input(input_data):
    decoded = base64.b64decode(input_data.encode('utf-8'))
    return decoded

def decode_file(file_in):
    with open(file_in, 'rb') as f_in:
        decoded = base64.b64decode(f_in.read())
        return decoded

def main():
    # Accept input from user
    print('\nType the number that corresponds with the option you want.\n\nOptions:\n\n1: to encode a file\n\n2: to decode a file\n\n3: to encode text\n\n4: to decode text\n\n\n\n')
    choice = input()
    
    if choice == '1':
        file_in = input('\nEnter the name/path of the file to encode: ')
        try:
            with open(file_in, 'rb') as f:
                pass
        except FileNotFoundError:
            print("\nError: File not found")
            return
        file_out = input('\nEnter the name of the output file: ')
        encoded = encode_file(file_in)
        with open(file_out, 'w') as f_out:
            f_out.write(encoded)
    
    elif choice == '2':
        file_in = input('\nEnter the name/path of the file to decode: ')
        try:
            with open(file_in, 'rb') as f:
                pass
        except FileNotFoundError:
            print("\nError: File not found")
            return
        file_out = input('\nEnter the name of the output file: ')
        with open(file_in, 'r') as f_in:
            encoded = f_in.read()
        decoded = decode_input(encoded)
        with open(file_out, 'wb') as f_out:
            f_out.write(decoded)
    
    elif choice == '3':
        text_in = input('\nEnter the text to encode: ')
        if not text_in:
            print("\nError: No text input found")
            return
        encoded = encode_input(text_in.encode('utf-8'))
        print('\nEncoded text:', encoded)
    
    elif choice == '4':
        text_in = input('\nEnter the text to decode: ')
        if not text_in:
            print("\nError: No text input found")
            return
        decoded = decode_input(text_in)
        print('\nDecoded text:', decoded.decode('utf-8'))
    
    else:
        print('\nInvalid choice. Please try again.')

if __name__ == '__main__':
    main()
