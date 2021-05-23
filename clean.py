with open("output_book.txt","r") as f, open("fin.txt","w") as outfile:
	for i in f.readlines():
		if not i.strip():
			continue
		if i:
			outfile.write(i)
