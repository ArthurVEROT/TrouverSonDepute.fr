import csv, sqlite3

con = sqlite3.connect('database.db') # change to 'sqlite:///your_filename.db'
cur = con.cursor()
cur.execute("CREATE TABLE deputes (id, nom,	nom_de_famille, prenom, sexe, date_naissance, lieu_naissance, num_deptmt, nom_circo, num_circo, mandat_debut, mandat_fin, ancien_depute, groupe_sigle, parti_ratt_financier, sites_web, emails, adresses, collaborateurs, autres_mandats, anciens_autres_mandats, anciens_mandats, profession, place_en_hemicycle, url_an, id_an, slug, url_nosdeputes, url_nosdeputes_api, nb_mandats, twitter, circo, FOREIGN KEY(circo) REFERENCES user(circo));") # use your column names here

with open('csv/deputes.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['id'], i['nom'], i['nom_de_famille'], i['prenom'], i['sexe'], i['date_naissance'], i['lieu_naissance'], i['num_deptmt'], i['nom_circo'], i['num_circo'], i['mandat_debut'], i['mandat_fin'], i['ancien_depute'], i['groupe_sigle'], i['parti_ratt_financier'], i['sites_web'],i['emails'],i['adresses'],i['collaborateurs'],i['autres_mandats'],i['anciens_autres_mandats'],i['anciens_mandats'],i['profession'],i['place_en_hemicycle'],i['url_an'],i['id_an'],i['slug'],i['url_nosdeputes'], i['url_nosdeputes_api'], i['nb_mandats'], i['twitter'], i['circo']) for i in dr]

cur.executemany("INSERT INTO deputes (id, nom,	nom_de_famille, prenom, sexe, date_naissance, lieu_naissance, num_deptmt, nom_circo, num_circo, mandat_debut, mandat_fin, ancien_depute, groupe_sigle, parti_ratt_financier, sites_web, emails, adresses, collaborateurs, autres_mandats, anciens_autres_mandats, anciens_mandats, profession, place_en_hemicycle, url_an, id_an, slug, url_nosdeputes, url_nosdeputes_api, nb_mandats, twitter, circo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()