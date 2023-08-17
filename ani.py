import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def generate_normal_distribution(mean, std, n_samples):
  """Generates a normal distribution with the given mean, standard deviation, and number of samples."""
  data = np.random.normal(mean, std, n_samples)
  return data

def plot_histogram(data):
  """Plots the histogram of the given data."""
  fig, ax = plt.subplots()
  ax.hist(data)
  plt.xlabel("Value")
  plt.ylabel("Frequency")
  plt.title("Histogram of the Normal Distribution")

def download_data(data):
  """Downloads the given data as a .csv file."""
  csv_file = "normal_distribution.csv"
  with open(csv_file, "w") as f:
    f.write("value,frequency\n")
    for value, frequency in enumerate(data):
      f.write(f"{value},{frequency}\n")

st.title("Generate Normal Distribution")

# Get the mean, standard deviation, and number of samples from the user.
mean = st.number_input("Mean", value=0)
std = st.number_input("Standard deviation", value=1)
n_samples = st.number_input("Number of samples", value=100)

# Generate the normal distribution data.
data = generate_normal_distribution(mean, std, n_samples)

# Plot the histogram of the data.
if st.checkbox("Plot histogram"):
  plot_histogram(data)

# Download the data as a .csv file.
if st.checkbox("Download data"):
  download_data(data)
