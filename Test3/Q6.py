import requests

upper_case = requests.get('http://127.0.0.1:8090/upcase/HaveANiceDay', auth=('Silver', 'Surfer')).text
myLength = requests.get('http://127.0.0.1:8090/length/HaveANiceDay', auth=('Silver', 'Surfer')).text
the_reverse = requests.get('http://127.0.0.1:8090/reverse/HaveANiceDay', auth=('Silver', 'Surfer')).text
the_sorted = requests.get('http://127.0.0.1:8090/sort_str/HaveANiceDay', auth=('Silver', 'Surfer')).text

print("Length of string is " + myLength)
print("Uppercase string is " + upper_case)
print("Sorted string is " + the_sorted)
print("Reversed string is " + the_reverse)
