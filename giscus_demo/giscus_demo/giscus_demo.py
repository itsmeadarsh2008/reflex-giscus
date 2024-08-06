"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from rxconfig import config
import reflex as rx
from reflex_giscus import giscus
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass

def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
        # render_document(),
        rx.spacer(),
        rx.heading('''Welcome to Reflex Giscus!''', size='9', align='center'),
        rx.link('Generate your config at giscus.vercel.app',href='https://giscus.vercel.app/', align='center'),
        rx.code_block(
            '''from reflex_giscus import giscus

rx.color_mode_cond(
    light=giscus(id="comments", theme="light"), dark=giscus(id="comments", theme="dark")
)''',language='python'),
        rx.switch(on_change=rx.toggle_color_mode),
            rx.text(
                "The missing commenting system from Reflex 🚀",
                font_size="2em",
            ),
            rx.color_mode_cond(
                light=giscus(id='comments', theme='light'),
                dark=giscus(id='comments', theme='dark'),
            ),
            rx.logo(),
            align="center",
            spacing="7",
        ),
        # height="100vh",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
