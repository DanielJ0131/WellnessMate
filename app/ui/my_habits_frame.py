"""Tkinter GUI for user's habits."""

from tkinter import Frame, Label, Button, Entry, Canvas, Scrollbar
from tkmacosx import Button


class MyHabits(Frame):
    """Tkinter frame for displaying and managing the user's habits."""

    def __init__(self, master, db, user_id, username, fontsize):
        """
        Initialize the MyHabits frame.

        Parameters:
        - master: The root window or parent widget.
        - db: The database connection instance.
        - user_id: The ID of the current user.
        - username: The username of the current user.
        - fontsize: A dictionary containing font sizes.
        """
        super().__init__(master, bg="#F3F1E7", padx=70, pady=60)
        self.master = master
        self.db = db
        self.user_id = user_id
        self.username = username
        self.fontsize = fontsize
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        welcome_label = Label(
            self,
            text="Welcome, " + f"{self.username.capitalize()}" + "!",
            font=("Helvetica", self.fontsize["xl"], "bold"),
            bg="#F3F1EB",
            fg="#2A2A28",
        )
        welcome_label.grid(row=0, column=0, sticky="w", padx=10, pady=30)

        self.mount_habit_creator()
        self.mount_habit_list()

    def mount_habit_creator(self):
        """
        Mount the habit creator frame.

        This frame contains an entry for the habit title and a button
        to create a new habit.
        """
        habit_creator_frame = Frame(self, bg="#59B2A7", pady=15, padx=35)
        habit_creator_frame.grid(row=1, column=0, sticky="nsew")
        habit_creator_frame.grid_columnconfigure(0, weight=1)

        label = Label(
            habit_creator_frame,
            text="Create a new habit",
            font=("Helvetica", self.fontsize["m"], "bold"),
            bg="#59B2A7",
            fg="#2A2A28",
        )
        label.grid(row=0, column=0, sticky="w", pady=(0, 20))

        entry_label = Label(
            habit_creator_frame,
            text="Title",
            font=("Helvetica", self.fontsize["xxs"], "bold"),
            bg="#59B2A7",
            fg="#48463D",
        )
        entry_label.grid(row=1, column=0, sticky="w")

        user_entry = Entry(
            habit_creator_frame,
            width=30,
            font=("Helvetica", self.fontsize["xs"]),
            fg="#2A2A28",
            bg="#FFFFFF",
            relief="solid",
            highlightthickness=5,
            highlightbackground="#FFFFFF",
            borderwidth=0,
            insertbackground="#4C4A46",
        )
        user_entry.grid(row=2, column=0, sticky="ew")
        user_entry.focus_set()

        self.create_habit_button = Button(
            habit_creator_frame,
            text="Create habit",
            font=("Helvetica", self.fontsize["xs"], "bold"),
            fg="#2A2A28",
            bg="#D7D97D",
            highlightbackground="#59B2A9",
            relief="solid",
            highlightthickness=0,
            borderwidth=0,
            padx=20,
            pady=10,
            cursor="hand2",
            command=lambda: self.create_habit(user_entry.get()),
        )
        self.create_habit_button.grid(row=3, column=0, sticky="w", pady=20)

    def mount_habit_list(self):
        """
        Mount the habit list frame.

        This frame displays the list of habits fetched from the database.
        """
        habit_list = self.db.get_habits(self.user_id)

        self.habit_list_frame = Frame(self, bg="#D7D97D", pady=15, padx=35)
        self.habit_list_frame.grid(row=2, column=0, sticky="nsew",
                                   pady=(30, 0))
        self.habit_list_frame.grid_columnconfigure(0, weight=1)
        self.habit_list_frame.grid_rowconfigure(1, weight=1)
        label = Label(
            self.habit_list_frame,
            text="My Habit List",
            font=("Helvetica", self.fontsize["m"], "bold"),
            bg="#D7D97D",
            fg="#2A2A28",
        )
        label.grid(row=0, column=0, sticky="w", pady=(0, 10))

        # Canvas to contain the habit items and attach scrollbar to it
        self.canvas = Canvas(self.habit_list_frame, bg="#D7D97D",
                             highlightthickness=0)
        self.canvas.grid(row=1, column=0, sticky="nsew", padx=(0, 20))
        self.canvas.grid_columnconfigure(0, weight=1)
        self.scrollbar = Scrollbar(self.habit_list_frame, orient="vertical",
                                   command=self.canvas.yview,
                                   background="#D7D97D",
                                   troughcolor="#F3F1E7")
        self.scrollbar.config(bg="#D7D97D")
        self.scrollbar.grid(row=1, column=1, sticky="ns", pady=10)
        self.habit_inner_frame = Frame(self.canvas, bg="#D7D97D", pady=10)
        self.habit_inner_frame.grid_columnconfigure(0, weight=1)
        self.canvas_frame = self.canvas.create_window(
            (0, 0),
            window=self.habit_inner_frame,
            anchor="nw")
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.habit_inner_frame.bind("<Configure>", lambda e:
                                    self.canvas.configure
                                    (scrollregion=self.canvas.bbox("all")))
        self.canvas.bind('<Configure>', lambda e: self.canvas.itemconfig(
            self.canvas_frame, width=self.canvas.winfo_width()))

        if habit_list == ():
            self.mount_empty_list_frame()
        else:
            for habit in habit_list:
                self.mount_habit_item(habit[0])

    def mount_empty_list_frame(self):
        """
        Mount the frame for an empty habit list.

        Displays a message indicating that no habits are currently present.
        """
        self.empty_list_label = Label(
            self.habit_inner_frame,
            text="You don't have any habit yet.",
            font=("Helvetica", self.fontsize["xs"], "bold"),
            bg="#D7D97D",
            fg="#2A2A28",
        )
        self.empty_list_label.grid(row=1, column=0,
                                   sticky="nsew", padx=30, pady=30)
        self.empty_list_label.grid_columnconfigure(0, weight=1)

    def mount_habit_item(self, habit_description):
        """
        Mount a single habit item in the habit list.

        Parameters:
        - habit_description: The description of the habit to display.
        """
        try:
            habit_item = Frame(self.habit_inner_frame,
                               bg="#F3F1E7", padx=7, pady=1)
            habit_item.grid(
                row=self.habit_inner_frame.grid_size()[1],
                column=0,
                sticky="nsew",
                pady=7
            )
            habit_item.grid_columnconfigure(0, weight=1)

            habit_item_label = Label(
                habit_item,
                text=f"{habit_description}",
                font=("Helvetica", self.fontsize["xs"]),
                fg="#2A2A28",
                bg="#F3F1E7",
                anchor="w",
            )
            habit_item_label.grid(row=0, column=0,
                                  sticky="nsew", padx=10, pady=10)

            edit_button = Button(
                habit_item,
                text="Edit",
                font=("Helvetica", self.fontsize["xxs"]),
                fg="#2A2A28",
                bg="#CDCBC1",
                highlightbackground="#F3F1E6",
                relief="solid",
                highlightthickness=0,
                pady=2,
                borderwidth=0,
                cursor="hand2",
                command=lambda: self.edit_habit(habit_item),
            )
            edit_button.grid(row=0, column=1, sticky="ew", padx=10)

            delete_button = Button(
                habit_item,
                text="Delete",
                font=("Helvetica", self.fontsize["xxs"]),
                fg="#2A2A28",
                bg="#45B9AC",
                highlightbackground="#F3F1E6",
                relief="solid",
                highlightthickness=0,
                pady=2,
                borderwidth=0,
                cursor="hand2",
                command=lambda: self.delete_habit(habit_item,
                                                  habit_description),
            )
            delete_button.grid(row=0, column=2, sticky="ew", padx=7)
        except Exception as e:
            print(f"An error occurred while creating a new habit: {e}")

    def create_habit(self, habit_description):
        """
        Create a new habit.

        Parameters:
        - habit_description: The description of the habit to create.
        """
        if hasattr(self, "empty_list_label"):
            self.empty_list_label.grid_forget()
            del self.empty_list_label
        self.mount_habit_item(habit_description)
        self.db.add_habit(habit_description, self.user_id)

    def delete_habit(self, habit_item, habit_description):
        """
        Delete a habit.

        Parameters:
        - habit_item: The UI frame of the habit to delete.
        - habit_description: The description of the habit to delete.
        """
        self.db.delete_habit(habit_description)
        habit_item.destroy()
        if self.habit_inner_frame.grid_size()[1] == 1:
            self.mount_empty_list_frame()

    def edit_habit(self, habit_item):
        """
        Edit a habit.

        Parameters:
        - habit_item: The UI frame of the habit to delete.
        """
        current_description = habit_item.grid_slaves(row=0, column=0)[0].cget(
            "text")
        entry_widget = Entry(
            habit_item,
            font=("Helvetica", self.fontsize["xs"]),
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
        entry_widget.bind("<Return>", lambda event: self.save_habit_edit(
            habit_item,
            entry_widget,
            current_description))

    def save_habit_edit(self, habit_item, entry_widget, current_description):
        """
        Save the edited habit.

        This method is called to save the changes made to a habit's description.
        It updates the habit description in the database and the UI.

        Parameters:
        - habit_item: The UI frame of the habit being edited.
        - entry_widget: The entry widget containing the new description.
        - current_description: The current description of the habit.
        """
        new_description = entry_widget.get()
        self.db.edit_habit(current_description, new_description)
        # Update the label text with the new description not working
        entry_widget.destroy()
        habit_item.grid_slaves(row=0, column=0)[0].config(text=new_description)
        print(habit_item.grid_slaves(row=0, column=0)[0].config
              (text=new_description))
