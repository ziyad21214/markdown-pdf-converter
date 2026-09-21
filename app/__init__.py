from flask import Flask

def create_app(Config) -> Flask:
    app = Flask(__name__, template_folder=Config.TEMPLATE_FOLDER,
                static_folder=Config.STATIC_FOLDER)
    app.config.from_object(Config)
    Config.init_app(app)
    from .routes import init_routes
    init_routes(app)
    return app

if __name__ == '__main__':
    app: Flask = create_app()
    app.run(debug=True)