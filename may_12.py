def restore_snow():
  n = int(input())
  a = list(map(int, input().split()))
  res = [0] * n  # Здесь будут восстановленные суммарные значения

  i = 0
  while i < n:
    if a[i] != -1:
      res[i] = a[i]
      i += 1
    else:
      # найти следующий известный
      j = i
      while j < n and a[j] == -1:
        j += 1

      if i == 0:
        # если в начале
        for k in range(j):
          res[k] = k + 1
      elif j == n:
        # если в конце
        for k in range(i, n):
          res[k] = res[k - 1] + 1
      else:
        left = res[i - 1]
        right = a[j]
        steps = j - i + 1  # сколько дней между значениями (включая j)
        diff = right - left
        if diff < steps:
          print("NO")
          return
        # Приросты: сначала по +1, а на последнем дне остаток
        for k in range(i, j):
          res[k] = res[k - 1] + 1
        res[j] = res[j - 1] + (diff - (steps - 1))

      i = j + 1 if j < n else n

  # Проверим корректность
  for i in range(1, n):
    if res[i] <= res[i - 1]:
      print("NO")
      return

  print("YES")
  print(' '.join(str(res[0]) if i == 0 else str(res[i] - res[i - 1]) for i in range(n)))


restore_snow()
