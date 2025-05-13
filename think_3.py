n, a, b = map(int, input().split())
s = input().strip()

# Заменяем символы "О" и "К" на "(" и ")" для удобства
s = s.replace('О', '(').replace('К', ')')

balance = 0
cost = 0

for i in range(len(s)):
    if s[i] == '(':
        balance += 1
    else:
        balance -= 1
    
    if balance < 0:
        # Ищем следующую "(" для обмена
        j = i + 1
        while j < len(s) and s[j] != '(':
            j += 1
        if j < len(s) and a < b:
            # Меняем местами s[i] и s[j]
            cost += a
            balance += 2  # После обмена баланс увеличивается на 2
            # Обновляем строку (для баланса)
            s = s[:i] + '(' + s[i+1:j] + ')' + s[j+1:]
        else:
            # Заменяем текущий символ на "("
            cost += b
            balance += 2  # После замены баланс увеличивается на 2
            s = s[:i] + '(' + s[i+1:]

print(cost)