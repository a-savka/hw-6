from multiprocessing import Process, Pipe
import time

def calculate_function_1(conn, x, iterations):
  for _ in range(iterations):
    y = x**2 - x**2 + x*4 - x*5 + x + x
  conn.send((y, time.time()))
  conn.close()

def calculate_function_2(conn, x, iterations):
  for _ in range(iterations):
    y = x + x
  conn.send((y, time.time()))
  conn.close()

def calculate_function_3(conn, x, y, iterations):
  for _ in range(iterations):
    z = x + y
  conn.send((z, time.time()))
  conn.close()

def input_arg():
  x = None
  while x == None:
    try:
      x = int(input('Введите аргумент: '))
    except:
      pass
  return x

def calculate(x, iterations):

  parent_conn1, child_conn1 = Pipe()
  p1 = Process(target=calculate_function_1, args=[child_conn1, x, iterations])
  start1 = time.time()
  p1.start()

  parent_conn2, child_conn2 = Pipe()
  p2 = Process(target=calculate_function_2, args=[child_conn2, x, iterations])
  start2 = time.time()
  p2.start()

  p1.join()
  p2.join()

  (y1, end1) = parent_conn1.recv()
  (y2, end2) = parent_conn2.recv()


  parent_conn3, child_conn3 = Pipe()
  p3 = Process(target=calculate_function_3, args=[child_conn3, y1, y2, iterations])
  start3 = time.time()
  p3.start()

  p3.join()
  (z, end3) = parent_conn3.recv()


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

if __name__ == '__main__':
  main()
