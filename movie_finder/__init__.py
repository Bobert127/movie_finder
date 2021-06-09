from flask import Flask


def create_app():
    movie_finder = Flask(__name__)
    movie_finder.config["SECRET_KEY"] = "secret"

    from movie_finder.Views.main_views import main_bp
    from movie_finder.Views.movie_views import movie_bp
    movie_finder.register_blueprint(main_bp)

    movie_finder.register_blueprint(movie_bp)

    return movie_finder


app = create_app()

