
import json

def read_data(file_name):
  data_dict = {}
  with open(file_name) as f:
    f.readline()
    for line in f:
      user_data = None
      try:
        user_data = json.loads(line)
      except:
        pass
      if user_data != None:
        data_dict[user_data['user_id']] = user_data['category']
  return data_dict

def print_enumerated_record(data_list):
  for data in data_list:
    (idx, (user_id, category)) = data
    idx_str = '{: >3d}'.format(idx+1)
    print(f'{idx_str} - {user_id} => {category} ')


def main():
  data_dict = read_data('./purchase_log.txt')

  print('Первые 100 строк данных:')
  print('------------------------')

  en = enumerate(data_dict.items())
  print_enumerated_record([next(en) for _ in range(100)])


main()
