"""Tkinter GUI for user's habits."""

from tkinter import Frame, Label, Button, Entry


class MyHabits(Frame):
    """Tkinter frame for displaying user's habits."""

    def __init__(self, master):
        """Initialize the MyHabits frame."""
        super().__init__(master)
        self.master = master
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.mount_habit_creator()
        self.mount_habit_list()

    def mount_habit_creator(self):
        """Mount the habit creator frame."""
        habit_creator_frame = Frame(self, bg="#93CE82")
        habit_creator_frame.grid(row=0, column=0, sticky='nswe',
                                 pady=20, padx=20)
        habit_creator_frame.grid_columnconfigure(0, weight=1)

        # Create and add widgets to the habit creator frame
        label = Label(habit_creator_frame, text="Habit Creator",
                      font=("Helvetica", 20), bg="#93CE82", fg="black")
        label.grid(row=1, column=0, sticky='nsew', padx=10, pady=20)
        label.grid_columnconfigure(0, weight=1)

        user_entry = Entry(habit_creator_frame, width=30)
        user_entry.insert(0, "Enter a new habit")
        user_entry.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)
        user_entry.grid_columnconfigure(0, weight=1)

        create_button = Button(
            habit_creator_frame,
            text="Create",
            bg="white",
            width=15,
            borderwidth=1,
            height=2,
            cursor="hand2",
            command=lambda: self.create_habit(user_entry.get()),
        )
        create_button.grid(row=3, column=0, sticky='ew', padx=10, pady=10)
        create_button.grid_columnconfigure(0, weight=1)

    def mount_habit_list(self):
        """Mount the habit list frame."""
        self.habit_list_frame = Frame(self, bg="#D9EAD3")
        self.habit_list_frame.grid(row=1, column=0, sticky='nswe',
                                   pady=20, padx=20)
        self.habit_list_frame.grid_columnconfigure(0, weight=1)

        label = Label(self.habit_list_frame, text="Habit List",
                      font=("Helvetica", 20), bg="#D9EAD3", fg="black")
        label.grid(row=0, column=0, sticky='nsew', padx=10, pady=20)
        label.grid_columnconfigure(0, weight=1)

        self.empty_list_label = Label(self.habit_list_frame,
                                      text="You don't have any habit yet.",
                                      font=("Helvetica", 14), bg="#D9EAD3",
                                      fg="black")
        self.empty_list_label.grid(row=1, column=0, sticky='nsew',
                                   padx=30, pady=30)
        self.empty_list_label.grid_columnconfigure(0, weight=1)

    def create_habit(self, habit_description):
        """Create a new habit item."""
        try:
            # Attempt to create a new habit item label
            if self.habit_list_frame:
                if self.empty_list_label:
                    self.empty_list_label.grid_remove()

                habit_item = Frame(self.habit_list_frame, bg="#D9EAD3")
                habit_item.grid(row=self.habit_list_frame.grid_size()[1],
                                column=0, sticky='nsew', padx=10, pady=10)
                habit_item.grid_columnconfigure(0, weight=1)

                habit_item_label = Label(habit_item,
                                         text=f"{habit_description}",
                                         font=("Helvetica", 14), bg="#8789C0",
                                         anchor="w", padx=10, pady=10)
                habit_item_label.grid(row=0, column=0, sticky='nsew',
                                      padx=10, pady=10)
                habit_item_label.grid_columnconfigure(0, weight=1)

                # Create edit button
                edit_button = Button(habit_item, text="Edit",
                                     command=lambda:
                                     self.edit_habit(habit_item))
                edit_button.grid(row=0, column=1, sticky='nsew',
                                 padx=5, pady=5)

                # Create delete button
                delete_button = Button(habit_item, text="Delete",
                                       command=lambda:
                                       self.delete_habit(habit_item))
                delete_button.grid(row=0, column=2, sticky='nsew',
                                   padx=5, pady=5)

            else:
                print("Error creating new habit: " +
                      "habit_list_frame is not initialized")
        except Exception as e:
            print(f"An error occurred while creating a new habit: {e}")

    def delete_habit(self, habit_item):
        """Delete a habit item."""
        habit_item.destroy()

    def edit_habit(self, habit_item):
        """Edit a habit item."""
        pass
