#!/usr/bin/python3
"""
imports API App for gunicorn configurations
"""
app = __import__('api.v1.app', globals(), locals(), ['*'])

if __name__ == "__main__":
    """runs the main flask app"""
    app.app.run()
