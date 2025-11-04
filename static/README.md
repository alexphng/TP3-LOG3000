# Dossier `static`

But : Contenir les ressources statiques utilisées par l'interface
web (feuilles de style, images, scripts côté client si besoin).

Fichiers principaux :

- `style.css` : styles visuels pour la calculatrice.

Dépendances / hypothèses :

- Les styles sont appliqués par la template HTML via
  `url_for('static', filename='style.css')`.
- Aucune dépendance externe n'est requise (pas de préprocesseur CSS
  dans cette version). Le fichier est du CSS standard.

Responsabilité :

- Fournir une apparence cohérente et accessible pour l'UI. Les
  comportements restent dans le HTML/JS de `templates`.
