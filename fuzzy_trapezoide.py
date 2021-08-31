def fuzzy_trapezoide(left, middle, right):
  middle = np.ones(middle)
  results_right = []
  results_left = []
  for x in range (left): results_left.append((1/(left + 1)) * (x+1))
  for x in range (right): results_right.append((1/(right + 1)) * (x+1))
  return results_left + middle.tolist() + results_right[::-1]


fuzzy_trapezoide(3,1,5)
fuzzy_trapezoide(1,1,1)
fuzzy_trapezoide(5,2,3)
fuzzy_trapezoide(2,2,2)
fuzzy_trapezoide(2,4,3)