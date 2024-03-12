from tkinter import Label, Button, Entry, Tk


def calculate():
    miles_result = miles_input.get()
    miles_int = float(miles_result)
    km_int = miles_int * 1.60934
    return km_result_label.config(text=f"{km_int}")


window = Tk()
window.title("Mile to Kilometer")
window.config(height=200, width=280)
window.config(padx=35, pady=35)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

miles_input = Entry(width=8, justify='center')
miles_input.grid(column=1, row=0)
miles_input.get()


calculate_button = Button(text="Calculate", width=7, command=calculate)
calculate_button.grid(column=1, row=2)

























window.mainloop()


