import flet as ft
import requests

# Define the URL and the JSON body
url = "https://khuji-ai.onrender.com/process-message"
def ai_response(user_input):
    data = {"message": user_input}

    # Make the POST request
    response = requests.post(url, json=data)
    return response.json()
def main(page: ft.Page):
    page.title = "Chatbot UI"

    page.bgcolor = "#212121"
    page.theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(
            track_visibility=False,
            thumb_visibility=True,
            thumb_color={
                ft.MaterialState.HOVERED: ft.colors.WHITE,
                ft.MaterialState.DEFAULT: ft.colors.TRANSPARENT,
            },
            thickness=5,
            radius=15,
            main_axis_margin=5,
            cross_axis_margin=5,
        )
    )

    # Message container to display chat messages
    messages = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
        width=page.width
    )

    # Function to handle sending messages
    def send_message(e):
        user_message = input_field.value
        if user_message:
            # Add user message on the right side with avatar
            messages.controls.append(
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Container(
                                        content=ft.Text(user_message, size=14, width=150),
                                        padding=ft.padding.all(10),
                                        bgcolor="#d87edb",
                                        border_radius=12,
                                    ),
                                    ft.Text("You", size=10, color="white"),
                                ]
                            ),
                            padding=ft.padding.only(left=10, right=10, top=5, bottom=5),
                            alignment=ft.alignment.center_right,
                        ),
                        ft.Image(src="man.png", width=40, height=40, fit=ft.ImageFit.COVER),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                )
            )
            input_field.value = ""
            page.update()

            # Simulate chatbot response
            chatbot_response = f"You said '{user_message}'"
            messages.controls.append(
                ft.Row(
                    [
                        ft.Image(src="woman.png", width=40, height=40, fit=ft.ImageFit.COVER),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Container(
                                        content=ft.Text(ai_response(user_message), size=14, width=150,color="#FFFFFF"),
                                        padding=ft.padding.all(10),
                                        bgcolor="#000000",
                                        border_radius=12,
                                    ),
                                    ft.Text("Chatbot", size=10, color="white"),
                                ]
                            ),
                            padding=ft.padding.only(left=10, right=10, top=5, bottom=5),
                            alignment=ft.alignment.center_left,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                )
            )
            page.update()

    # Input field for user to type messages
    input_field = ft.TextField(
        hint_text="Type a message...",
        expand=True,
        on_submit=send_message,
        bgcolor="black",
        border_radius=20,
        text_align=ft.TextAlign.LEFT,
        height=50,
        border_color="#ccc",  # Light border color
    )

    # Send button to send the message
    send_button = ft.IconButton(
        icon=ft.icons.SEND,
        on_click=send_message,
        bgcolor="#007bff",  # A blue color similar to Messenger's send button
        icon_color="white",
        width=50  # Adjusted width
    )

    # Bottom row for input and send button
    bottom_row = ft.ResponsiveRow(
        controls=[
            ft.ResponsiveRow(
                controls=[input_field],
                col={
                    "xs": 8,
                    "sm": 9,
                    "md": 10,
                    "lg": 11,
                    "xl": 11,
                }
            ),
            ft.ResponsiveRow(
                controls=[send_button],
                col={
                    "xs": 4,
                    "sm": 3,
                    "md": 2,
                    "lg": 1,
                    "xl": 1,
                }
            )
        ]
    )

    # Main layout
    page.add(
        ft.Column(
            [
                ft.Container(messages, expand=True, padding=10, border=ft.border.all(1, ft.colors.OUTLINE),
                             border_radius=5,),
                ft.Divider(height=1, color="grey"),
                bottom_row
            ],
            expand=True,
        )
    )

ft.app(target=main,assets_dir="assets")
