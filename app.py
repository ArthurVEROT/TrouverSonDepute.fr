from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Configure application
app = Flask(__name__)

# Configure database
db = SQLAlchemy()
DB_NAME = "database.db" 

# app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = "openspending rocks"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

@app.route('/')
def home():
    return render_template("main.html")

if __name__ == '__main__':
    app.run(debug=True)