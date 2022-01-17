import tkinter as tk
from tkinter import Entry

import tkinter_helper as tkh


def save_movie(*args):
    title = ent_movie_title.get()
    year = int(ent_movie_year.get())
    duration = int(ent_movie_duration.get())

    key = f"({year}) {title}"
    movies[key] = {'title': title, 'year': year, 'duration': duration}
    listbox_movies.insert(tk.END, key)


def item_selected(*args):
    movie_key = listbox_movies.get(listbox_movies.curselection())
    movie = movies[movie_key]

    ent_movie_title.delete(0, tk.END)
    ent_movie_title.insert(0, movie['title'])


movies = {'(2020) Soul': {'title': 'Soul', 'year': 2020, 'duration': 100},
          '(2021) Dune': {'title': 'Dune', 'year': 2021, 'duration': 156},
          }

window = tk.Tk()
tkh.create_big_ui(20)

# Create list frame
list_frame = tk.Frame()

movie_list = tk.StringVar(value=list(movies))
listbox_movies = tk.Listbox(list_frame, listvariable=movie_list)
listbox_movies.bind('<<ListboxSelect>>', item_selected)

listbox_movies.pack()
list_frame.pack(side=tk.LEFT)

# Create main frame
main_frame = tk.Frame()
# Create form labels
lbl_movie_title = tk.Label(main_frame, text="Title:")
lbl_movie_year = tk.Label(main_frame, text="Year:")
lbl_movie_duration = tk.Label(main_frame, text="Duration:")
# Create form entry-boxes
ent_movie_title: Entry = tk.Entry(main_frame)
ent_movie_year = tk.Entry(main_frame)
ent_movie_duration = tk.Entry(main_frame)
# Create save button
btn_save = tk.Button(main_frame, text="Save", command=save_movie)
# Put the form widget in a "nice" grid
lbl_movie_title.grid(row=0, column=0)
lbl_movie_year.grid(row=1, column=0)
lbl_movie_duration.grid(row=2, column=0)
ent_movie_title.grid(row=0, column=1)
ent_movie_year.grid(row=1, column=1)
ent_movie_duration.grid(row=2, column=1)
btn_save.grid(row=3, column=0, columnspan=2)

main_frame.pack(padx=20, pady=20)

window.mainloop()
