"""Sport events navigation module."""
import tkinter as tk


class sport_event_navigation:
    """Sport event class for the application."""

    root = tk.Tk()
    root.geometry("500x500")

    # Create main container
    container = tk.Frame(root, width=500, height=500)
    container.pack(expand=True, fill="both")

    # Container style
    container_style = {
        "width": "100%",
        "height": "100%",
        "position": "relative"
        }

    # Main container
    main_container = tk.Frame(container, **container_style)
    main_container.pack(expand=True, fill="both")

    # Defining/customizing widget 
    def create_wdiget(parent, width, height, left, top, background, text=None):
        """Create parameters for widget."""
        widget = tk.Frame(parent, width=width, height=height, bg=background)
        widget.place(x=left, y=top, anchor="nw")
      
        if text:
            label = tk.Label(widget, text=text, bg=background, fg="white",
                             font=("Inter", 14, "bold"),
                             justify="center", wraplength=width)
            label.pack(expand=True, fill="both", padx=10, pady=10)

    # create widget/buttons
    