"""Welcome to Reflex! This file showcases the custom component in a basic app."""

# from rxconfig import config
import reflex as rx
from reflex_giscus import giscus

def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            # render_document(),
            rx.spacer(),
            rx.heading("""Welcome to Reflex Giscus!""", size="9", align="center"),
            rx.switch(on_change=rx.toggle_color_mode),
            rx.text(
                "The missing commenting system from Reflex 🧐",
                font_size="2em",
                align="center",
            ),
            rx.color_mode_cond(
                light=giscus(id="comments", theme="light", align="center"),
                dark=giscus(id="comments", theme="dark", align="center")
            ),
            rx.logo(),
            align="center",
            spacing="7",
            padding="30px",
        ),
        # height="100vh",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
