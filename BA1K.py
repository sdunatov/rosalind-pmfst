from itertools import product

def FrequencyArray(text, k):
  patterns = []
  
  all_k_mers = [''.join(i) for i in product('ACGT', repeat = k)]
  freq_arr = [0] * len(all_k_mers)
  for i in range(len(text) - (k - 1)):
    patterns.append(text[i:k+i])
  for i in range(len(patterns)):
    indeks = all_k_mers.index(patterns[i])
    freq_arr[indeks] = freq_arr[indeks] + 1 

  res = " ".join(map(str, freq_arr))
  return res
