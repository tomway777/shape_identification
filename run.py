from flask import Flask, request, escape, render_template

def create_app():
    app = Flask(__name__)


    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)