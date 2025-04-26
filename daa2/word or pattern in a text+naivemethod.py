import timeit

# General string find using built-in method
def find_pattern_general(text, pattern):
    return text.find(pattern) != -1

# Sample text and pattern
text = "This is a sample text where we will search for a pattern."
pattern = "search"

# Time the general string find approach
t_general_find = timeit.timeit(lambda: find_pattern_general(text, pattern), number=10000)

# Print execution times for the general approach
print("Time taken for general approach (using find()):", t_general_find)
