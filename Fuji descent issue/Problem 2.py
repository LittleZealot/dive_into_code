import pandas as pd

file_path = "data/mtfuji_data.csv"
data = pd.read_csv(file_path)
def calculate_gradient(data, point_number):

    current_point = data[data['x'] == point_number]
    previous_point_number = point_number - 1
    previous_point = data[data['x'] == previous_point_number]
    if previous_point.empty:
        print(f"Error: Point {previous_point_number} not found in the dataset.")
        return None
    delta_elevation = current_point['elevation'].values[0] - previous_point['elevation'].values[0]
    delta_point_number = current_point['x'].values[0] - previous_point_number
    gradient = delta_elevation / delta_point_number

    return gradient

point_number = 136
gradient_at_point_5 = calculate_gradient(data, point_number)
print(f"Gradient at point {point_number}: {gradient_at_point_5}")
