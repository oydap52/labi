def disemvowel(string):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in string if char not in vowels)

print(disemvowel("This website is for losers LOL!"))