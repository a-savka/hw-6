import threading
import time

def calculate_function_1(x, result, iterations=10000):
  for _ in range(iterations):
    y = x**2 - x**2 + x*4 - x*5 + x + x
  return result.append((y, time.time()))

def calculate_function_2(x, result, iterations=10000):
  for _ in range(iterations):
    y = x + x
  return result.append((y, time.time()))

def calculate_function_3(x, y, result, iterations=10000):
  for _ in range(iterations):
    z = x + y
  return result.append((z, time.time()))


def input_arg():
  x = None
  while x == None:
    try:
      x = int(input('Введите аргумент: '))
    except:
      pass
  return x

def calculate(x, iterations):

  result_f1 = []
  tf1 = threading.Thread(target=calculate_function_1, args=[x, result_f1], kwargs={'iterations': iterations})
  start1 = time.time()
  tf1.start()

  result_f2 = []
  tf2 = threading.Thread(target=calculate_function_2, args=[x, result_f2], kwargs={'iterations': iterations})
  start2 = time.time()
  tf2.start()

  tf1.join()
  tf2.join()

  (y1, end1) = result_f1[0]
  (y2, end2) = result_f2[0]

  result_f3 = []
  tf3 = threading.Thread(target=calculate_function_3, args=[y1, y2, result_f3], kwargs={'iterations': iterations})
  start3 = time.time()
  tf3.start()

  tf3.join()

  (z, end3) = result_f3[0]

  print('-----------------------------------------')
  print(f'итераций: {iterations}')
  print(f'Результат: {z}')
  print(f'Выполнение шага 1: {end1 - start1} сек.')
  print(f'Выполнение шага 2: {end2 - start2} сек.')
  print(f'Выполнение шага 3: {end3 - start3} сек.')
  print('-----------------------------------------')
  print()


def main():
  x = input_arg()
  calculate(x, 10000)
  calculate(x, 100000)
  calculate(x, 1000000)

main()