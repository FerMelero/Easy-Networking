from __future__ import annotations
from flask import Flask, redirect, render_template, request, session, url_for
from routes import scan_bp

def create_app() -> Flask:
    app = Flask(__name__)

    # Tienes que pasarle el objeto scan_bp que importaste arriba
    app.register_blueprint(scan_bp) 

    app.config["SECRET_KEY"] = "dev-key"

    @app.route('/')
    def home():
        return redirect(url_for('scan.index_page_scan')) # Redirige al formulario




    @app.errorhandler(404)
    def not_found(e):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error(e):
        return render_template("errors/500.html"), 500

    return app

app = create_app()