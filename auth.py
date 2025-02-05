from dash import no_update
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user

# Configuración de usuarios (en producción esto debería estar en una base de datos segura)
VALID_USERNAME_PASSWORD = {
    'procolombia': 'exportaciones2024'  # usuario: contraseña
}

class User(UserMixin):
    def __init__(self, username):
        self.id = username

# Layout de la página de login
def create_login_layout():
    return dbc.Container([
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader("Iniciar Sesión", className="text-center"),
                        dbc.CardBody(
                            [
                                dbc.Input(id="username", placeholder="Usuario", type="text", className="mb-3"),
                                dbc.Input(id="password", placeholder="Contraseña", type="password", className="mb-3"),
                                dbc.Button("Ingresar", id="login-button", color="primary", className="w-100"),
                                html.Div(id="login-alert", className="mt-3")
                            ]
                        )
                    ],
                    style={"maxWidth": "400px", "margin": "100px auto"}
                )
            )
        )
    ])

# Función para inicializar la autenticación
def init_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app.server)
    login_manager.login_view = '/login'
    
    @login_manager.user_loader
    def load_user(username):
        if username in VALID_USERNAME_PASSWORD:
            return User(username)
        return None

    @app.callback(
        [Output("url", "pathname"),
         Output("login-alert", "children")],
        [Input("login-button", "n_clicks")],
        [State("username", "value"),
         State("password", "value")]
    )
    def login_callback(n_clicks, username, password):
        if n_clicks is None:
            return no_update, ""
        
        if username in VALID_USERNAME_PASSWORD and VALID_USERNAME_PASSWORD[username] == password:
            login_user(User(username))
            return "/paises-potenciales/", ""
        
        return no_update, html.Div("Usuario o contraseña incorrectos", style={"color": "red"})

    return login_manager