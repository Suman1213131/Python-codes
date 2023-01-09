import random
quote_list = []
access = open('inspirationalquotes.txt','rt')
for the_quote in access:
    quote_list.append(the_quote)
access.close()
print("your inspirationalquote for today is:")
print(random.choice(quote_list))
