words = dict()
words["adjectives"] = ["red", "wet", "bad"]
words["nouns"] = ["cars", "bird", "island"]
words["verbs"] = ["strike", "slice"]
words['nationality'] = ["Persian"]


p = f"""{words['adjectives'][0]} (adjective) is better than ugly.
{words["adjectives"][1]} (adjective) is better than implicit.
Simple is better than {words["adjectives"][2]} (adjective).
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special {words['nouns'][0]} (plural noun) aren't special enough to break the rules.
Although practicality beats purity.
Errors should never {words['verbs'][0]} (verb) silently.
Unless explicitly silenced.
In the face of ambiguity, {words['verbs'][1]} (verb) the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're {words['nationality'][0]}(nationality).
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad {words['nouns'][1]}(noun).
If the implementation is easy to explain, it may be a good {words['nouns'][2]}(noun).
Namespaces are one honking great idea -- let's do more of those!"""


if 1 == 0:

  print(p)

else:

  print("woot")



y = ["apples", "watermelons", "starberries", "lemons"]
x = ["carrots", "peas", "lettuce", "asparagus"]

# for values in zip(y, x):
#   print(values)

# for values in enumerate(x):
#   print(values)


g = [i for i in range(10)]
print(g)

c = []
# for every element in x
for i in x:
  # if the length of element is greater or equal to 5
  if len(i) >= 5:
    # append to list c
    c.append(i)

# print list c
print(c)

k = [n[1:4] for n in x]
print(k)

pangram = 'The quick brown fox jumps over the lazy dog'
# vowels = []
vowels = ("a", "e", "i", "o", "u")
no_vowels = []
for v in pangram:
  # if "a" in v or "e" in v or "i" in v or "o" in v or "u" in v:
  if v not in vowels:
    no_vowels.append(v)

no_vowels_pangram = ''.join(no_vowels)
# print(no_vowels_pangram)

#list comprehension
#hint: you'll probably need to use .join()


try:
  int('s')
  print("it work")

except:

  print("didn't work")

pass

# finally:
#   print("continue")


def my_func(x):
  x = x + 1
  return x

print(my_func(2))
