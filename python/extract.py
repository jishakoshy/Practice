# extract digit from a string

def extract_digits(input_string):
    digits = ''
    for char in input_string:
        if char.isdigit():
            digits += char
    return digits

# Example usage:
input_string = "abc123def456ghi"
extracted_digits = extract_digits(input_string)
print("Digits extracted from the string:", extracted_digits)

