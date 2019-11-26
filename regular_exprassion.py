import re 
from input import string_from_terminal as sft

pattern = sft.str_from_terminal()
#print(string)
string = r''

results = re.findall(pattern, string)