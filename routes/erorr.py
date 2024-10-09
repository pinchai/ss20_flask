from app import app, render_template, jsonify


# Global handler for 404 errors (Page Not Found)
@app.errorhandler(404)
def handle_404_error(e):
    return jsonify(error="Page not found"), 404


# Global handler for 500 errors (Internal Server Error)
# @app.errorhandler(500)
# def handle_500_error(e):
#     return jsonify(error="Internal server error"), 500


# Global handler for any other uncaught exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify(error=str(e)), 500
