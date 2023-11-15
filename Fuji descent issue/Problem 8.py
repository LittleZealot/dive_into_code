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

        if delta_points != 0:
            gradient = delta_elevation / delta_points
            return gradient
        else:
            print("Delta points is zero. Unable to calculate gradient.")
            return None
    else:
        print("Invalid current point. Please provide a valid point.")
        return None

# Function to calculate the destination point
def calculate_destination_point(current_point, gradient, alpha=0.2):
    destination_point = round(current_point - alpha * gradient)
    if destination_point < 0:
        raise ValueError("Destination point cannot be negative.")
    return destination_point


# Function to descend the mountain for a given alpha
def descend_mountain_with_alpha(start_point, df, alpha):
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


# Function to visualize the descent process for different alphas
def visualize_descent_for_alphas(df, initial_points, alphas):
    plt.figure(figsize=(12, 8))
    plt.plot(df["x"], df["elevation"], label="Mt. Fuji Elevation", linestyle='-', color='blue')

    for alpha in alphas:
        for starting_point in initial_points:
            descended_points = descend_mountain_with_alpha(starting_point, df, alpha)
            valid_points = [point for point in descended_points if point in df.index]
            plt.scatter(valid_points, df.loc[valid_points, "elevation"], label=f"Alpha={alpha}", marker='o')

    plt.title("Mt. Fuji Descent Process for Different Alphas")
    plt.xlabel("Position")
    plt.ylabel("Elevation [m]")
    plt.legend()
    plt.grid(True)
    plt.show()


# Set initial points and alpha values
initial_points = [136, 142, 150]
alpha_values = [0.01, 0.1, 0.5]

# Visualize the descent process for different alphas
visualize_descent_for_alphas(df, initial_points, alpha_values)
