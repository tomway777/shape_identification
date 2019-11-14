from flask import Flask, request, escape

def create_app():
    app = Flask(__name__)


    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    @app.route('/')
    def hello():
        name = request.args.get("name", "World")
        return f'Hello, {escape(name)}!'

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)