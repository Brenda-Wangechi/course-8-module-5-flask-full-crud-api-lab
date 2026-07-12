"""
Flask Event Management API
Import from the app package and run the server
"""
from app import app

if __name__ == "__main__":
    app.run(debug=True)
