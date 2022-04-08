from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from helpers import localisation, circonscription

# Configure application
app = Flask(__name__)

# Configure database
db = SQLAlchemy()
DB_NAME = "database.db" 

# app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = "openspending rocks"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':

        # Get the circonscription
        address = request.form.get('inputAddress')
        gps = localisation(address)
        circo = circonscription(gps['coordinates'][0], gps['coordinates'][1])

        # Get info about the député
        nom_depute = db.engine.execute('SELECT nom_de_famille FROM deputes WHERE circo = ?;', circo).fetchall()
        prenom_depute = db.engine.execute('SELECT prenom FROM deputes WHERE circo = ?;', circo).fetchall()
        emails_depute = db.engine.execute('SELECT emails FROM deputes WHERE circo = ?;', circo).fetchall()
        slug_depute = db.engine.execute('SELECT slug FROM deputes WHERE circo = ?;', circo).fetchall()
        nom_circo = db.engine.execute('SELECT nom_circo FROM deputes WHERE circo = ?;', circo).fetchall()
        parti = db.engine.execute('SELECT parti_ratt_financier FROM deputes WHERE circo = ?;', circo).fetchall()
        num_circo = db.engine.execute('SELECT num_circo FROM deputes WHERE circo = ?;', circo).fetchall()
        profession = db.engine.execute('SELECT profession FROM deputes WHERE circo = ?;', circo).fetchall()
        url_an = db.engine.execute('SELECT url_an FROM deputes WHERE circo = ?;', circo).fetchall()

        if slug_depute:
            mon_url = "https://www.nosdeputes.fr/depute/photo/" + slug_depute[0][0]
            if '|' in emails_depute[0][0]:
                emailDepute = emails_depute[0][0].split("|")
                data = [nom_depute[0][0], prenom_depute[0][0], emailDepute[0], mon_url, nom_circo[0][0], parti[0][0], num_circo[0][0], profession[0][0], url_an[0][0], emailDepute[1]]
                return render_template("main.html", data=data)
            data = [nom_depute[0][0], prenom_depute[0][0], emails_depute[0][0], mon_url, nom_circo[0][0], parti[0][0], num_circo[0][0], profession[0][0], url_an[0][0]]
            return render_template("main.html", data=data)
        
            
        else:
            return render_template("mainNotFound.html")
    
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)