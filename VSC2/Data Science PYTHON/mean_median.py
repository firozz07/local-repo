import statistics as stats
data = [10, 20, 20, 30, 40, 50, 60, 70]
mean = stats.mean(data)
median = stats.median(data)
mode = stats.mode(data)
variance = stats.variance(data)
std_dev = stats.stdev(data)
data_range = max(data) - min(data)
sorted_data = sorted(data)
n = len(sorted_data)
lower_half = sorted_data[:n//2]
upper_half = sorted_data[n//2:]
q1 = stats.median(lower_half)
q3 = stats.median(upper_half)
iqr = q3 - q1
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
print("Range:", data_range)
print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)