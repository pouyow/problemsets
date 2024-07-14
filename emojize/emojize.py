import emoji

x = input().strip
s = emoji.emojize(x, use_aliases=True)
print(s)
