def DPChange(money, Coins):
  minNumCoins = (money + 1) * [0]
  for i in range(1, money + 1):
    minNumCoins[i] = i + 1
    for coin in Coins:
      if i >= coin:
        if minNumCoins[i - coin] + 1 < minNumCoins[i]:
          minNumCoins[i] = minNumCoins[i - coin] + 1

  return minNumCoins[money]
