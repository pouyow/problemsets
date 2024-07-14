import emoji

# Read input from the user
x = input().strip()

# Convert the input string to emojis with aliases enabled
s = emoji.emojize(x, language='alias')

# Print the resulting string
print(s)
