# OC_projet_3
projet 3: aidez Mac Gyver à s'échapper d'un labyrinthe.
Ce programme est un jeu

# Installation
1) allez sur https://github.com/GMBAMorera/OC_projet_3
2) Downloadez le jeu et copiez l'adresse exacte du dossier où vous l'avez installé
3) Ouvrez votre console puis à l'intérieur, tapez 'cd' suivi de l'adresse du dossier du jeu
4) Installer un environnement virtuel avec la commande 'virtualenv -p $env:python3 env' sur windows
5) Activez ensuite l'environnement virtuel avec './env/scripts/activate.ps1'
6) puis, télechargez les prérequis avec la commande 'pip install -r requirements.txt'.
7) Enfin, tapez 'python main.py' dans la commande pour éxecuter le fichier.
8) Voilà: amusez-vous!

# Paramétrages
    Toutes les images sont modifiables. Il vous suffit d'abord pour cela de
déposer vos propres images dans le dossier ressource. Ouvrez ensuite le
fichier constants.py, repérez l'objet que vous désirez modifier puis mettez
le nom de votre fichier à la place de l'ancien. Attention: ne touchez pas au
guillemet et indiquez bien son extension (.bmp, .png, .jpg, ...).
    Le labyrinthe peut être modifié de la même manière en changeant la
disposition des 1 et des 0 dans le fichier 'lab.txt' voir en le remplaçant.
N'oubliez pas de Placer un M à l'emplacement de Départ de Mac Gyver ainsi
qu'un K à celui du gardien.