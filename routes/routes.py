from routes.auth.login import login_page
from routes.auth.register import register_page



def register_all_blueprints(app):
    app.register_blueprint(login_page)
    app.register_blueprint(register_page)