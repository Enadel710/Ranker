import math

n = int(input("Enter the number of things you would like to rank: "))
sum_min = 0
sum_max = 0

for i in range(1, n+1):
  min_value = math.floor(math.log(i, 2))
  max_value = math.ceil(math.log(i, 2))
  sum_min += min_value
  sum_max += max_value
  # print(" " + str(i) + ":\tmin_value " + str(min_value) + ", max_value " + str(max_value) + ", sum_min " + str(sum_min) + ", sum_max " + str(sum_max))

print("\nMinimum number of questions for ranking " + str(n) + " things is " + str(sum_min))
print("Average number of questions for ranking " + str(n) + " things is " + str(math.ceil((sum_min + sum_max) / 2)))
print("Maximum number of questions for ranking " + str(n) + " things is " + str(sum_max))
