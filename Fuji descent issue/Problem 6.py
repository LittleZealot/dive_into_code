import pandas as pd
import matplotlib.pyplot as plt

file_path = "data/mtfuji_data.csv"
df = pd.read_csv(file_path)

def calculate_gradient(df, current_point):
    if current_point >= 1 and current_point < len(df):
        elevation_current = df.loc[current_point, "elevation"]
        elevation_previous = df.loc[current_point - 1, "elevation"]
        delta_points = df.loc[current_point, "x"] - df.loc[current_point - 1, "x"]
        delta_elevation = elevation_current - elevation_previous
        gradient = delta_elevation / delta_points
        return gradient
    else:
        print("Invalid current point. Please provide a valid point.")

current_point = 137
resulting_gradient = calculate_gradient(df, current_point)
print(f"Gradient at point {current_point}: {resulting_gradient}")

def calculate_destination_point(current_point, gradient, alpha=0.2):
    try:
        destination_point = round(current_point - alpha * gradient)
        if destination_point < 0:
            raise ValueError("Destination point cannot be negative.")
        return destination_point
    except Exception as e:
        print(f"Error: {e}")
        return None

current_point = 137
current_gradient = calculate_gradient(df, current_point)
destination_point = calculate_destination_point(current_point, current_gradient)

if destination_point is not None:
    print(f"Destination point: {destination_point}")
else:
    print("Unable to calculate destination point.")

def descend_mountain(start_point, df):
    points_list = [start_point]

    while True:
        current_gradient = calculate_gradient(df, start_point)

        if current_gradient is None:
            print("Unable to calculate gradient. Stopping descent.")
            break

        destination_point = calculate_destination_point(start_point, current_gradient)

        if destination_point == start_point:
            print("Reached a flat area. Stopping descent.")
            break

        start_point = destination_point
        points_list.append(start_point)

    return points_list

# Example usage:
starting_point = 137  # Starting point near the summit
descended_points = descend_mountain(starting_point, df)
print("Recorded Points:", descended_points)

# Visualize the descent process
plt.figure(figsize=(10, 6))
plt.plot(df["x"], df["elevation"], label="Mt. Fuji Elevation", linestyle='-', color='blue')
plt.scatter(descended_points, df.loc[descended_points, "elevation"], color='red', label="Descent Points", marker='o')
plt.title("Mt. Fuji")
plt.xlabel("Position")
plt.ylabel("Elevation [m]")
plt.legend()
plt.grid(True)
plt.show()
