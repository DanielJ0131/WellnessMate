"""Tkinter GUI for user's habits."""

from tkinter import Frame, Label, Button, Entry, Canvas, Scrollbar
from tkmacosx import Button



class MyHabits(Frame):
    """Tkinter frame for displaying user's habits."""

    def __init__(self, master, db, user_id, username):
        """Initialize the MyHabits frame."""
        super().__init__(master, bg="#F3F1E7", padx=70, pady=60)
        self.master = master
        self.db = db
        self.user_id = user_id
        self.username = username
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        welcome_label = Label(
            self,
            text="Welcome, " + f"{self.username.capitalize()}" + "!",
            font=("Helvetica", 32),
            bg="#F3F1EB",
            fg="#2A2A28",
        )
        welcome_label.grid(row=0, column=0, sticky="w", padx=10, pady=30)

        self.mount_habit_creator()
        self.mount_habit_list()

    def mount_habit_creator(self):
        habit_creator_frame = Frame(self, bg="#D8B7E3", pady=25, padx=25)
        habit_creator_frame.grid(row=1, column=0, sticky="nsew")
        habit_creator_frame.grid_columnconfigure(0, weight=1)

        label = Label(
            habit_creator_frame,
            text="Habit Creator",
            font=("Helvetica", 20),
            bg="#D8B7E3",
            fg="#2A2A28",
        )
        label.grid(row=0, column=0, sticky="w", pady=(0, 10))

        user_entry = Entry(
            habit_creator_frame,
            width=30,
            font=("Helvetica", 16),
            fg="#2A2A28",
            bg="#FFFFFF",
            relief="solid",
            highlightthickness=5,
            highlightbackground="#FFFFFF",
            borderwidth=0,
            insertbackground="#4C4A46",
        )
        user_entry.grid(row=1, column=0, sticky="ew")
        user_entry.focus_set()

        self.create_habit_button = Button(
            habit_creator_frame,
            text="Create habit",
            font=("Helvetica", 16, "bold"),
            fg="#2A2A28",
            bg="#45B9AC",
            highlightbackground="#D8B7E4",
            relief="solid",
            highlightthickness=0,
            borderwidth=0,
            padx=20,
            pady=10,
            cursor="hand2",
            command=lambda: self.create_habit(user_entry.get()),
        )
        self.create_habit_button.grid(row=2, column=0, sticky="w", pady=20)

    def mount_habit_list(self):
        # Get habits from database
        habit_list = self.db.get_habits(self.user_id)

        self.habit_list_frame = Frame(self, bg="#D7D97D", pady=25, padx=25)
        self.habit_list_frame.grid(row=2, column=0, sticky="nsew", pady=(30, 0))
        self.habit_list_frame.grid_columnconfigure(0, weight=1)
        self.habit_list_frame.grid_rowconfigure(1, weight=1)

        label = Label(
            self.habit_list_frame,
            text="My Habit List",
            font=("Helvetica", 20),
            bg="#D7D97D",
            fg="#2A2A28",
        )
        label.grid(row=0, column=0, sticky="w", pady=(0, 10))

        # Canvas to contain the habit items and attach scrollbar to it
        self.canvas = Canvas(self.habit_list_frame, bg="#D7D97D", highlightthickness=0)
        self.canvas.grid(row=1, column=0, sticky="nsew", padx=(0, 20))
        self.canvas.grid_columnconfigure(0, weight=1)

        self.scrollbar = Scrollbar(self.habit_list_frame, orient="vertical", command=self.canvas.yview, background="#D7D97D", troughcolor="#F3F1E7")
        self.scrollbar.config(bg="#D7D97D")
        self.scrollbar.grid(row=1, column=1, sticky="ns", pady=10) 
        
        self.habit_inner_frame = Frame(self.canvas, bg="#D7D97D", pady=10)
        self.habit_inner_frame.grid_columnconfigure(0,weight=1)

        self.canvas_frame = self.canvas.create_window((0, 0), window=self.habit_inner_frame, anchor="nw")
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.habit_inner_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind('<Configure>', lambda e: self.canvas.itemconfig(self.canvas_frame, width=self.canvas.winfo_width()))   

        #self.canvas.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))

        if habit_list == ():
            self.mount_empty_list_frame()
        else:
            for habit in habit_list:
                self.mount_habit_item(habit[0])

    def mount_empty_list_frame(self):
        self.empty_list_label = Label(
            self.habit_inner_frame,
            text="You don't have any habit yet.",
            font=("Helvetica", 14),
            bg="#D7D97D",
            fg="#2A2A28",
        )
        self.empty_list_label.grid(row=1, column=0,
                                   sticky="nsew", padx=30, pady=30)
        self.empty_list_label.grid_columnconfigure(0, weight=1)

    def mount_habit_item(self, habit_description):
        try:
            habit_item = Frame(self.habit_inner_frame,
                               bg="#F3F1E7", padx=7, pady=7)
            habit_item.grid(
                row=self.habit_inner_frame.grid_size()[1],
                column=0,
                sticky="nsew",
                pady=10
            )
            habit_item.grid_columnconfigure(0, weight=1)

            habit_item_label = Label(
                habit_item,
                text=f"{habit_description}",
                font=("Helvetica", 16),
                fg="#2A2A28",
                bg="#F3F1E7",
                anchor="w",
            )
            habit_item_label.grid(row=0, column=0,
                                  sticky="nsew", padx=10, pady=10)

            edit_button = Button(
                habit_item,
                text="Edit",
                font=("Helvetica", 14, "bold"),
                fg="#2A2A28",
                bg="#CDCBC1",
                highlightbackground="#F3F1E6",
                relief="solid",
                highlightthickness=0,
                pady=5,
                borderwidth=0,
                cursor="hand2",
                command=lambda: self.edit_habit(habit_item),
            )
            edit_button.grid(row=0, column=1, sticky="ew", padx=10)

            delete_button = Button(
                habit_item,
                text="Delete",
                font=("Helvetica", 14, "bold"),
                fg="#2A2A28",
                bg="#45B9AC",
                highlightbackground="#F3F1E6",
                relief="solid",
                highlightthickness=0,
                pady=5,
                borderwidth=0,
                cursor="hand2",
                command=lambda: self.delete_habit(habit_item,
                                                  habit_description),
            )
            delete_button.grid(row=0, column=2, sticky="ew", padx=10)
        except Exception as e:
            print(f"An error occurred while creating a new habit: {e}")

    def create_habit(self, habit_description):
        # Check if empty_list_frame exists and remove it if it does
        if hasattr(self, "empty_list_label"):
            self.empty_list_label.grid_forget()
            del self.empty_list_label
        self.mount_habit_item(habit_description)
        self.db.add_habit(habit_description, self.user_id)

    def delete_habit(self, habit_item, habit_description):
        self.db.delete_habit(habit_description)
        habit_item.destroy()
        if self.habit_inner_frame.grid_size()[1] == 1:
            self.mount_empty_list_frame()

    def edit_habit(self, habit_item):
        current_description = habit_item.grid_slaves(row=0, column=0)[0].cget("text")
    
        entry_widget = Entry(
            habit_item,
            font=("Helvetica", 16),
            fg="#2A2A28",
            bg="#FFFFFF",
            relief="solid",
            highlightthickness=5,
            highlightbackground="#FFFFFF",
            borderwidth=0,
            insertbackground="#4C4A46",
        )
        entry_widget.insert(0, current_description)
        entry_widget.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        entry_widget.focus_set()
        entry_widget.bind("<Return>", lambda event: self.save_habit_edit(habit_item, entry_widget, current_description))

    def save_habit_edit(self, habit_item, entry_widget, current_description):
        new_description = entry_widget.get()
        self.db.edit_habit(current_description, new_description)
        # Update the label text with the new description not working
        entry_widget.destroy()
        habit_item.grid_slaves(row=0, column=0)[0].config(text=new_description)
        print(habit_item.grid_slaves(row=0, column=0)[0].config(text=new_description))
