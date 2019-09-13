def word_count(fname):
	with open(fname) as f:
		return Counter(f.read().split())
		print("number of words in the file:",word_count("file1.txt"))
