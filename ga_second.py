import random
import numpy as np

default_values = [(1, 11), (2, 21), (3, 35), (4, 53), (5, 75)]

def generate_pop():
  return np.random.randint(-10, 10, size = 3)


def avaliation(points):
  a = points[0]
  b = points[1]
  c = points[2]
  error_rate = 0
  for x, expected in default_values:
    result = a * (x*x) + (b*x) + c
    error_rate += abs(expected - result)
  return error_rate


def to_bin(number):
  return format(number, "05b")


def to_int(binary):
  return int(binary, 2)

def merge_bins(first_bin, second_bin, cut):
  return to_int(first_bin[:cut] + second_bin[cut:])


def cross(pop):
  first_point = None
  second_point = None
  while True:
    indexes = random.sample(range(len(pop)), 2)
    point_indexes = random.sample(range(2), 2)
    first_index = indexes[0]
    second_index = indexes[1]
    point_index_first = point_indexes[0]
    point_index_second = point_indexes[1]
    #
    first_bin = to_bin( pop[first_index][point_index_first] ) 
    second_bin = to_bin( pop[second_index][point_index_second] )
    cut = random.randrange(1,5)
    #
    new_first = merge_bins(first_bin, second_bin, cut)
    new_second = merge_bins(second_bin, first_bin, cut)
    #
    if is_valid_number(new_first) and is_valid_number(new_second):
      first_point = pop[first_index]
      first_point[point_index_first] = new_first
      second_point = pop[second_index]
      second_point[point_index_second] = new_second
      break
  return [first_point, second_point]


def mutation(pop):
  results = []
  for x in range(2):
    while True:
      index_pop = random.randrange(len(pop))
      point_index = random.randrange(2)
      binary = to_bin(pop[index_pop][point_index])
      index = random.randrange(len(binary))
      if index == 0:
        if binary[index] == '-': binary = replace_bin(binary, index, '0')
        else: binary = replace_bin(binary, index, '-')
      elif binary[index] == '0': binary = replace_bin(binary, index, '1')
      else: binary = replace_bin(binary, index, '0')
      number = to_int(binary)
      if is_valid_number(number):
        result = pop[index_pop]
        result[point_index] = number
        results.append(result)
        break
  return results


def replace_bin(bin_num, index, value):
  list_bin = list(bin_num)
  list_bin[index] = value
  return ''.join(list_bin)


def is_valid_number(number):
  return number >= -10 and number <= 10


def ga(pop_size, generation):
  pop = [ generate_pop() for _ in range(pop_size)]
  print("First pop ", pop)
  final = []
  for x in range(generation):
    results = []
    validateds = [ avaliation(point) for point in pop ]
    index = validateds.index(min(validateds))
    results.append(pop[index])
    if validateds[index] == 0:
      print("Better result founded with ", pop[index])
    results += cross(pop)
    results += mutation(pop, len(pop))
    pop = results
    print("results ", results)
    final.append(results)
  return results
