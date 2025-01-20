import flet as ft

def main(page: ft.Page):
    page.title = "Tela de Login"
    page.bgcolor = ft.colors.BLUE_GREY_50
    page.window_width = 400
    page.window_height = 600
    page.window_resizable = True
    
    # Criando as referências dos campos como variáveis do TextField
    username_field = ft.TextField(
        label="Usuário",
        border_radius=10,
        prefix_icon=ft.icons.PERSON,
        bgcolor=ft.colors.WHITE,
        border_color=ft.colors.BLUE_400,
        width=300,
        color = ft.colors.BLACK
    )
    
    password_field = ft.TextField(
        label="Senha",
        border_radius=10,
        prefix_icon=ft.icons.LOCK,
        password=True,
        can_reveal_password=True,
        bgcolor=ft.colors.WHITE,
        border_color=ft.colors.BLUE_400,
        width=300,
        color = ft.colors.BLACK
    )
    
    def on_login_click(e):
        if username_field.value == "admin" and password_field.value == "1234":
            page.show_snack_bar(
                ft.SnackBar(content=ft.Text("Login realizado com sucesso!", color=ft.colors.BLACK))
            )
        else:
            page.show_snack_bar(
                ft.SnackBar(content=ft.Text("Credenciais inválidas!", color=ft.colors.BLACK))
            )
        page.update()

    # Container principal
    login_card = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "Bem-vindo!",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.BLUE_GREY_900,
                    text_align=ft.TextAlign.CENTER,
                ),
                username_field,  # Usando a variável do campo
                password_field,  # Usando a variável do campo
                ft.ElevatedButton(
                    content=ft.Text(
                        "Entrar",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                    ),
                    width=200,
                    height=45,
                    style=ft.ButtonStyle(
                        color={
                            ft.MaterialState.DEFAULT: ft.colors.WHITE,
                        },
                        bgcolor={
                            ft.MaterialState.DEFAULT: ft.colors.BLUE_700,
                            ft.MaterialState.HOVERED: ft.colors.BLUE_800,
                        },
                        elevation={"pressed": 0, "": 5},
                        animation_duration=500,
                        shape=ft.RoundedRectangleBorder(radius=10),
                    ),
                    on_click=on_login_click,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        width=350,
        bgcolor=ft.colors.WHITE,
        border_radius=20,
        padding=30,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.colors.BLUE_GREY_100,
        ),
    )

    # Centraliza o container na página
    page.add(
        ft.Row(
            controls=[login_card],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    def page_resize(e):
        page.update()

    page.on_resize = page_resize
    page.update()

ft.app(target=main)