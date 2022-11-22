def line(text):
  text_arr = list(text)
  i = 0
  while i < len(text_arr):
    if text_arr[i] == '-' or text_arr[i] == '_':
      del text_arr[i]
      if i != len(text_arr) - 1 and text_arr[i].isalpha():
        text_arr[i] = text_arr[i].upper()
        i += 1
    else:
      i += 1
  return ''.join(text_arr)

print(line("the-stealth-warrio"))
print(line("The_Stealth_Warrior"))
