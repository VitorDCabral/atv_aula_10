import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Sistema Comercial - Cadastro"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30
    page.bgcolor = ft.colors.GREY_50
    page.scroll = "auto"

    def validate_fields(e):
        is_valid = True
        # Validação básica dos campos obrigatórios
        for field in [razao_social, cnpj, email, telefone]:
            if not field.value:
                field.error_text = "Campo obrigatório"
                is_valid = False
                field.update()
            else:
                field.error_text = None
                field.update()
        
        if is_valid:
            page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("Cadastro realizado com sucesso!"),
                    bgcolor=ft.colors.GREEN_600
                )
            )
        page.update()

    # Cabeçalho
    header = ft.Container(
        content=ft.Column([
            ft.Text("Cadastro de Empresa", size=32, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_900),
            ft.Text("Preencha os dados da empresa", size=16, color=ft.colors.GREY_700),
        ]),
        bgcolor=ft.colors.WHITE,
        padding=20,
        border_radius=10,
        margin=ft.margin.only(bottom=20),
    )

    # Campos do formulário
    razao_social = ft.TextField(
        label="Razão Social",
        border_color=ft.colors.BLUE_400,
        prefix_icon=ft.icons.BUSINESS,
        expand=True
    )

    nome_fantasia = ft.TextField(
        label="Nome Fantasia",
        border_color=ft.colors.BLUE_400,
        prefix_icon=ft.icons.STORE,
        expand=True
    )

    cnpj = ft.TextField(
        label="CNPJ",
        border_color=ft.colors.BLUE_400,
        prefix_icon=ft.icons.NUMBERS,
        hint_text="00.000.000/0001-00",
        expand=True
    )

    inscricao_estadual = ft.TextField(
        label="Inscrição Estadual",
        border_color=ft.colors.BLUE_400,
        prefix_icon=ft.icons.DOCUMENT_SCANNER,
        expand=True
    )

    email = ft.TextField(
        label="E-mail",
        border_color=ft.colors.BLUE_400,
        prefix_icon=ft.icons.EMAIL,
        hint_text="empresa@exemplo.com",
        expand=True
    )

    telefone = ft.TextField(
        label="Telefone",
        border_color=ft.colors.BLUE_400,
        prefix_icon=ft.icons.PHONE,
        hint_text="(00) 0000-0000",
        expand=True
    )

    cep = ft.TextField(
        label="CEP",
        border_color=ft.colors.BLUE_400,
        prefix_icon=ft.icons.LOCATION_ON,
        hint_text="00000-000",
        width=200
    )

    endereco = ft.TextField(
        label="Endereço",
        border_color=ft.colors.BLUE_400,
        prefix_icon=ft.icons.HOME,
        expand=True
    )

    numero = ft.TextField(
        label="Número",
        border_color=ft.colors.BLUE_400,
        width=120
    )

    complemento = ft.TextField(
        label="Complemento",
        border_color=ft.colors.BLUE_400,
        expand=True
    )

    bairro = ft.TextField(
        label="Bairro",
        border_color=ft.colors.BLUE_400,
        expand=True
    )

    cidade = ft.TextField(
        label="Cidade",
        border_color=ft.colors.BLUE_400,
        expand=True
    )

    estado = ft.Dropdown(
        label="Estado",
        border_color=ft.colors.BLUE_400,
        width=150,
        options=[
            ft.dropdown.Option("AC"), ft.dropdown.Option("AL"), ft.dropdown.Option("AP"),
            ft.dropdown.Option("AM"), ft.dropdown.Option("BA"), ft.dropdown.Option("CE"),
            ft.dropdown.Option("DF"), ft.dropdown.Option("ES"), ft.dropdown.Option("GO"),
            ft.dropdown.Option("MA"), ft.dropdown.Option("MT"), ft.dropdown.Option("MS"),
            ft.dropdown.Option("MG"), ft.dropdown.Option("PA"), ft.dropdown.Option("PB"),
            ft.dropdown.Option("PR"), ft.dropdown.Option("PE"), ft.dropdown.Option("PI"),
            ft.dropdown.Option("RJ"), ft.dropdown.Option("RN"), ft.dropdown.Option("RS"),
            ft.dropdown.Option("RO"), ft.dropdown.Option("RR"), ft.dropdown.Option("SC"),
            ft.dropdown.Option("SP"), ft.dropdown.Option("SE"), ft.dropdown.Option("TO"),
        ]
    )

    # Botões
    buttons_row = ft.Row(
        controls=[
            ft.ElevatedButton(
                "Cancelar",
                style=ft.ButtonStyle(
                    bgcolor={"": ft.colors.GREY_500},
                    color={"": ft.colors.WHITE},
                ),
                width=150
            ),
            ft.ElevatedButton(
                "Salvar",
                style=ft.ButtonStyle(
                    bgcolor={"": ft.colors.BLUE_700},
                    color={"": ft.colors.WHITE},
                ),
                width=150,
                on_click=validate_fields
            ),
        ],
        alignment=ft.MainAxisAlignment.END,
    )

    # Container principal do formulário
    form_container = ft.Container(
        content=ft.Column([
            ft.Row([razao_social], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([nome_fantasia], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([cnpj, inscricao_estadual], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([email, telefone], alignment=ft.MainAxisAlignment.CENTER),
            ft.Container(
                content=ft.Text("Endereço", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_900),
                margin=ft.margin.only(top=20, bottom=10)
            ),
            ft.Row([cep, endereco, numero], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([complemento, bairro], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([cidade, estado], alignment=ft.MainAxisAlignment.CENTER),
            ft.Container(height=20),
            buttons_row,
        ]),
        bgcolor=ft.colors.WHITE,
        padding=30,
        border_radius=10,
    )

    # Adiciona os elementos à página
    page.add(header, form_container)
    page.update()

ft.app(target=main)