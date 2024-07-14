import emoji

# Read input from the user
x = input().strip()

# Convert the input string to emojis with aliases enabled
s = emoji.emojize(x, use_aliases=True)

# Print the resulting string
print(s)
