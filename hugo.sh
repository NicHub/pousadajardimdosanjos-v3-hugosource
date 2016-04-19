#!/bin/bash

case "$1" in

github)
    OUT_PATH="$HOME/Sites/pousadajardimdosanjos/site-web-v3"
    # rm -rf $OUT_PATH # !! Ne pas effacer le répertoire .git !!
    echo "Génération des fichiers GitHub"
    hugo                                                                \
        --destination=$OUT_PATH                                         \
        --baseURL="http://pousadajardimdosanjos.com/"
    cp README.md $OUT_PATH
    if [ -z "$2" ]
    then
        echo "##########"
        echo "site généré à $OUT_PATH"
        COMMENT="Pas de commit sans commentaires !"
    else
        COMMENT=$2
        echo -e "\n### Mise à jour du dépôt “site-web-v3”"
        git add .
        git commit -m "$COMMENT"
        git push
        echo -e "\n### Mise à jour du dépôt “site-web-v3-hugosource"
        cd $OUT_PATH
        git add .
        git commit -m "$COMMENT"
        git push
    fi
    echo -e "\n### COMMENTAIRE = $COMMENT"
    ;;

hostpapa)
    OUT_PATH="$HOME/Sites/pousadajardimdosanjos/site-web-v3/"
    # rm -rf $OUT_PATH
    echo "Génération des fichiers Hostpapa"
    hugo                                                                         \
        --destination=$OUT_PATH                                                  \
        --baseURL="http://pousadajardimdosanjos.com/"
    ;;

*)
    IP=192.168.1.106
    hugo server                 \
        --baseURL="http://$IP/" \
        --bind=$IP              \
        --port=8080             \
        --appendPort=true       \
        --theme pjda
    ;;

esac

exit 0
