import timeit

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

# Time the brute force pattern matching approach
t_brute_force = timeit.timeit(lambda: find_pattern_brute_force(text, pattern), number=10000)

# Print execution times for brute force
print("Time taken for brute force technique:", t_brute_force)
