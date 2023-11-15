import pandas as pd
import matplotlib.pyplot as plt

file_path = "data/mtfuji_data.csv"
df = pd.read_csv(file_path)

plt.figure(figsize=(10, 6))
plt.plot(df["x"], df["elevation"], linestyle='-')
plt.title("Mt. Fuji")
plt.xlabel("Position")
plt.ylabel("Elevation [m]")
plt.grid(True)
plt.show()

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

def calculate_destination_point(current_point, gradient, alpha=0.2):
    try:
        destination_point = round(current_point - alpha * gradient)

        if destination_point < 0:
            raise ValueError("Destination point cannot be negative.")

        return destination_point
    except Exception as e:
        print(f"Error: {e}")
        return None

def descend_mt_fuji(start_point):
    descended_points = [start_point]

    while True:
        current_point = descended_points[-1]
        current_gradient = calculate_gradient(df, current_point)

        if current_gradient is not None:
            destination_point = calculate_destination_point(current_point, current_gradient)

            if destination_point in descended_points:
                print("Reached a flat area. Stopping descent.")
                break

            descended_points.append(destination_point)
        else:
            print("Unable to calculate gradient. Stopping descent.")
            break

    return descended_points

# Example usage:
start_point = 136  # Replace with the desired start point
descended_points = descend_mt_fuji(start_point)
print(f"Recorded Points: {descended_points}")
