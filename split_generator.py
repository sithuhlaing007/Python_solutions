def make_word():
  word = ""
  get = input("Enter a word : ")
  for ch in get:
    word +=ch
    yield word

print(list(make_word()))