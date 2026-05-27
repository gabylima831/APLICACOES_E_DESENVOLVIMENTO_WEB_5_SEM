from flask import Flask
from config import Config
from database.models import db
from database.routes.usuarios import usuarios_bp
from flask import render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/frontend")
def frontend():
    return render_template("index.html")

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Registrar blueprint
    app.register_blueprint(usuarios_bp)

    @app.route("/")
    def home():
        return "Servidor Flask com banco de dados rodando!"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
    
