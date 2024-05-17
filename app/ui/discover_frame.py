from tkinter import Frame, Label, Button, Entry, Canvas, Scrollbar, Text
from tkmacosx import Button



class Discover(Frame):
    """Tkinter frame for displaying user's habits."""

    def __init__(self, master, db, user_id, username):
        """Initialize the MyHabits frame."""
        super().__init__(master, bg="#F3F1E7", padx=70, pady=60)
        self.master = master
        self.db = db
        self.user_id = user_id
        self.username = username
        self.grid_columnconfigure(0, weight=1)

        heading_label = Label(
            self,
            text="Discover",
            font=("Helvetica", 32),
            bg="#F3F1EB",
            fg="#2A2A28",
        )
        heading_label.grid(row=0, column=0, sticky="w", padx=10, pady=(30,10))

        self.subheading_label = Text(
            self,
            wrap="word",
            font=("Helvetica", 14),
            spacing3=6,
            bg="#F3F1EB",
            fg="#2A2A28",
            width=30,
            height=10,
            borderwidth=0,
            highlightthickness=0,
        )
        self.subheading_label.insert("1.0", "Here, you'll find a curated collection of habits and ideas to help you lead a healthier, happier life. Explore the categories below to discover new habits, learn actionable tips, and start incorporating positive changes into your daily routine.")
        self.subheading_label.config(state="disabled")
        self.subheading_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)

        self.mount_trending_habits()

    def mount_trending_habits(self):
        self.trending_habits_frame = Frame(self, bg="#F3F1EB")
        self.trending_habits_frame.grid(row=2, column=0, sticky="ew")
        self.trending_habits_frame.grid_columnconfigure(0, weight=1)

        self.h2_label = Label(
            self.trending_habits_frame,
            text="Trending Habits",
            font=("Helvetica", 24),
            bg="#F3F1EB",
            fg="#2A2A28",
        )
        self.h2_label.grid(row=0, column=0, sticky="w", padx=10, pady=(30,20))

        self.trending_habits_container = Frame(self.trending_habits_frame, bg="#F3F1EB")
        self.trending_habits_container.grid(row=1, column=0, sticky="ew")
        

        ## Habit 1 card
        self.habit1_frame = Frame(self.trending_habits_container, bg="#D8B7E3", padx=10, pady=20)
        self.habit1_frame.grid(row=0, column=0, padx=10, sticky="nsew")
        self.habit1_label = Label(
            self.habit1_frame,
            text="Morning Stretching",
            font=("Helvetica", 18),
            bg="#D8B7E3",
            fg="#2A2A28",
        )
        self.habit1_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.habit1_description = Text(
            self.habit1_frame,
            wrap="word",
            font=("Helvetica", 14),
            spacing3=6,
            bg="#D8B7E3",
            fg="#2A2A28",
            width=30,
            height=10,
            borderwidth=0,
            highlightthickness=0,
        )
        self.habit1_description.insert("1.0", "Start your day on the right foot by incorporating a quick stretching routine into your morning ritual. Stretching helps improve flexibility, reduce muscle tension, and increase blood flow, leaving you feeling energized and ready to tackle the day ahead.")
        self.habit1_description.config(state="disabled")
        self.habit1_description.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.create_habit_button = Button(
            self.habit1_frame,
            text="Add to My Habits",
            font=("Helvetica", 14, "bold"),
            fg="#2A2A28",
            bg="#45B9AC",
            highlightbackground="#D8B7E4",
            relief="solid",
            highlightthickness=0,
            borderwidth=0,
            padx=5,
            pady=10,
            cursor="hand2",
            command=lambda: self.add_to_my_habit(self.habit1_label.cget("text")),
        )
        self.create_habit_button.grid(row=3, column=0, sticky="w", pady=10)

        ## Habit 2 card
        self.habit2_frame = Frame(self.trending_habits_container, bg="#D8B7E3", padx=10, pady=20)
        self.habit2_frame.grid(row=0, column=1, padx=10, sticky="nsew")
        self.habit2_label = Label(
            self.habit2_frame,
            text="Pomodoro Technique",
            font=("Helvetica", 18),
            bg="#D8B7E3",
            fg="#2A2A28",
        )
        self.habit2_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.habit2_description = Text(
            self.habit2_frame,
            wrap="word",
            font=("Helvetica", 14),
            spacing3=6,
            bg="#D8B7E3",
            fg="#2A2A28",
            width=30,
            height=10,
            borderwidth=0,
            highlightthickness=0,
        )
        self.habit2_description.insert("1.0", "Boost your productivity and focus with the Pomodoro Technique. This time management method involves breaking your workday into short, focused intervals (typically 25 minutes), followed by a short break. By working in short bursts, you can maintain high levels of concentration and avoid burnout.")
        self.habit2_description.config(state="disabled")
        self.habit2_description.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.create_habit_button = Button(
            self.habit2_frame,
            text="Add to My Habits",
            font=("Helvetica", 14, "bold"),
            fg="#2A2A28",
            bg="#45B9AC",
            highlightbackground="#D8B7E4",
            relief="solid",
            highlightthickness=0,
            borderwidth=0,
            padx=5,
            pady=10,
            cursor="hand2",
            command=lambda: self.add_to_my_habit(self.habit2_label.cget("text")),
        )
        self.create_habit_button.grid(row=3, column=0, sticky="w", pady=10)

        ## Habit 3 card
        self.habit3_frame = Frame(self.trending_habits_container, bg="#D8B7E3", padx=10, pady=20)
        self.habit3_frame.grid(row=0, column=2, padx=10, sticky="nsew")
        self.habit3_label = Label(
            self.habit3_frame,
            text="Evening Meditation",
            font=("Helvetica", 18),
            bg="#D8B7E3",
            fg="#2A2A28",
        )
        self.habit3_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.habit3_description = Text(
            self.habit3_frame,
            wrap="word",
            font=("Helvetica", 14),
            spacing3=6,
            bg="#D8B7E3",
            fg="#2A2A28",
            width=30,
            height=10,
            borderwidth=0,
            highlightthickness=0,
        )
        self.habit3_description.insert("1.0", "Wind down at the end of the day with a relaxing evening meditation practice. Meditation helps calm the mind, reduce stress, and promote a sense of inner peace and tranquility. By incorporating meditation into your evening routine, you can improve sleep quality and prepare your mind for restful sleep.")
        self.habit3_description.config(state="disabled")
        self.habit3_description.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.create_habit_button = Button(
            self.habit3_frame,
            text="Add to My Habits",
            font=("Helvetica", 14, "bold"),
            fg="#2A2A28",
            bg="#45B9AC",
            highlightbackground="#D8B7E4",
            relief="solid",
            highlightthickness=0,
            borderwidth=0,
            padx=5,
            pady=10,
            cursor="hand2",
            command=lambda: self.add_to_my_habit(self.habit3_label.cget("text")),
        )
        self.create_habit_button.grid(row=3, column=0, sticky="w", pady=10)

        ##Habit 4
        self.habit4_frame = Frame(self.trending_habits_container, bg="#D8B7E3", padx=10, pady=20)
        self.habit4_frame.grid(row=0, column=3, padx=10, sticky="nsew")
        self.habit4_label = Label(
            self.habit4_frame,
            text="Gratitude Practice",
            font=("Helvetica", 18),
            bg="#D8B7E3",
            fg="#2A2A28",
        )
        self.habit4_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.habit4_description = Text(
            self.habit4_frame,
            wrap="word",
            font=("Helvetica", 14),
            spacing3=6,
            bg="#D8B7E3",
            fg="#2A2A28",
            width=30,
            height=10,
            borderwidth=0,
            highlightthickness=0,
        )
        self.habit4_description.insert("1.0", "Cultivate a sense of gratitude and appreciation by incorporating a daily gratitude practice into your life. Gratitude has been linked to improved mental and physical health, increased happiness, and stronger relationships. By taking time each day to reflect on the things you're grateful for, you can shift your focus from negativity to positivity and cultivate a more positive outlook on life.")
        self.habit4_description.config(state="disabled")
        self.habit4_description.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.create_habit_button = Button(
            self.habit4_frame,
            text="Add to My Habits",
            font=("Helvetica", 14, "bold"),
            fg="#2A2A28",
            bg="#45B9AC",
            highlightbackground="#D8B7E4",
            relief="solid",
            highlightthickness=0,
            borderwidth=0,
            padx=5,
            pady=10,
            cursor="hand2",
            command=lambda: self.add_to_my_habit(self.habit4_label.cget("text")),
        )
        self.create_habit_button.grid(row=3, column=0, sticky="w", pady=10)

    def add_to_my_habit(self, habit_description):
        print(habit_description)
        self.db.add_habit(habit_description, self.user_id)
