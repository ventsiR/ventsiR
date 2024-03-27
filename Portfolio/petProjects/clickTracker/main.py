import time
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

class ClickTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Click Tracker")
        self.root.geometry("850x500")

        self.syllable_times = []
        self.new_line_times = [0]

        self.label = tk.Label(root, text="Left click for syllables, right click for new line")
        self.label.pack(pady=10)

        self.button = tk.Button(root, height = 10, width = 100, text="Syllable   /   New Line")
        self.button.pack(pady=5)
        self.button.bind("<Button-1>", self.record_left_click)  # Left click
        self.button.bind("<Button-3>", self.record_right_click)  # Right click

        self.display_button = tk.Button(root, height = 10, width = 100, text="End", command=self.display_intervals)
        self.display_button.pack(pady=5)

    def record_left_click(self, event):
        self.syllable_times.append(time.time())

    def record_right_click(self, event):
        self.new_line_times.append(time.time())

    def raw_data_to_lines(self):
        output = []
        self.new_line_times[0] = min(self.syllable_times) - 0.3
        if max(self.new_line_times) < max(self.syllable_times):
            self.new_line_times.append(max(self.syllable_times) + 0.3)
        syllable_times = self.syllable_times
        max_line_index = len(self.new_line_times) - 1
        for index, line_start_time in enumerate(self.new_line_times):
            if index == max_line_index:
                break
            counter = 0
            line_end_time = self.new_line_times[index + 1]
            line = []
            for syllable_time in syllable_times:
                if syllable_time > line_end_time:
                    syllable_times = syllable_times[counter:]
                    break
                counter += 1
                line.append(syllable_time - line_start_time)
            output.append(line)
        return output

    def display_intervals(self):
        # Create values to plot
        lines = self.raw_data_to_lines()
        x = [point for line in lines for point in line]
        num_of_points = len(x)
        y = [0] * num_of_points
        first_point = 0
        counter = 0
        for line in lines:
            counter += 1
            line_len = len(line)
            y[first_point : first_point + line_len] = [counter] * line_len
            first_point += line_len
        y = y[::-1]

        # Plot values
        plt.scatter(x,y)

        plt.xlabel('Time')
        plt.ylabel('Values')
        plt.title('Spread')
        plt.grid(True)
        plt.show()



       
        # messagebox.showinfo("Intervals", str(self.syllable_times) + '\n\n\n\n' + str(self.new_line_times))
        # messagebox.showinfo("Intervals", str(x) + '\n\n\n\n' + str(y))
        # messagebox.showinfo("Intervals", str([str(line) for line in lines]))
        self.syllable_times = []
        self.new_line_times = [0]


if __name__ == "__main__":
    root = tk.Tk()
    app = ClickTracker(root)
    root.mainloop()
