Gravité — Simulation N‑corps (Pyxel, OOP Version)
Nommé dans l’esprit de Nuit du c0de — Pyxel Shooter (OOP Version), ce dépôt contient une petite simulation gravitationnelle écrite en Python avec Pyxel, organisée en classes orientées objet. Le programme simule l’attraction mutuelle entre plusieurs corps (instances de ) et affiche leur position en 2D via Pyxel. Conçu comme prototype pédagogique, il met l’accent sur la lisibilité du code et la possibilité d’expérimenter paramètres physiques et comportements.

Fonctionnalités principales
• 	Architecture OOP : classes  (corps) et  (boucle principale, rendu).
• 	Simulation gravitationnelle 3D simplifiée : positions en  mais rendu 2D.
• 	Accumulation d’accélérations pour calculer les interactions pair-à-pair avant d’appliquer les vitesses.
• 	Paramètres modifiables : constante gravitationnelle , pas de temps , masses et positions initiales.
• 	Affichage Pyxel minimal pour visualiser les corps en mouvement.

Contrôles et interaction
• 	Aucun contrôle joueur implémenté — la simulation tourne automatiquement.
• 	Pour expérimenter, modifier les valeurs dans le constructeur de  (masses, positions initiales, nombre d’objets).
Structure du code et explication rapide
- Classe rondc
- Attributs : poid (masse), taille, x,y,z, vx,vy,vz.
- Accumulateurs : ax_total, ay_total, az_total pour sommer les accélérations reçues de tous les autres corps.
- Méthodes :
- calculer_vecteur(other) — vecteur dirigé vers other.
- calculer_distance(vecteur) — norme euclidienne du vecteur.
- calculer_force_gra(m1,m2,r) — loi de Newton \; F=G\frac{m_1m_2}{r^2}\;  (protection contre r=0).
- attraction(other) — calcule et ajoute l’accélération due à other dans les accumulateurs.
- appliquer_acceleration() — met à jour les vitesses à partir des accélérations accumulées et remet les accumulateurs à zéro.
- deplacement() — met à jour la position selon la vitesse.
- Classe jeu
- Initialise Pyxel, crée quelques instances de rond et lance la boucle pyxel.run(update, draw).
- update() : pour chaque paire de corps, appelle attraction, puis applique les accélérations et déplace.
- draw() : efface l’écran et dessine les corps avec pyxel.circ.

Paramètres utiles à modifier
- Constante gravitationnelle G : attention à l’échelle — dans le code G est réduite pour rendre la simulation stable.
- Pas de temps dt : actuellement dt = 1. Pour plus de stabilité, intégrer dt dans les mises à jour des vitesses et positions.
- Masses et positions initiales : changer rond(...) dans jeu.__init__ pour tester collisions, orbites, ou éjections.
- Nombre d’objets : convertir la liste self.l pour générer dynamiquement N corps aléatoires.

Améliorations recommandées (roadmap)
- Intégrer dt explicitement dans les équations : \Delta v=a\cdot dt, \Delta x=v\cdot dt.
- Ajout d’un softening pour éviter les forces infinies à très courte distance (ex. remplacer r^2 par r^2+\varepsilon ^2).
- Rendu 3D simple (projection perspective) pour refléter la coordonnée z.
- Optimisation N‑corps : implémenter Barnes‑Hut pour O(N\log N) si N grand.
- Interface utilisateur Pyxel : pause, reset, ajout/suppression de corps, affichage des paramètres.
- Sauvegarde/chargement d’états pour rejouer des scénarios.

Problèmes connus et conseils de débogage
- Valeurs de G et des masses peuvent rendre la simulation instable (vitesses très grandes). Réduire G ou augmenter dt/diminuer masses.
- Collisions non gérées : deux corps qui se superposent peuvent produire comportements non physiques. Ajouter gestion de collision ou fusion si nécessaire.
- Rendu fixe en 2D ignore la profondeur z — pour visualiser la profondeur, mapper z sur la taille ou la couleur.

expérience perso :
- première simulation "réaliste" fait en 2D pour simplicité mais en projet d'une version 3D 