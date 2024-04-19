"""Sport events navigation module."""

import tkinter as tk

root = tk.Tk()
root.geometry("500x500")


# Create main container
container = tk.Frame(root, width=500, height=500)
container.pack(expand=True, fill="both")

# Container style
container_style = {"width": "100%", "height": "100%", "position": "relative"}

# Main container
main_container = tk.Frame(container, **container_style)
main_container.pack(expand=True, fill="both")

