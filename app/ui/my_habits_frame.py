"""Tkinter GUI for user's habits."""

from tkinter import Frame, Label, Button, Entry


class MyHabits(Frame):
    """Tkinter frame for displaying user's habits."""

    def __init__(self, master, db, user_id, username):
        """Initialize the MyHabits frame."""
        super().__init__(master, bg="#F3F1EB", padx=50, pady=30)
        self.master = master
        self.db = db
        self.user_id = user_id
        self.username = username
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        welcome_label = Label(self, text="Welcome, " + f"{self.username}" + "!", font=("Helvetica", 32), bg="#F3F1EB", fg="#2A2A28")
        welcome_label.grid(row=0, column=0, sticky='w', padx=10, pady=30)

        self.mount_habit_creator()
        self.mount_habit_list()

    def mount_habit_creator(self):
        """Mount the habit creator frame."""
        habit_creator_frame = Frame(self, bg="#D8B7E3", pady=10, padx=50)
        habit_creator_frame.grid(row=1, column=0, sticky='nsew', pady=20, padx=20)
        habit_creator_frame.grid_columnconfigure(0, weight=1)

        label = Label(habit_creator_frame, text="Habit Creator", font=("Helvetica", 20), bg="#D8B7E3", fg="#2A2A28")
        label.grid(row=0, column=0, sticky='w', pady=20)

        user_entry = Entry(habit_creator_frame, width=30, font=("Helvetica", 16), fg="#2A2A28", bg="#FFFFFF", relief="solid", highlightthickness=5, highlightbackground="#FFFFFF", borderwidth=0, insertbackground='#4C4A46')
        user_entry.grid(row=1, column=0, sticky='ew')

        self.create_habit_button = Button(habit_creator_frame, text="Crete habit", font=("Helvetica", 16, "bold"), fg="#2A2A28", bg="#45B9AC", highlightbackground="#F3F1E7", relief="solid", highlightthickness=0, borderwidth=0, padx=20, pady=10, cursor="hand2", command=lambda: self.create_habit(user_entry.get()))
        self.create_habit_button.grid(row=3, column=0, sticky='w', pady=20)

    def mount_habit_list(self):
        """Mount the habit list frame."""
        # Get habits from database
        habit_list = self.db.get_habits(self.user_id)

        self.habit_list_frame = Frame(self, bg="#D7D97D", pady=20, padx=50)
        self.habit_list_frame.grid(row=2, column=0, sticky='nsew', pady=20, padx=20)
        self.habit_list_frame.grid_columnconfigure(0, weight=1)

        label = Label(self.habit_list_frame, text="My Habit List", font=("Helvetica", 20), bg="#D7D97D", fg="#2A2A28")
        label.grid(row=0, column=0, sticky='w', pady=20)

        if habit_list==():
            self.mount_empty_list_frame()
        else:
            for habit in habit_list:
                self.mount_habit_item(habit[0])
    
    def mount_empty_list_frame(self):
        self.empty_list_label = Label(self.habit_list_frame, text="You don't have any habit yet.", font=("Helvetica", 14), bg="#D7D97D", fg="#2A2A28")
        self.empty_list_label.grid(row=1, column=0, sticky='nsew', padx=30, pady=30)
        self.empty_list_label.grid_columnconfigure(0, weight=1)        

    def mount_habit_item(self, habit_description):
        """Create a new habit item."""
        try:
            habit_item = Frame(self.habit_list_frame, bg="#F3F1E7", padx=10, pady=10)
            habit_item.grid(row=self.habit_list_frame.grid_size()[1], column=0, sticky='nsew', pady=10)
            habit_item.grid_columnconfigure(0, weight=1)

            habit_item_label = Label(habit_item, text=f"{habit_description}", font=("Helvetica", 16), fg="#2A2A28", bg="#F3F1E7", anchor="w")
            habit_item_label.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

            edit_button = Button(habit_item, text="Edit", font=("Helvetica", 14, "bold"), fg="#2A2A28", bg="#CDCBC1", highlightbackground="#F3F1E7", relief="solid", highlightthickness=0, pady=5 ,borderwidth=0, cursor="hand2", command=lambda:self.edit_habit(habit_item))
            edit_button.grid(row=0, column=1, sticky='ew', padx=10)

            # Create delete button
            delete_button = Button(habit_item, text="Delete", font=("Helvetica", 14, "bold"), fg="#2A2A28", bg="#45B9AC", highlightbackground="#F3F1E7", relief="solid", highlightthickness=0, pady=5 ,borderwidth=0, cursor="hand2", command=lambda:self.delete_habit(habit_item, habit_description))
            delete_button.grid(row=0, column=2, sticky='ew', padx=10)
        except Exception as e:
            print(f"An error occurred while creating a new habit: {e}") 

    def create_habit(self, habit_description):
        # Check if empty_list_frame exists and remove it if it does
        if hasattr(self, 'empty_list_label'):
            self.empty_list_label.grid_forget()
            del self.empty_list_label
        self.mount_habit_item(habit_description)
        self.db.add_habit(habit_description, self.user_id)

    def delete_habit(self, habit_item, habit_description):
        """Delete a habit item."""
        self.db.delete_habit(habit_description)
        habit_item.destroy()
        if self.habit_list_frame.grid_size()[1] == 1:
            self.mount_empty_list_frame()


    def edit_habit(self, habit_item):
        """Edit a habit item."""
        pass
