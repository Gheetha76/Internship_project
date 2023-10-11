
# Task 1. Reverse a negative integer and keep the negative sign at the beginning.
# Example: -189 -> -981


def reverse_integer(n: int):

    s = str(n)
    return int('-' + s[:0:-1])


print(reverse_integer(-189))
print(reverse_integer(123))

# Task 2. Write a function that takes two strings as input and returns True if they are anagrams of each other, and False otherwise.
# The strings can contain uppercase and lowercase letters, and should be ignored during the comparison.
#
# Examples:
# Word 1: “race” Word 2: “care” should return “True”
# Word 1: “hEArt” Word 2: “earth” should return “True”
# Word 1: “rattle” Word 2: “battle” should return “False”
#
# Hints:
# Convert both input strings to lowercase (to ignore case)
# Sort both strings
# Compare the sorted strings. If they are the same, the original strings are anagrams


def is_anagram(s1: str, s2: str):

    if len(s1) != len(s2):
        return False
    if sorted(s1.lower()) == sorted(s2.lower()):
        return True
    else:
        return False

print(is_anagram('race','care'))
print(is_anagram('hEArt','earth'))
print(is_anagram('rattle','battle'))


# Task 3. Given a sentence, reverse the order of characters in each word.
# Examples:
# “Hello World” should be transformed into “olleH dlroW”
# “mistertwister” should be transformed into “retsiwtretsim”
#
# Hint: One of the last steps is the string method .join(). The string method .join() concatenates a list of strings together to create a new string joined with any special character, for ex space, comma, etc.



def reverse_words(sentence: str):
    list_of_words = sentence.split()
    print( list_of_words)
    empty_list = []
    for word in  list_of_words:
        reversed_word = word[::-1]
        empty_list.append(reversed_word)
    print(empty_list)
    joined_words = " ".join(empty_list)
    return(joined_words)

sentence = "PYTHON IS GOOD PRAGRAMMING LANGUAGE"
print(reverse_words(sentence))


# Task 4. Given a string made of digits [0-9], return a string where each digit is repeated a number of times equals to its value.
# Examples:
# “312” should return “333122”
# “102” should return “122”
#
# Hint: In order to repeat each digit a number of times which is equal to its value, for each iteration of the loop take the current character and multiply it by a number of times equal to its integer value.
# Example:


def repeated_numbers(s: str):
    result = ""

    for char in s:
        result += char * int(char)
    return (result)


print(repeated_numbers("567"))
print(repeated_numbers("102"))



# Task 5. Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u) in a given string.
# “y” is not considered a vowel for this task. The input string is always in lowercase.
#
# Examples:
# “hello”     -->  “hll”
# “goodbye”   -->  “gdby”
#
# Hints:
# 1. Check if the character is NOT a vowel (using the NOT operator)
# 2. If not a vowel, add the character to the result string




def shortcut(s: str):
    result = ""
    for char in s:
        if( char not in ('a','e','i','o','u') ):
            result += char

    return(result)

print(shortcut("leopard"))


