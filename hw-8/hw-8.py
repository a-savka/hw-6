
def parse_sex(sex):
  if sex.lower() == 'male':
    return 'M'
  elif sex.lower() == 'female':
    return 'F'
  raise Exception('Forbidden gender')

def parse_device_type(devicve_type):
  if devicve_type.lower() in ['mobile', 'tablet']:
    return 'M'
  elif devicve_type.lower() in ['laptop', 'desktop']:
    return 'D'
  raise Exception('Unsupported device type')

def parse_customer(line):
  data = line.split(',')
  customer = {}
  try:
    customer['name'] = data[0]
    customer['device_type'] = parse_device_type(data[1])
    customer['browser'] = data[2]
    customer['sex'] = parse_sex(data[3])
    customer['age'] = int(data[4])
    customer['bill'] = float(data[5])
    customer['region'] = data[6]
  except:
    print('Failed to parse customer, skipping: ' + line)
    return None
  return customer

def sex_to_string(sex):
  return 'женского' if sex == 'F' else 'мужского'

def device_type_to_string(device_type):
  return 'мобильного' if device_type == 'M' else 'настольного'

def bill_to_string(bill):
  if bill.is_integer():
    return '{1:2.{0}f}'.format(int(not bill.is_integer()), bill)
  return '{:2}'.format(bill)

def customer_to_string(customer):
  customer_string = (' '
    'Пользователь {} '
    '{} пола, '
    '{} лет '
    'совершила покупку на {} у.е. '
    'с {} браузера {}. '
    'Регион, из которого совершалась покупка: {}.'
  ).format(
    customer['name'],
    sex_to_string(customer['sex']),
    customer['age'],
    bill_to_string(customer['bill']),
    device_type_to_string(customer['device_type']),
    customer['browser'],
    customer['region']
  )
  return customer_string

def convert_data(input_file_name, outut_file_name):
  with open(input_file_name, 'r') as input_file:
    with open(outut_file_name, 'w') as output_file:
      input_file.readline()
      for line in input_file:
        customer = parse_customer(line.strip())
        if customer != None:
          customer_string = customer_to_string(customer)
          output_file.write(customer_string + '\n')

def main():
  input_file_name = 'web_clients_correct.csv'
  outut_file_name = 'web_clients.txt'
  convert_data(input_file_name, outut_file_name)

main()
