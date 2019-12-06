Ce repertoire contient tout le code nécessaire pour faire fonctionner notre application de la nuit
de l'info 2019.

Cette application est composée de trois images:
1. Une image avec nodejs et http-server pour exposer un serveur web. PORT 8080
2. Le code ci-contenu qui crée un serveur qui expose une API. PORT 5000
3. Une image de mongodb qui nous permet de faire de la persistance sur la machine.

La configuration du docker-compose est dans le fichier docker-compose.yml

Le code de l'application web se trouve sur: https://github.com/timBorelle/NI2019_Chatbot
Le code de l'api se trouve sur: https://github.com/kaiser185/visits-flask

docker docker-compose sont les deux éléments requis.

Pour démarrer le system (sous linux) il suffit de écrire

$ sudo docker-compose up

