"""Sport events navigation module."""

from tkinter import Frame, Button, Tk, Label


class SportEvents:
    """Sport event class for the application."""

    def __init__(self, parent=None):
        """Initialize the class."""
        if parent is None:
            self.window = Tk()
        else:
            self.window = parent

        # Create main container
        container = Frame(parent)
        container.pack(expand=True, fill="both")

        # Container style
        container.style = {"width": "100%", "height": "100%",
                           "position": "relative"}

        # Main container
        main_container = Frame(container)
        main_container.pack(expand=True, fill="both")

        # Defining/customizing widget
        def create_widget(
            parent, width, height, left, top, background,
            text=None, command=None
        ):
            """Create parameters for widget."""
            if command:
                button = Button(
                    parent,
                    text=text,
                    bg=background,
                    fg="white",
                    font=("Inter", 13, "bold"),
                    justify="center",
                    wraplength=width,
                    command=command,
                    cursor="hand2",
                )
                button.place(x=left, y=top, anchor="nw", width=width,
                             height=height)
            else:
                widget = Frame(parent, width=width, height=height,
                               bg=background)
                widget.place(x=left, y=top, anchor="nw")
                if text:
                    label = Label(
                        widget,
                        text=text,
                        bg=background,
                        fg="white",
                        font=("Inter", 14, "bold"),
                        justify="center",
                        wraplength=width,
                    )
                    label.pack(expand=True, fill="both", padx=10, pady=10)

        def open_to_everyone():
            """Display specific sport events."""
            # >>> This is only saved temporary to later be put in database <<<
            print(" ")

        def return_function():
            """Return."""
            # pass

        def national_lct_function():
            """Display sport leagues, cups and tours."""
            # >>> This is only saved temporary to later be put in database <<<

            # Allsvenskan — the top-level men's football league
            # Damallsvenskan — the top-level women's football league
            # Swedish Hockey League — the top-level ice hockey league
            # Elitserien — the top-level bandy league
            # Elitserien — the top-level baseball league
            # Elitserien — the top-level men's handball league
            # Elitserien — the top-level women's handball league
            # Elitserien — the top-level speedway league
            # Svenska Basketligan - the top-level men's basketball league
            # Basketligan Dam - the top-level women's basketball league
            # Svenska Cupen - the main Swedish football cup
            # Swedish Golf Tour - the domestic professional golf tour
            # Swedish Super League — the top-level men's floorball league
            # Swedish Super League — the top-level women's floorball league
            # Swedish Touring Car Championship
            print(" ")

        def elites_only_function():
            """Display event on elite level."""
            # >>> This is only saved temporary to later be put in database <<<
            print(" ")

        create_widget(main_container, 490, 300, 0, 0, "#82AACF")
        create_widget(
            main_container, 267, 17, 116, 24, "#1165A1",
            "Sporting events in Sweden"
        )
        create_widget(
            main_container,
            293,
            35,
            103,
            95,
            "#1165A1",
            "Open to everyone",
            command=open_to_everyone,
        )
        create_widget(
            main_container,
            106,
            22,
            192,
            260,
            "#1165A1",
            "Return",
            command=return_function,
        )
        create_widget(
            main_container,
            293,
            35,
            103,
            205,
            "#1165A1",
            "National leagues, cups and tours",
            command=national_lct_function,
        )
        create_widget(
            main_container,
            293,
            35,
            103,
            150,
            "#1165A1",
            "Elites only",
            command=elites_only_function,
        )

        self.window.mainloop()
