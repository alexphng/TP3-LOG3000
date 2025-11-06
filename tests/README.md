# Tests unitaires (dossier `tests`)

Ce dossier contient les tests unitaires pour l'application de calculatrice.
Les tests sont écrits avec le module `unittest` de Python.

## Contenu

- `test_app.py`
  - Valide la fonction `calculate` définie dans `app.py`
- `test_operators.py`
  - Valide les fonctions arithmétiques `add`, `subtract`, `multiply`, `divide` définies dans `operators.py`.

## Lancer tous les tests

```powershell
python -m unittest discover -v tests
```
