import math

n = int(input("Enter the number of things you would like to rank: "))
sum_min = 0
sum_max = 0
sum_options = 0
sum_avg_options = 0

for i in range(1, n+1):
  min_value = math.floor(math.log(i, 2))
  max_value = math.ceil(math.log(i, 2))
  sum_min += min_value
  sum_max += max_value
  sum_options += 1 + math.ceil(math.log(i + 1, 2))
  avg_options = sum_options / (i + 1)
  sum_avg_options += avg_options if i != n else 0
  # print(" " + str(i) + ":\tmin_value " + str(min_value) + ", max_value " + str(max_value) + 
  #       ", sum_options " + str(sum_options) + ", avg_options " + str(avg_options) +
  #       ", sum_min " + str(sum_min) + ", sum_max " + str(sum_max))

print("\nMinimum number of questions for ranking " + str(n) + " things is " + str(sum_min))
print("Average number of questions for ranking " + str(n) + " things is " + str(round(sum_avg_options)))
print("Maximum number of questions for ranking " + str(n) + " things is " + str(sum_max))