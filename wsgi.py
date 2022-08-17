"""Application entry point."""
from application import init_app


app = init_app()

"""Application in DEBUG mode, delete this in production"""
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)