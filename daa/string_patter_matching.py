import timeit
import re

# General string find using built-in method
def find_pattern_general(text, pattern):
    return text.find(pattern) != -1

# Using regex to find a pattern
def find_pattern_regex(text, pattern):
    return bool(re.search(pattern, text))

# Brute force pattern matching
def find_pattern_brute_force(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m:
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == m:  # Match found
            return True
    return False  # No match found

# Sample text and pattern
text = "This is a sample text where we will search for a pattern."
pattern = "search"

# Time the different pattern matching approaches
t_general_find = timeit.timeit(lambda: find_pattern_general(text, pattern), number=10000)
t_regex = timeit.timeit(lambda: find_pattern_regex(text, pattern), number=10000)
t_brute_force = timeit.timeit(lambda: find_pattern_brute_force(text, pattern), number=10000)

# Print execution times
print("Time taken for general approach (using find()):", t_general_find)
print("Time taken for regex approach:", t_regex)
print("Time taken for brute force technique:", t_brute_force)
