import urllib.request, urllib.parse, urllib.error

one = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in one:
  words = line.decode().strip()
  for word in words:
    counts[word] = counts.get(word,0) + 1
    
print(counts)

quit()