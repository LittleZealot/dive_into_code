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

current_point = 136
current_gradient = calculate_gradient(df, current_point)
destination_point = calculate_destination_point(current_point, current_gradient)

if destination_point is not None:
    print(f"Destination point: {destination_point}")
else:
    print("Unable to calculate destination point.")
