import pandas as pd
import matplotlib.pyplot as plt

file_path = "data/mtfuji_data.csv"
df = pd.read_csv(file_path)

# Function to calculate the gradient at a certain point
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

# Function to calculate the destination point
def calculate_destination_point(current_point, gradient, alpha=0.2):
    destination_point = round(current_point - alpha * gradient)
    if destination_point < 0:
        raise ValueError("Destination point cannot be negative.")
    return destination_point

# Function to descend the mountain starting from a given point and record each move
def descend_mountain(start_point, df, alpha=0.2):
    points_list = [start_point]

    while True:
        current_gradient = calculate_gradient(df, start_point)

        if current_gradient is None:
            print("Unable to calculate gradient. Stopping descent.")
            break

        destination_point = calculate_destination_point(start_point, current_gradient, alpha)

        if destination_point == start_point:
            print("Reached a flat area. Stopping descent.")
            break

        start_point = destination_point
        points_list.append(start_point)

    return points_list

# Function to visualize the descent process for each initial value
def visualize_descent_for_initial_values(df, initial_values, alpha=0.2):
    plt.figure(figsize=(12, 8))
    plt.plot(df["x"], df["elevation"], label="Mt. Fuji Elevation", linestyle='-', color='blue')

    for starting_point in initial_values:
        descended_points = descend_mountain(starting_point, df, alpha)
        valid_points = [point for point in descended_points if point in df.index]
        plt.scatter(valid_points, df.loc[valid_points, "elevation"], label=f"137={starting_point}", marker='o')

    plt.title("Mt. Fuji Descent Process for Different Initial Values")
    plt.xlabel("Position")
    plt.ylabel("Elevation [m]")
    plt.legend()
    plt.grid(True)
    plt.show()

# Set initial values
initial_values = [136, 142, 150]

# Visualize the descent process for each initial value
visualize_descent_for_initial_values(df, initial_values)
