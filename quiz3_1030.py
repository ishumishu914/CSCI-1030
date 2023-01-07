def find_sum_n(values, n):
  result =[]
  if len(values) == 1:
    return values[0]
  else:
    for i in values:
      if i <= n:
        result.append(i)
        if sum(result) == n:
          return result

print(find_sum_n([1,2,3,4,5,6],15))

# answer 
def find_sum_n2(values, n):
  if len(values) == 0:
    return []
  elif len(values) == 1 and values[0] == n:
    return values

  # check remaining of list except for first element
  remaining = find_sum_n2(values[1:], n - values[0])

  if len(remaining) > 0:
    # sum of first element in list and 
    return [values[0]] + remaining
  else:
    return find_sum_n2(values[1:], n)

print(find_sum_n2([1,2,3,4,5,6],15))
