def ReconstructAString(seq):
  seq_split = seq.split("\n")
  new_seq = seq_split[0]
  k = len(seq_split[0])
  for j in range(1, len(seq_split)):
    if(new_seq.endswith(seq_split[j][:k - 1])):
      new_seq += seq_split[j][k - 1:]
  return new_seq
