import numpy as np
import random

def generate_pop(size):
  return np.random.randint(-10, 10, size = size)


def to_bin(number):
  return format(number, "05b")


def to_int(binary):
  return int(binary, 2)


def get_zero_value(pop):
  results = {}
  for i in pop:
    result = (i*i) - (3*i) + 4
    results[i] = abs(result)
    
  zero = min(results.values())
  print("results ", results)

  index = list(results.values()).index(zero)
  return list(results)[index]


def cross_times(pop, times):
  results = []
  for _ in range(times): results += cross(pop)
  return results


def cross(pop):
  new_first = None
  new_second = None

  while True:
    indexes = random.sample(range(len(pop)), 2)
    first_index = indexes[0]
    second_index = indexes[1]

    first_bin = to_bin( pop[first_index] ) 
    second_bin = to_bin( pop[second_index] )
    cut = random.randrange(1,5)

    new_first = merge_bins(first_bin, second_bin, cut)
    new_second = merge_bins(second_bin, first_bin, cut)

    if is_valid_number(new_first) and is_valid_number(new_second): break

  return [new_first, new_second]


def is_valid_number(number):
  return number >= -10 and number <= 10


def merge_bins(first_bin, second_bin, cut):
  return to_int(first_bin[:cut] + second_bin[cut:])


def mutation(pop, times):
  results = []
  for x in range(times):
    while True:
      index = random.randrange(len(pop))
      binary = to_bin(pop[index])
      index = random.randrange(len(binary))

      if index == 0:
        if binary[index] == '-': binary = replace_bin(binary, index, '0')
        else: binary = replace_bin(binary, index, '-')
      elif binary[index] == '0': binary = replace_bin(binary, index, '1')
      else: binary = replace_bin(binary, index, '0')

      number = to_int(binary)
      if is_valid_number(number):
        results.append(number)
        break
  return results


def replace_bin(bin_num, index, value):
  list_bin = list(bin_num)
  list_bin[index] = value
  return ''.join(list_bin)


def ga(pop_size, generation, cross, mutations):
  pop = generate_pop(pop_size)
  print("First pop ", pop)

  final = []
  for x in range(generation):
    results = []
    results.append(get_zero_value(pop))
    results += cross_times(pop, cross)
    results += mutation(pop, mutations)
    
    pop = results
    final.append(results)
  return final

  
print("Final results: ", ga(4,5,2,1))