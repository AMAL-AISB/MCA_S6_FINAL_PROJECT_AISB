
with open('results.txt','r') as f1, open('output.txt', 'w') as f2:
	f2.write("".join([c for c in f1.read() if not c.isdigit()]))


import re

string = open('output.txt').read()
new_str = re.sub('[^a-zA-Z\n\.]', '', string)
open('b.txt', 'w').write(new_str)

with open('b.txt', 'r') as fin:
	data = fin.read().splitlines(True)
with open('c.txt', 'w') as fout:
	fout.writelines(data[1:])