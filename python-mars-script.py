import time

# Code that assumes the input metric values are already in the correct format
def no_need_to_convert_metric(value):
  return value / 1000

# Code that checks the input metric format and converts if necessary
def convert_metric2(value, unit):
    if unit.lower() == "meters":
        return value / 1000
    elif unit.lower() == "kilometers":
        return value * 1000
    elif unit.lower() == "feet":
        return value / 3280.84
    elif unit.lower() == "miles":
        return value * 1.60934
    else:
        raise ValueError("Invalid unit: {}".format(unit))

# Measure the execution time of Code 1
total_time1 = 0
for i in range(10):
    start_time = time.perf_counter()
    for j in range(100000):
        no_need_to_convert_metric(1000)
    end_time = time.perf_counter()
    time1 = end_time - start_time
    total_time1 += time1

# Measure the execution time of Code 2
total_time2 = 0
for i in range(10):
    start_time = time.perf_counter()
    for j in range(100000):
        convert_metric2(1000, "meters")
    end_time = time.perf_counter()
    time2 = end_time - start_time
    total_time2 += time2

# Calculate the average execution time for each code
avg_time1 = total_time1 / 10
avg_time2 = total_time2 / 10

# Calculate the percentage difference between the execution times
percentage_diff = abs((avg_time1 - avg_time2) / avg_time1) * 100

# Determine which code is faster based on the percentage difference
if avg_time1 < avg_time2:
    message = "Code 1 is faster than Code 2"
elif avg_time2 < avg_time1:
    message = "Code 2 is faster than Code 1"
else:
    message = "Both codes have the same execution time"

# Print the results
print("Code 1 average execution time: {:.6f} seconds".format(avg_time1))
print("Code 2 average execution time: {:.6f} seconds".format(avg_time2))
print("{} by {:.2f}%".format(message, percentage_diff))