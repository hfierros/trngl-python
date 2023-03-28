import os 
from app.main import create_app
from app import blueprint

app = create_app(os.getenv('APP_CONFIG') or 'dev')

app.register_blueprint(blueprint)
app.app_context().push()
