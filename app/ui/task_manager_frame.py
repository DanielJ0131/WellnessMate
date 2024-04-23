"""Task manager module for the application."""

import tkinter as tk
from tkinter import messagebox


class TaskManager:
    """Task Manager class for the application."""

    def __init__(self, master):
        """Initialize the Task Manager with the given master window."""
        self.master = master
        master.title("Task Manager")

        # dict to store tasks and their status, value is False if not completed
        self.tasks = {}

        # Active tasks
        self.active_label = tk.Label(
            master, text="Active Tasks: 0", bg="#82AACF", fg="black"
        )
        self.active_label.grid(row=0, column=0, padx=10, pady=5)

        # Active tasks box
        self.active_habit_listbox = tk.Listbox(
            master,
            width=50,
            highlightbackground="#82AACF",
            highlightcolor="#82AACF",
            bg="white",
            fg="black",
        )
        self.active_habit_listbox.grid(row=1, column=0, padx=10, pady=5)
        self.active_habit_listbox.bind("<<ListboxSelect>>", self.on_habit_selected)

        # entry for adding new task with placeholder text
        self.new_task_entry = tk.Entry(master, width=40)
        self.new_task_entry.insert(0, "Enter a new task...")
        self.new_task_entry.config(fg="grey")
        self.new_task_entry.bind("<FocusIn>", self.clear_placeholder)
        self.new_task_entry.bind("<FocusOut>", self.restore_placeholder)
        self.new_task_entry.grid(row=2, column=0, padx=10, pady=5)

        # button to add new task
        self.add_task_button = tk.Button(
            master, text="Add Task", command=self.add_task, bg="#1165A1", fg="white"
        )
        self.add_task_button.grid(row=2, column=1, padx=10, pady=5)

        # separate the active and completed tasks
        self.separator = tk.Frame(master, height=2, bd=1, relief=tk.SUNKEN)
        self.separator.grid(row=0, column=1, padx=5, pady=10, sticky="ns")

        # completed tasks
        self.completed_label = tk.Label(
            master, text="Completed Tasks: 0", bg="#82AACF", fg="black"
        )
        self.completed_label.grid(row=0, column=2, padx=10, pady=5)

        # completed tasks box
        self.completed_habit_listbox = tk.Listbox(
            master,
            width=50,
            highlightbackground="#82AACF",
            highlightcolor="#82AACF",
            bg="white",
            fg="black",
        )
        self.completed_habit_listbox.grid(row=1, column=2, padx=10, pady=5)
        self.completed_habit_listbox.bind("<<ListboxSelect>>", self.on_habit_selected)

        # Task Completed Button
        self.task_completed_button = tk.Button(
            master,
            text="Task Completed",
            command=self.mark_completed,
            bg="#1165A1",
            fg="white",
        )
        self.task_completed_button.grid(row=3, column=0, columnspan=3, pady=5)

        # Initialize counts
        self.update_task_counts()

    def clear_placeholder(self, event):
        """Clear placeholder text when entry is in focus."""
        if self.new_task_entry.get() == "Enter a new task...":
            self.new_task_entry.delete(0, tk.END)
            self.new_task_entry.config(fg="black")

    def restore_placeholder(self, event):
        """Restore placeholder text when entry loses focus."""
        if not self.new_task_entry.get():
            self.new_task_entry.insert(0, "Enter a new task...")
            self.new_task_entry.config(fg="grey")

    def populate_active_habit_list(self):
        # Clear existing items in the listbox
        self.active_habit_listbox.delete(0, tk.END)
        # Add tasks to the listbox
        for task, completed in self.tasks.items():
            if not completed:
                self.active_habit_listbox.insert(tk.END, task)

    def populate_completed_habit_list(self):
        # Clear existing items in the listbox
        self.completed_habit_listbox.delete(0, tk.END)
        # Add completed tasks to the listbox
        for task, completed in self.tasks.items():
            if completed:
                self.completed_habit_listbox.insert(tk.END, task)

    def on_habit_selected(self, event=None):
        # Clear the selection in the other listbox when a task is selected
        self.completed_habit_listbox.selection_clear(0, tk.END)
        # Also clear selection in the entry widget
        self.new_task_entry.delete(0, tk.END)
        self.new_task_entry.insert(0, "Enter a new task...")
        self.new_task_entry.config(fg="grey")

    def mark_completed(self):
        # Get the index of the selected task
        selected_index = self.active_habit_listbox.curselection()
        # Check if a task is selected
        if selected_index:
            task = self.active_habit_listbox.get(selected_index)
            self.tasks[task] = True  # Mark task as completed
            self.active_habit_listbox.delete(
                selected_index
            )  # Remove task from active list
            self.completed_habit_listbox.insert(
                tk.END, task
            )  # Add task to completed list
            self.update_task_counts()
        else:
            # No task selected, display an error message
            messagebox.showerror("Error", "Please select a task to mark as completed.")

    def edit_habit(self):
        # implement code to edit a task, change name or description
        pass

    def add_task(self):
        # Get the task entered by the user
        new_task = self.new_task_entry.get()
        if new_task and new_task != "Enter a new task...":
            # Add the new task to the tasks dictionary
            self.tasks[new_task] = False  # Mark task as not completed
            self.populate_active_habit_list()  # Update the active tasks
            self.new_task_entry.delete(0, tk.END)  # Clear the entry widget
            self.new_task_entry.insert(0, "Enter a new task...")
            self.new_task_entry.config(fg="grey")
            self.update_task_counts()  # Update task counts labels
        else:
            # if entry is empty, show an error message
            messagebox.showerror("Error", "Please enter a task.")

    def update_task_counts(self):
        # update the active and completed task counts
        self.active_tasks = sum(
            1 for _, completed in self.tasks.items() if not completed
        )
        self.completed_tasks = sum(
            1 for _, completed in self.tasks.items() if completed
        )
        self.active_label.config(text=f"Active Tasks: {self.active_tasks}")
        self.completed_label.config(text=f"Completed Tasks: {self.completed_tasks}")


root = tk.Tk()
TaskManager = TaskManager(root)
root.configure(bg="#82AACF")  # Set the background colour to match the theme
root.mainloop()