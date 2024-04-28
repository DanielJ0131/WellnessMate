"""Sport events navigation module."""

from tkinter import Frame, Button, Tk, Label


#class SportEventsFrame:
    """Sport event class for the application."""

    def __init__(self, parent=None, return_callback=None):
        """Initialize the class."""
        self.return_callback = return_callback
        if parent is None:
            self.window = Tk()
        else:
            self.window = parent

        # Create main container
        container = Frame(parent)
        container.grid(row=0, column=1, sticky='nsew')

        # Container style
        container.style = {"width": "100%", "height": "100%",
                           "position": "relative"}

        # Main container
        main_container = Frame(container)
        main_container.grid(row=0, column=1, sticky='nsew') 

        # Defining/customizing widget
        def create_widget(
            parent, width, height, left, top, background,
            text=None, command=None
        ):
            """Create parameters for widget."""
            label = None
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
                button.grid(row=top, column=left, sticky='nsew')
                return button

            else:
                widget = Frame(parent, width=width, height=height,
                               bg=background)
                widget.grid(row=top, column=left, sticky='nsew')
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
                    print("Created label:", label)  # Debugging line
                    if label:
                        label.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
                    else:
                        print("Label is None!")  # Debugging line
                else:
                    print("No text provided!")  # Debugging line
                print("Returning label:", label)  # Debugging line
                return label
        
        def open_to_everyone():
            """Display specific sport events."""
            # >>> This is only saved temporary to later be put in database <<<
            print(" ")

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

        def return_function():
            """Return."""
            if self.return_callback:
                self.return_callback()

        create_widget(main_container, 1024, 700, 0, 0, "#82AACF")  # main widget
        create_widget(
            main_container, 200, 40, 412, 50, "#1165A1",
            "Sporting events in Sweden"
        )
        create_widget(
            main_container,
            210,
            80,
            0,
            1,
            "#1165A1",
            "Open to everyone",
            command=open_to_everyone,
        )
        create_widget(
            main_container,
            210,
            80,
            0,
            2,
            "#1165A1",
            "National leagues, cups and tours",
            command=national_lct_function,
        )
        create_widget(
            main_container,
            293,
            35,
            0,
            3,
            "#1165A1",
            "Elites only",
            command=elites_only_function,
        )
        create_widget(
            main_container,
            100,
            100,
            0,
            4,
            "#1165A1",
            "Return",
            command=return_function,
        )
        self.window.mainloop()


if __name__ == "__main__":
    SportEventsFrame()
