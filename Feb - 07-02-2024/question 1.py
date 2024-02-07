# WAP to check if the words is anagrams or not.

# Question 1

w1 = input("Give a word")
w2 = input("Give a word")

w1 = sorted(w1.lower().replace(" ", ""))
w2 = sorted(w2.lower().replace(" ", ""))

if (w1 == w2):
  print("This is an anagram")
else:
  print("This is not an anagram")