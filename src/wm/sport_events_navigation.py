"""Sport events navigation module."""
import tkinter as tk


class sport_event_navigation:
    """Sport event class for the application."""

    root = tk.Tk()
    root.geometry("490x300")

    # Create main container
    container = tk.Frame(root)
    container.pack(expand=True, fill="both")

    # Container style
    container_style = {
        "width": "100%",
        "height": "100%",
        "position": "relative"
        }

    # Main container
    main_container = tk.Frame(container)
    main_container.pack(expand=True, fill="both")

    # Defining/customizing widget 
    def create_widget(parent, width, height, left, top, background, text=None):
        """Create parameters for widget."""
        widget = tk.Frame(parent, width=width, height=height, bg=background)
        widget.place(x=left, y=top, anchor="nw")
      
        if text:
            label = tk.Label(widget, text=text, bg=background, fg="white",
                             font=("Inter", 14, "bold"),
                             justify="center", wraplength=width)
            label.pack(expand=True, fill="both", padx=10, pady=10)

    # create widget/buttons
    create_widget(main_container, 490, 300, 0, 0, "#82AACF")
    create_widget(main_container, 267, 17, 116, 24, "#1165A1", "Sporting events in Sweden")
    create_widget(main_container, 293, 35, 103, 95, "#1165A1", "Open to everyone")
    create_widget(main_container, 106, 22, 192, 260, "#1165A1", "Return")
    create_widget(main_container, 293, 35, 103, 205, "#1165A1", "National leagues, cups and tours")
    create_widget(main_container, 293, 35, 103, 150, "#1165A1", "Elites only")

    root.mainloop()
