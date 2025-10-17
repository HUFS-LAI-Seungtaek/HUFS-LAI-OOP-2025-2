from dsops import train_test_split, label_distribution

if __name__ == "__main__":
	tr, te = train_test_split([1,2,3,4,5], 0.4, seed=42)
	print(tr, te)
	print(label_distribution(["cat","dog","cat"]))
	print(train_test_split(list(range(5)), 0.4, seed=0))
	print(label_distribution(["a","b","a"]))