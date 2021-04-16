# IA-TICTACTOE
Un programme d'IA tic-tac-toe qui ne perd jamais. Ce programme utilise l'algorithme minimax avec élagage alpha-bêta pour réduire l'espace de recherche.

# NEGAMAX
L'algorithme negamax recherche et évalue les futurs mouvements possibles. C'est une variation de l'algorithme minimax qui est optimisé pour les jeux où la "valeur" de l'état d'un jeu pour un joueur est directement inverse de la valeur pour le joueur adverse. C'est ce qu'on appelle un [jeu à somme nulle] (https://en.wikipedia.org/wiki/Zero-sum_game).

Cet algorithme est conçu pour faire un élagage alpha / bêta, ce qui raccourcit l'arbre de recherche.

Negamax a les restrictions suivantes:

* Cela ne fonctionne que pour les jeux à deux joueurs.
* Cela ne fonctionne pas avec les jeux qui impliquent un caractère aléatoire pendant le jeu. (Le caractère aléatoire initial pour la "configuration du tableau", etc. avant le début du jeu est très bien.)
* Il exige que la valeur du conseil soit de nature à somme nulle.

Détails sur l'algorithme:

* https://en.wikipedia.org/wiki/Negamax
* https://en.wikipedia.org/wiki/Minimax

# LES TECHNOLOGIES UTILISEES
Python, Minimax, Negamax, Flask

# CREDIT

Le code de ce projet imite celui écrit en Python dans la bibliothèque EasyAI située à <https://github.com/Zulko/easyAI>. Cette bibliothèque contient à la fois le moteur de règles de jeu (appelé TwoPlayerGame) ainsi qu'une variété d'algorithmes d'IA pour jouer en tant que joueurs, tels que Negamax.
