def line(text):
    s = text.replace("-", " ").replace("_", " ")
    s = s.split()
    if len(text) == 0:
        return text
    return s[0] + ''.join(i.capitalize() for i in s[1:])
print(line("the-stealth-warrior"))
print(line("The_Stealth_Warrior"))

def next_palin(n):
    while True:
        n += 1
        if str(n) == str(n)[::-1]:
            return n

n = int(input("Введите число: "))
print(next_palin(n))
