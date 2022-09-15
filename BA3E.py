def deBrujinGraphKmers(patterns):
  patterns = patterns.split("\n")
  D = {}
  first = []
  last = []

  for i in range(len(patterns)):
    first.append(patterns[i][:len(patterns[i]) - 1])
    last.append(patterns[i][1:len(patterns[i])])
  
  for i in range(len(first)):
    if(first[i] + last[i][len(patterns[i]) - 2:] == patterns[i]):
      if first[i] not in D:
        D[first[i]] = [last[i]]
      else:
        D[first[i]].append(last[i])


  out = ""
  keys = sorted(D.keys())
  for first in keys:
    last = ",".join(sorted(D[first]))
    out = out + f"{first} -> {last}\n"
  return print(out)
