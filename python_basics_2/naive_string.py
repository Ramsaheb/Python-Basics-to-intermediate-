def naive_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i)

    return matches

# Example usage:
text = "ababcababcabc"
pattern = "abc"
print("Pattern found at indices:", naive_string_match(text, pattern))
