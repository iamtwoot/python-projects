import tkinter as tk

def km_to_miles():
    miles = float(km_input.get()) * 0.62
    miles_result_label.config(text=f"{miles}")

window = tk.Tk()
window.title("Km to Mile Converter")
window.config(padx=20, pady=20)

# Input (Row 0)
km_input = tk.Entry(width=10)
km_input.grid(column=1, row=0)

km_label = tk.Label(text="Km")
km_label.grid(column=2, row=0)

# Answer (Row 1)
equal_label = tk.Label(text="equals to")
equal_label.config(padx=5, pady=5)
equal_label.grid(column=0, row=1)

miles_result_label = tk.Label(text="0")
miles_result_label.config(padx=5, pady=5)
miles_result_label.grid(column=1, row=1)

miles_label = tk.Label(text="Miles")
miles_label.config(padx=5, pady=5)
miles_label.grid(column=2, row=1)

# Button (Row 2)
calc_button = tk.Button(text="Calculate", command=km_to_miles)
calc_button.grid(column=1, row=2)


window.mainloop()