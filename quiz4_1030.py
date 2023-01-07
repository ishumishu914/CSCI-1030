import re

def recognize_ip_address(test_string):
  regex = "^(\d{1,3}\.)(\d{1,3}\.)(\d{1,3}\.)(\d{1,3})$"

  if re.match(regex, test_string):
    return True
  else:
    return False

str1 = '1.2.3.4'
print(f'recognize_ip_address({str1}) =>', recognize_ip_address(str1))

str2 = '255.255.255.255'
print(f'recognize_ip_address({str2}) =>', recognize_ip_address(str2))

str3 = '173.201.64.8'
print(f'recognize_ip_address({str3}) =>', recognize_ip_address(str3))

str4 = '23.64.18.201.3'
print(f'recognize_ip_address({str4}) =>', recognize_ip_address(str4))

str5 = '201.1295.6.14'
print(f'recognize_ip_address({str5}) =>', recognize_ip_address(str5))

str6 = '38.126.84'
print(f'recognize_ip_address({str6}) =>', recognize_ip_address(str6))