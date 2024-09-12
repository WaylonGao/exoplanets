import numpy as np
import csv
from datetime import datetime, timedelta

# Parameters
num_points = 1000  # Number of data points
noise_level = 0.1  # Noise level

# Generate time data
start_time = datetime.now()
time = [start_time + timedelta(seconds=i) for i in range(num_points)]

# Generate transit signal (simple dip in the middle)
transit_signal = np.ones(num_points)
transit_signal[450:550] = 0.8  # Simulate a transit dip

# Add random noise
noise = np.random.normal(0, noise_level, num_points)
noisy_data = transit_signal + noise

# Write to CSV
with open('noisy_data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Timestamp', 'Flux'])
    for t, flux in zip(time, noisy_data):
        csvwriter.writerow([t.strftime('%Y-%m-%d %H:%M:%S'), flux])

print("Data has been written to noisy_data.csv")
