import numpy as np
import pandas as pd
data = [10, 20, 30, 40, 50]
def range_ungrouped(data):
    data = np.array(data)
    return np.max(data) - np.min(data)

def variance_sd_ungrouped(data):
    data = np.array(data)
    mean = np.mean(data)
    variance = np.mean((data - mean) ** 2)
    sd = np.sqrt(variance)
    return mean, variance, sd

def cv_ungrouped(data):
    data = np.array(data)
    mean = np.mean(data)
    sd = np.std(data)
    return (sd / mean) * 100

df = pd.DataFrame({
"class_interval": ["0-10", "10-20", "20-30"],
"frequency": [5, 8, 7]})

def compute_midpoints(df):
    midpoints = []
    for interval in df["class_interval"]:
        lower, upper = interval.split("-")
        midpoints.append((float(lower) + float(upper)) / 2)
        df["midpoint"] = midpoints
    return df

def range_grouped(df):
    first_lower = float(df["class_interval"].iloc[0].split("-")[0])
    last_upper = float(df["class_interval"].iloc[-1].split("-")[1])
    return last_upper - first_lower

def variance_sd_grouped(df):
    df = compute_midpoints(df)
    f = df["frequency"].values
    x = df["midpoint"].values
    mean = np.sum(f * x) / np.sum(f)
    variance = np.sum(f * (x - mean) ** 2) / np.sum(f)
    sd = np.sqrt(variance)
    return mean, variance, sd

def cv_grouped(df):
    mean, var, sd = variance_sd_grouped(df)
    return (sd / mean) * 100
data = [12, 15, 20, 25, 30, 35]
print("Range:", range_ungrouped(data))
mean, var, sd = variance_sd_ungrouped(data)
print("Mean:", mean)
print("Variance:", var)
print("Standard Deviation:", sd)
print("CV:", cv_ungrouped(data))

