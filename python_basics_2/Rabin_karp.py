class RabinKarp:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.text_len = len(text)
        self.pattern_len = len(pattern)
        self.prime = 101  # A prime number for hashing

    def hash(self, s):
        hash_value = 0
        for char in s:
            hash_value = (hash_value * 256 + ord(char)) % self.prime
        return hash_value

    def search(self):
        pattern_hash = self.hash(self.pattern)
        text_hash = self.hash(self.text[:self.pattern_len])

        for i in range(self.text_len - self.pattern_len + 1):
            if pattern_hash == text_hash:
                if self.text[i:i+self.pattern_len] == self.pattern:
                    return i
            if i < self.text_len - self.pattern_len:
                text_hash = (256 * (text_hash - ord(self.text[i]) * (256 ** (self.pattern_len - 1))) + ord(self.text[i + self.pattern_len])) % self.prime
                if text_hash < 0:
                    text_hash += self.prime
        return -1

# Example usage:
text = "ababcababcabc"
pattern = "abc"
rk = RabinKarp(text, pattern)
index = rk.search()
if index != -1:
    print("Pattern found at index:", index)
else:
    print("Pattern not found.")
