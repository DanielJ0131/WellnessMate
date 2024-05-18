from tkinter import Frame, Label, Button, Entry, Canvas, Scrollbar, Text
from tkmacosx import Button



class Discover(Frame):
    """Tkinter frame for displaying user's habits."""

    def __init__(self, master, db, user_id, username, fontsize):
        """Initialize the MyHabits frame."""
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
        heading_label.grid(row=0, column=0, sticky="w", padx=10, pady=(30,10))

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
        self.subheading_label.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

        self.mount_trending_habits()

    def mount_trending_habits(self):
        self.trending_habits_frame = Frame(self, bg="#F3F1EB")
        self.trending_habits_frame.grid(row=2, column=0, sticky="ew")
        self.trending_habits_frame.grid_columnconfigure(0, weight=1)

        self.trending_habits_container = Frame(self.trending_habits_frame, bg="#F3F1EB")
        self.trending_habits_container.grid(row=1, column=0, sticky="ew", pady=20)


        self.trending_habits_container.grid_columnconfigure(0, weight=1)
        self.trending_habits_container.grid_columnconfigure(1, weight=1)
        self.trending_habits_container.grid_columnconfigure(2, weight=1)

        ## Habit 1 card
        self.habit1_frame = Frame(self.trending_habits_container, bg="#D7D97D", padx=10, pady=20)
        self.habit1_frame.grid(row=0, column=0, padx=15, sticky="nsew")
        self.habit1_frame.grid_columnconfigure(0, weight=1)
        self.habit1_label = Label(
            self.habit1_frame,
            text="Morning Stretching",
            font=("Helvetica", self.fontsize["m"], "bold"),
            bg="#D7D97D",
            fg="#2A2A28",
        )
        self.habit1_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.habit1_description = Text(
            self.habit1_frame,
            wrap="word",
            font=("Helvetica", self.fontsize["xxs"]),
            spacing2=4,
            bg="#D7D97D",
            fg="#4C4A46",
            height=7,
            borderwidth=0,
            highlightthickness=0,
        )
        self.habit1_description.insert("1.0", "Stretching in the morning can boost your flexibility, release muscle tension, and get your blood flowing. It's a simple way to feel refreshed and ready to take on whatever comes your way!")
        self.habit1_description.config(state="disabled")
        self.habit1_description.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
        self.create_habit_button = Button(
            self.habit1_frame,
            text="Add to My Habits",
            font=("Helvetica", self.fontsize["xxs"], "bold"),
            fg="#2A2A28",
            bg="#F3F1EB",
            highlightbackground="#D7D97E",
            relief="solid",
            highlightthickness=0,
            borderwidth=0,
            padx=15,
            pady=10,
            cursor="hand2",
            command=lambda: self.add_to_my_habit(self.habit1_label.cget("text")),
        )
        self.create_habit_button.grid(row=3, column=0, sticky="w", pady=10)

        ## Habit 2 card
        self.habit2_frame = Frame(self.trending_habits_container, bg="#D9DABF", padx=10, pady=20)
        self.habit2_frame.grid(row=0, column=1, padx=15, sticky="nsew")
        self.habit2_frame.grid_columnconfigure(0, weight=1)
        self.habit2_label = Label(
            self.habit2_frame,
            text="Pomodoro Technique",
            font=("Helvetica", self.fontsize["m"], "bold"),
            bg="#D9DABF",
            fg="#2A2A28",
        )
        self.habit2_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.habit2_description = Text(
            self.habit2_frame,
            wrap="word",
            font=("Helvetica", self.fontsize["xxs"]),
            spacing2=4,
            bg="#D9DABF",
            fg="#4C4A46",
            height=7,
            borderwidth=0,
            highlightthickness=0,
        )
        self.habit2_description.insert("1.0", "Break your work into short, intense bursts (usually 25 minutes), followed by quick breaks. This method helps you stay super focused and avoid burning out.")
        self.habit2_description.config(state="disabled")
        self.habit2_description.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
        self.create_habit_button = Button(
            self.habit2_frame,
            text="Add to My Habits",
            font=("Helvetica", self.fontsize["xxs"], "bold"),
            fg="#2A2A28",
            bg="#F3F1EB",
            highlightbackground="#D9DABE",
            relief="solid",
            highlightthickness=0,
            borderwidth=0,
            padx=15,
            pady=10,
            cursor="hand2",
            command=lambda: self.add_to_my_habit(self.habit2_label.cget("text")),
        )
        self.create_habit_button.grid(row=3, column=0, sticky="w", pady=10)

        ## Habit 3 card
        self.habit3_frame = Frame(self.trending_habits_container, bg="#59B2A7", padx=10, pady=20)
        self.habit3_frame.grid(row=0, column=2, padx=15, sticky="nsew")
        self.habit3_frame.grid_columnconfigure(0, weight=1)
        self.habit3_label = Label(
            self.habit3_frame,
            text="Evening Meditation",
            font=("Helvetica", self.fontsize["m"], "bold"),
            bg="#59B2A7",
            fg="#2A2A28",
        )
        self.habit3_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.habit3_description = Text(
            self.habit3_frame,
            wrap="word",
            font=("Helvetica", self.fontsize["xxs"]),
            spacing2=4,
            bg="#59B2A7",
            fg="#4C4A46",
            height=7,
            borderwidth=0,
            highlightthickness=0,
        )
        self.habit3_description.insert("1.0", "It's a great way to ease stress, calm your mind, and feel totally zen. Plus, it sets you up for a peaceful night's sleep, so you wake up feeling refreshed and ready to tackle the day.")
        self.habit3_description.config(state="disabled")
        self.habit3_description.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
        self.create_habit_button = Button(
            self.habit3_frame,
            text="Add to My Habits",
            font=("Helvetica", self.fontsize["xxs"], "bold"),
            fg="#2A2A28",
            bg="#F3F1EB",
            highlightbackground="#59B2A8",
            relief="solid",
            highlightthickness=0,
            borderwidth=0,
            padx=15,
            pady=10,
            cursor="hand2",
            command=lambda: self.add_to_my_habit(self.habit3_label.cget("text")),
        )
        self.create_habit_button.grid(row=3, column=0, sticky="w", pady=10)

        ##Habit 4
        self.habit4_frame = Frame(self.trending_habits_container, bg="#A1CFC9", padx=10, pady=20)
        self.habit4_frame.grid(row=1, column=0, padx=15, pady=30, sticky="nsew")
        self.habit4_frame.grid_columnconfigure(0, weight=1)
        self.habit4_label = Label(
            self.habit4_frame,
            text="Daily Reflections",
            font=("Helvetica", self.fontsize["m"], "bold"),
            bg="#A1CFC9",
            fg="#2A2A28",
        )
        self.habit4_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.habit4_description = Text(
            self.habit4_frame,
            wrap="word",
            font=("Helvetica", self.fontsize["xxs"]),
            spacing2=4,
            bg="#A1CFC9",
            fg="#4C4A46",
            height=7,
            borderwidth=0,
            highlightthickness=0,
        )
        self.habit4_description.insert("1.0", "Take a few moments each evening to reflect on your day, acknowledging accomplishments, challenges, and moments of growth. Reflective practices encourage self-awareness, promote personal growth, and can help you make positive changes in your life.")
        self.habit4_description.config(state="disabled")
        self.habit4_description.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
        self.create_habit_button = Button(
            self.habit4_frame,
            text="Add to My Habits",
            font=("Helvetica", self.fontsize["xxs"], "bold"),
            fg="#2A2A28",
            bg="#F3F1EB",
            highlightbackground="#A1CFC8",
            relief="solid",
            highlightthickness=0,
            borderwidth=0,
            padx=15,
            pady=10,
            cursor="hand2",
            command=lambda: self.add_to_my_habit(self.habit4_label.cget("text")),
        )
        self.create_habit_button.grid(row=3, column=0, sticky="w", pady=10)

        ##Habit 5
        self.habit5_frame = Frame(self.trending_habits_container, bg="#D7D97D", padx=10, pady=20)
        self.habit5_frame.grid(row=1, column=1, padx=15, pady=30, sticky="nsew")
        self.habit5_frame.grid_columnconfigure(0, weight=1)
        self.habit5_label = Label(
            self.habit5_frame,
            text="Digital Detox",
            font=("Helvetica", self.fontsize["m"], "bold"),
            bg="#D7D97D",
            fg="#2A2A28",
        )
        self.habit5_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.habit5_description = Text(
            self.habit5_frame,
            wrap="word",
            font=("Helvetica", self.fontsize["xxs"]),
            spacing2=4,
            bg="#D7D97D",
            fg="#4C4A46",
            height=7,
            borderwidth=0,
            highlightthickness=0,
        )
        self.habit5_description.insert("1.0", "Disconnect from screens for a designated period each day to reduce digital overload and reconnect with the present moment. Use this time to engage in activities like reading, journaling, or spending quality time with loved ones.")
        self.habit5_description.config(state="disabled")
        self.habit5_description.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
        self.create_habit_button = Button(
            self.habit5_frame,
            text="Add to My Habits",
            font=("Helvetica", self.fontsize["xxs"], "bold"),
            fg="#2A2A28",
            bg="#F3F1EB",
            highlightbackground="#D7D97E",
            relief="solid",
            highlightthickness=0,
            borderwidth=0,
            padx=15,
            pady=10,
            cursor="hand2",
            command=lambda: self.add_to_my_habit(self.habit5_label.cget("text")),
        )
        self.create_habit_button.grid(row=3, column=0, sticky="w", pady=10)

        ##Habit 6
        self.habit6_frame = Frame(self.trending_habits_container, bg="#D9DABF", padx=10, pady=20)
        self.habit6_frame.grid(row=1, column=2, padx=15, pady=30, sticky="nsew")
        self.habit6_frame.grid_columnconfigure(0, weight=1)
        self.habit6_label = Label(
            self.habit6_frame,
            text="Daily Walk",
            font=("Helvetica", self.fontsize["m"], "bold"),
            bg="#D9DABF",
            fg="#2A2A28",
        )
        self.habit6_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.habit6_description = Text(
            self.habit6_frame,
            wrap="word",
            font=("Helvetica", self.fontsize["xxs"]),
            spacing2=4,
            bg="#D9DABF",
            fg="#4C4A46",
            height=7,
            borderwidth=0,
            highlightthickness=0,
        )
        self.habit6_description.insert("1.0", "Walking boosts mood, reduces stress, and supports overall well-being. Aim for at least 30 minutes a day to reap the benefits.")
        self.habit6_description.config(state="disabled")
        self.habit6_description.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
        self.create_habit_button = Button(
            self.habit6_frame,
            text="Add to My Habits",
            font=("Helvetica", self.fontsize["xxs"], "bold"),
            fg="#2A2A28",
            bg="#F3F1EB",
            highlightbackground="#D9DABE",
            relief="solid",
            highlightthickness=0,
            borderwidth=0,
            padx=15,
            pady=10,
            cursor="hand2",
            command=lambda: self.add_to_my_habit(self.habit6_label.cget("text")),
        )
        self.create_habit_button.grid(row=3, column=0, sticky="w", pady=10)

    def add_to_my_habit(self, habit_description):
        print(habit_description)
        self.db.add_habit(habit_description, self.user_id)
