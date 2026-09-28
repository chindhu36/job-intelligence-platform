from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Job Intelligence API is running!"

    from app.routes.jobs import jobs_bp
    app.register_blueprint(jobs_bp, url_prefix="/api/jobs")

    from app.routes.cv import cv_bp
    app.register_blueprint(cv_bp, url_prefix="/api/cv")

    return app