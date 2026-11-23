parameters_billions = 3.0
bits_per_parameter = 4
raw_bytes = parameters_billions * 1_000_000_000 * bits_per_parameter / 8
print("Raw parameter size (GB):", round(raw_bytes / 1e9, 2))
print("Raw parameter size (GiB):", round(raw_bytes / (1024**3), 2))


