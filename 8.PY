s = "programming"
freq = {}
for chr in s:
    freq[chr] = freq.get(chr,0) +1
    print(freq)