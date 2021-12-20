def caesarCipherEncryptor(string, key):
    """
    O(n) time
    O(n) space

    n is the length of the string. 
    """
    ans = ""
    for i in string:
        ans += transfer(i, key)

    return ans


def transfer(character, key):
    idx = ord(character)
    idx += key % 26
    if idx > 122:
        idx -= 26

    return chr(idx)
