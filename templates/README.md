# Dossier `templates`

But : Contenir les templates HTML utilisées par Flask. Ces fichiers
définissent la structure des pages rendues côté serveur.

Fichiers principaux :

- `index.html` : page principale de la calculatrice. Contient le
  formulaire, le champ d'affichage et les boutons. Le template attend
  une variable `result` fournie par la vue Flask.

Dépendances / hypothèses :

- Utilisation de `render_template('index.html', result=...)` dans
  `app.py` pour fournir les données.
- Le template référence `static/style.css` via
  `url_for('static', filename='style.css')`.

Responsabilité :

- Présenter l'interface utilisateur et fournir les placeholders pour
  l'affichage du résultat et l'envoi des expressions au serveur.
