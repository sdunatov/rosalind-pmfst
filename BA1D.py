def AllOccurrences(pattern, text):
  positionList = []

  for i in range(len(text) - len(pattern) + 1):
    if text[i:len(pattern)+i] == pattern:
      positionList.append(i)

  position = " ".join(map(str, positionList))
  return position
