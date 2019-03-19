def reverse(text):
  b = ""
  for i in range(len(text), 0, -1):
    b += text[i-1]
  print(b)
  print(b)
  return b

reverse("abecedario")
