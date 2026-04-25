text = "Hello, World!"
print(text[0:5])  # Output: "Hello" characters from index 0 to 4
print(text[:5])  # Output: "Hello" characters from the beginning to index 4
print(text[7:])  # Output: "World!" characters from index 7 to the end
print(text[7:12])  # Output: "World" characters from index 7 to 11
print(text[-6:])  # Output: "World!" characters from the sixth character from the end to the end
print(text[:-6])  # Output: "Hello, " characters from the beginning to the sixth character from the end
print(text[::2])  # Output: "Hlo ol!" characters from the beginning to the end with a step of 2 (every second character)
print(text[::-2])  # Output: "Hlo ol!" characters from the beginning to the end with a step of 2 (every second character)
print(text[1::2])  # Output: "el,Wrd" characters from index 1 to the end with a step of 2 (every second character starting from index 1)
print(text[::-1])  # Output: "!dlroW ,olleH" characters from the end to the beginning (reversed string)
print(text[::3])  # Output: "Hl r!" characters from the beginning to the end with a step of 3 (every third character)
print(text[1:10:2])  # Output: "el,W" characters from index 1 to 9 with a step of 2 (every second character starting from index 1)
print(text[10:1:-2])  # Output: "o,W" characters from index 10 to 2 with a step of -2 (every second character in reverse starting from index 10)