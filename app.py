# Importation des modules nécessaires
from flask import Flask, render_template, request  # Flask = framework web, render_template = pour afficher la page HTML, request = pour récupérer les données du formulaire
import pandas as pd  # Pandas = pour lire et manipuler les données Excel

# Création de l'application Flask
app = Flask(__name__)

# Chargement du fichier Excel contenant les médicaments dans un DataFrame
df = pd.read_excel("medicaments.xlsx")

# Définition de la route principale "/" qui gère l'affichage de la page et la recherche
@app.route("/", methods=["GET", "POST"])
def index():
    infos = None          # Contiendra les infos du médicament trouvé (si trouvé)
    recherche = ""        # Contiendra le texte saisi par l'utilisateur

    # Si l'utilisateur a soumis le formulaire (méthode POST)
    if request.method == "POST":
        # On récupère le texte saisi dans le champ "produit", on enlève les espaces et on met en minuscules
        recherche = request.form["produit"].strip().lower()
        
        # On cherche dans le DataFrame la ligne où le nom du médicament correspond
        resultat = df[df["nom"].str.lower() == recherche]

        # Si on trouve un résultat (résultat non vide)
        if not resultat.empty:
            # On transforme la première ligne du résultat en dictionnaire (clé : nom de colonne)
            infos = resultat.iloc[0].to_dict()

    # On affiche la page HTML avec les résultats (ou rien si rien trouvé)
    return render_template("index.html", infos=infos, recherche=recherche)

# Lancement de l'application Flask
if __name__ == "__main__":
    # debug=True : recharge automatique en cas de changement du code
    # host="0.0.0.0" : rend l'application accessible sur le réseau local
    # port=8080 : on force le port 8080 au lieu du port par défaut 5000
    app.run(debug=True, host="0.0.0.0", port=8080)


