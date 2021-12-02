import pandas as pd


def read_heights():
    with open("data/input.txt") as f:
        heights = [int(height.strip()) for height in f.readlines()]

    return heights


def count_deeper_measurements(heights, start_index=0):
    count = 0
    for index in range(start_index, len(heights)):
        if index != 0:
            if heights[index] > heights[index - 1]:
                count += 1
    return count


def create_rolling_window_data(heights):
    heights_df = pd.DataFrame({'measurements': heights})
    return list(heights_df['measurements'].rolling(3).sum())


if __name__ == "__main__":
    heights = read_heights()
    print(f"Deeper measurements {count_deeper_measurements(heights)}")

    rolling_windows_heights = create_rolling_window_data(heights)
    print(f"rolling window Deeper measurements",
          f"{count_deeper_measurements(rolling_windows_heights, start_index=2)}")

