class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        """
        O(n^2) time
        O(n^2) space

        n is the length of the string.
        """
        for i in range(len(string)):
            substring = string[i:]
            self.helper(substring)

    def helper(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                node[letter] = {}
            node = node[letter]

        node[self.endSymbol] = True

    def contains(self, string):
        """
        O(m) time
        O(1) space

        m is the length of the string.
        """
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]

        return self.endSymbol in node
