"""
Problem 3: T-I-Double Guh-Er II

T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() 
that accepts a string word and returns a new string that removes any 
substrings t, i, gg, and er from word. The function should be case 
insensitive.

Example Usage:
word = "Trigger"
tiggerfy(word)

word = "eggplant"
tiggerfy(word)

word = "Choir"
tiggerfy(word)

Example Output:
"r"
"eplan"
"Chor"
"""


def tiggerfy(word: str) -> str:
    return ""


if __name__ == "__main__":
    word = "Trigger"
    print(tiggerfy(word))

    word = "eggplant"
    print(tiggerfy(word))

    word = "Choir"
    print(tiggerfy(word))
