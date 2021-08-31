def fuzzy_triangular(d):
  dim = d + 1
  value = 1/dim
  results = []
  for x in range(d + 1): results.append(value * (x+1))
  return results + results[:d][::-1]

fuzzy_triangular(1)
fuzzy_triangular(2)
fuzzy_triangular(3)
fuzzy_triangular(4)
fuzzy_triangular(5)


