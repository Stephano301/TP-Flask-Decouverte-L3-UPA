
# Journal de découverte — TP Flask
## Frameworks web Python — L3 UPA

## Mission 1 — Faire tourner Flask
- Essayé : lancer Flask en mode debug et modifier le code.
- Observé : le serveur recharge l'application après une modification.
- Documentation : Flask Quickstart — Debug Mode.
- Expliqué : le mode debug facilite le développement, mais ne doit pas être utilisé en production.

## Mission 2 — Jouer avec les URL
- Essayé : utiliser /taches/2 et /taches/99.
- Observé : la route dynamique reçoit l'identifiant et une tâche inconnue renvoie une erreur 404.
- Documentation : Flask Quickstart — Variable Rules, Redirects and Errors.
- Expliqué : <int:id> convertit l'identifiant en entier ; abort(404) renvoie le bon code HTTP.

## Mission 3 — Afficher les tâches
- Essayé : afficher les tâches avec une boucle et une condition Jinja2.
- Observé : les tâches sont affichées avec leur priorité et leur état.
- Documentation : Flask Quickstart — Rendering Templates ; Jinja Template Designer.
- Expliqué : {{ }} affiche une valeur et {% %} exécute une instruction de template.

## Mission 4 — Un menu commun
- Essayé : utiliser base.html, extends, block et un fichier CSS.
- Observé : les pages partagent le même menu et le même style.
- Documentation : Jinja — Template Inheritance ; Flask — Static Files.
- Expliqué : l'héritage évite de répéter la structure HTML commune.

## Mission 5 — Ajouter une tâche
- Essayé : envoyer le formulaire en POST, valider les données et rediriger.
- Observé : les saisies invalides sont refusées et le rafraîchissement après ajout ne répète pas l'envoi.
- Documentation : Flask Quickstart — HTTP Methods, Accessing Request Data, Redirects and Errors.
- Expliqué : request.form lit les champs envoyés ; redirect et url_for redirigent vers une route.

## Mission 6 — Messages et mémoire
- Essayé : afficher un message flash et mémoriser un filtre dans la session.
- Observé : le message apparaît après l'ajout et le dernier filtre est conservé.
- Documentation : Flask Quickstart — Sessions, Message Flashing, URL Building.
- Expliqué : flash transmet un message temporaire ; session conserve des données associées au visiteur grâce à une clé secrète.

## Bilan final
- L'application affiche la liste et le détail des tâches.
- L'ajout est validé côté serveur.
- Les filtres et les messages fonctionnent.
- Les templates partagent une structure commune.
