import tkinter as tk

window = tk.Tk()
window.title("GUI Elements")

label = tk.Label(
    text="Label 1"
)

label_2 = tk.Label(
    text="label 2",
    font=("Arial", 16),
    background="red",
    foreground="white"
)
# bg = background, fg = foreground

label_3 = tk.Label(
    text="Label 3",
    font=("Arial", 16),
    bg="yellow",
    height=5,
    width=10
)

button = tk.Button(
    text="Button!",
    height=2,
    width=7
)

entry = tk.Entry(
    width=15
)

text_box = tk.Text(

)

label.pack()
label_2.pack()
label_3.pack()
button.pack()
entry.pack()
text_box.pack()

window.mainloop()

