import math

def compute_hamming_code(data):
    # Convert the decimal to binary string
    binary_str = bin(data)[2:]
    n = len(binary_str)
    
    # Determine number of parity bits needed
    m = 0
    while (2 ** m) < (n + m + 1):
        m += 1
    
    # Initialize Hamming code array with placeholders for parity bits
    hamming_code = ['0'] * (n + m)
    
    # Fill data bits
    j = 0
    for i in range(1, n + m + 1):
        if math.log2(i).is_integer():
            hamming_code[i - 1] = 'p'  # Placeholders for parity bits
        else:
            hamming_code[i - 1] = binary_str[j]
            j += 1
    
    # Calculate parity bits
    for i in range(m):
        parity_pos = 2 ** i
        parity_value = 0
        
        for j in range(1, n + m + 1):
            if j & parity_pos == parity_pos:
                if hamming_code[j - 1] != 'p':
                    parity_value ^= int(hamming_code[j - 1])
        
        hamming_code[parity_pos - 1] = str(parity_value)
    
    # Calculate the overall parity bit at position 0
    overall_parity = 0
    for bit in hamming_code:
        overall_parity ^= int(bit)
    
    hamming_code.insert(0, str(overall_parity))
    
    return ''.join(hamming_code)

def main():
    # Ask the user to enter a number
    data = int(input("Enter a number to encode: "))
    encoded_hamming = compute_hamming_code(data)
    print(f"Encoded Hamming code for {data} is: {encoded_hamming}")

if __name__ == "__main__":
    main()
