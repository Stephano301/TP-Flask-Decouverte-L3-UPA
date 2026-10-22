
from flask import (
    Flask, abort, render_template, request,
    redirect, url_for, flash, session
)

app = Flask(__name__)

# Remplacer cette valeur par une clé générée avec secrets.token_hex()
app.secret_key = "aa63d7eb82dbeefd2963f3bc4f588bd6e2e7bf0084617206eead0e89e734923a"

taches = [
    {
        "id": 1,
        "titre": "Réviser les décorateurs",
        "priorite": "haute",
        "terminee": False
    },
    {
        "id": 2,
        "titre": "Installer Flask",
        "priorite": "normale",
        "terminee": True
    },
    {
        "id": 3,
        "titre": "Lire la doc Jinja2",
        "priorite": "basse",
        "terminee": False
    },
]


@app.route("/")
def index():
    filtre = request.args.get("filtre")

    if filtre in ["toutes", "actives", "terminees"]:
        session["filtre"] = filtre

    filtre = session.get("filtre", "toutes")

    if filtre == "actives":
        liste = [t for t in taches if not t["terminee"]]
    elif filtre == "terminees":
        liste = [t for t in taches if t["terminee"]]
    else:
        liste = taches

    restantes = sum(1 for t in taches if not t["terminee"])

    return render_template(
        "taches.html",
        taches=liste,
        restantes=restantes,
        filtre=filtre
    )


@app.route("/taches/<int:id>")
def tache(id):
    for t in taches:
        if t["id"] == id:
            return render_template("detail.html", tache=t)

    abort(404)


@app.route("/ajouter", methods=["GET", "POST"])
def ajouter():
    if request.method == "POST":
        titre = request.form.get("titre", "").strip()
        priorite = request.form.get("priorite", "")

        if not titre:
            erreur = "Le titre est obligatoire."
        elif len(titre) > 80:
            erreur = "Le titre ne doit pas dépasser 80 caractères."
        elif priorite not in ["basse", "normale", "haute"]:
            erreur = "La priorité choisie est invalide."
        elif any(t["titre"].lower() == titre.lower() for t in taches):
            erreur = "Cette tâche existe déjà."
        else:
            nouvel_id = max(t["id"] for t in taches) + 1

            taches.append({
                "id": nouvel_id,
                "titre": titre,
                "priorite": priorite,
                "terminee": False
            })

            flash("Tâche ajoutée")
            return redirect(url_for("index"))

        return render_template(
            "ajouter.html",
            erreur=erreur,
            titre=titre,
            priorite=priorite
        )

    return render_template(
        "ajouter.html",
        erreur=None,
        titre="",
        priorite="normale"
    )


if __name__ == "__main__":
    app.run(debug=True)
