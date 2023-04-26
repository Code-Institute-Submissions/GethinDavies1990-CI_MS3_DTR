from flask import (render_template, Blueprint)

from binge_reviews import app

errors = Blueprint('errors', __name__)


@app.errorhandler(404)
def error_404(error: object) -> object:
    """
    Render 404.html template in case of 404 error
    :return render_template of 404.html
    """
    return render_template('errors/404.html', error=error), 404
