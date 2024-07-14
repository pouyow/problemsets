import emoji

x = input().strip()
s = emoji.emojize(x, language='alias')
print(s)
