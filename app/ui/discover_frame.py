"""Discover frame for displaying user's habits."""
from tkinter import Frame, Label, Button, Text, messagebox
from tkmacosx import Button


class Discover(Frame):
    """Tkinter frame for displaying user's habits."""

    def __init__(self, master, db, user_id, username, fontsize):
        """
        Initialize the Discover frame.

        Args:
            master (Tk or Frame): The parent widget.
            db (Database): The database connection object.
            user_id (int): The ID of the user.
            username (str): The username of the user.
            fontsize (dict): A dictionary containing font sizes
            for different text elements.
        """
        super().__init__(master, bg="#F3F1E7", padx=70, pady=60)
        self.master = master
        self.db = db
        self.user_id = user_id
        self.username = username
        self.fontsize = fontsize
        self.grid_columnconfigure(0, weight=1)

        heading_label = Label(
            self,
            text="Discover",
            font=("Helvetica", self.fontsize["xl"], "bold"),
            bg="#F3F1EB",
            fg="#2A2A28",
        )
        heading_label.grid(row=0, column=0, sticky="w", padx=10, pady=(30, 10))

        self.subheading_label = Text(
            self,
            wrap="word",
            font=("Helvetica", self.fontsize["xs"]),
            bg="#F3F1E7",
            fg="#4C4A46",
            borderwidth=0,
            highlightthickness=0,
            height=3,
            spacing2=7,
        )
        self.subheading_label.insert("1.0", "Here, you'll find a curated collection of habits and ideas to help you lead a healthier, happier life. Explore the categories below to discover new habits, learn actionable tips, and start incorporating positive changes into your daily routine.")
        self.subheading_label.config(state="disabled")
        self.subheading_label.grid(row=1, column=0, sticky="ew",
                                   padx=10, pady=10)

        self.mount_trending_habits()

    def mount_trending_habits(self):
        """Mount the trending habits section with individual habit cards."""
        self.trending_habits_frame = Frame(self, bg="#F3F1EB")
        self.trending_habits_frame.grid(row=2, column=0, sticky="ew")
        self.trending_habits_frame.grid_columnconfigure(0, weight=1)

        self.trending_habits_container = Frame(self.trending_habits_frame,
                                               bg="#F3F1EB")
        self.trending_habits_container.grid(row=1, column=0,
                                            sticky="ew", pady=20)

        self.trending_habits_container.grid_columnconfigure(0, weight=1)
        self.trending_habits_container.grid_columnconfigure(1, weight=1)
        self.trending_habits_container.grid_columnconfigure(2, weight=1)

        self.create_habit_card(
            self.trending_habits_container,
            row=0,
            column=0,
            bg="#D7D97D",
            highlightbackground="#D7D97E",
            title="Morning Stretching",
            description="Stretching in the morning can boost your flexibility, release muscle tension, and get your blood flowing. It's a simple way to feel refreshed and ready to take on whatever comes your way!",
        )

        self.create_habit_card(
            self.trending_habits_container,
            row=0,
            column=1,
            bg="#D9DABF",
            highlightbackground="#D9DABE",
            title="Pomodoro Technique",
            description="Break your work into short, intense bursts (usually 25 minutes), followed by quick breaks. This method helps you stay super focused and avoid burning out.",
        )

        self.create_habit_card(
            self.trending_habits_container,
            row=0,
            column=2,
            bg="#59B2A7",
            highlightbackground="#59B2A9",
            title="Evening Meditation",
            description="It's a great way to ease stress, calm your mind, and feel totally zen. Plus, it sets you up for a peaceful night's sleep, so you wake up feeling refreshed and ready to tackle the day.",
        )

        self.create_habit_card(
            self.trending_habits_container,
            row=1,
            column=0,
            bg="#A1CFC9",
            highlightbackground="#A1CFC8",
            title="Daily Reflections",
            description="Take a few moments each evening to reflect on your day, acknowledging accomplishments, challenges, and moments of growth. Reflective practices encourage self-awareness, promote personal growth, and can help you make positive changes in your life.",
        )

        self.create_habit_card(
            self.trending_habits_container,
            row=1,
            column=1,
            bg="#D7D97D",
            highlightbackground="#D7D97E",
            title="Digital Detox",
            description="Disconnect from screens for a designated period each day to reduce digital overload and reconnect with the present moment. Use this time to engage in activities like reading, journaling, or spending quality time with loved ones.",
        )

        self.create_habit_card(
            self.trending_habits_container,
            row=1,
            column=2,
            bg="#D9DABF",
            highlightbackground="#D9DABE",
            title="Daily Walk",
            description="Walking boosts mood, reduces stress, and supports overall well-being. Aim for at least 30 minutes a day to reap the benefits.",
        )

    def create_habit_card(self, container, row, column, bg,
                          highlightbackground, title, description):
        """
        Create a habit card.

        Args:
            container (Frame): The parent frame for the habit card.
            row (int): The row in the grid layout to place the habit card.
            column (int): Column in the grid layout to place the habit card.
            bg (str): The background color for the habit card.
            highlightbackground (str): Highlight color for the button.
            title (str): The title of the habit.
            description (str): The description of the habit.
        """
        habit_frame = Frame(container, bg=bg, padx=10, pady=20)
        habit_frame.grid(row=row, column=column, padx=15,
                         pady=(30, 30) if row > 0 else 0, sticky="nsew")
        habit_frame.grid_columnconfigure(0, weight=1)

        habit_label = Label(
            habit_frame,
            text=title,
            font=("Helvetica", self.fontsize["m"], "bold"),
            bg=bg,
            fg="#2A2A28",
        )
        habit_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        habit_description = Text(
            habit_frame,
            wrap="word",
            font=("Helvetica", self.fontsize["xxs"]),
            spacing2=4,
            bg=bg,
            fg="#4C4A46",
            height=7,
            borderwidth=0,
            highlightthickness=0,
        )
        habit_description.insert("1.0", description)
        habit_description.config(state="disabled")
        habit_description.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

        create_habit_button = Button(
            habit_frame,
            text="Add to My Habits",
            font=("Helvetica", self.fontsize["xxs"], "bold"),
            fg="#2A2A28",
            bg="#F3F1EB",
            highlightbackground=highlightbackground,
            relief="solid",
            highlightthickness=0,
            borderwidth=0,
            padx=15,
            pady=10,
            cursor="hand2",
            command=lambda: self.add_to_my_habit(habit_label.cget("text")),
        )
        create_habit_button.grid(row=3, column=0, sticky="w", pady=10)

    def add_to_my_habit(self, habit_description):
        """
        Add a habit to the user's habit list.

        Args:
            habit_description (str): The description of the habit to add.
        """
        print(habit_description)
        self.db.add_habit(habit_description, self.user_id)
        messagebox.showinfo("Success", "Habit added successfully!")
