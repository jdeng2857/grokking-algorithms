def sum(arr):
  total = 0
  for x in arr:
    total += x
  return total

def recursive_sum(arr):
  if len(arr) == 0:
    return 0
  else:
    element = arr.pop()
    return element + recursive_sum(arr)

print(sum([1, 2, 3, 4]))
print(recursive_sum([1, 2, 3, 4]))

def quicksort(array):
  if len(array) < 2:
    return array
  else:
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))