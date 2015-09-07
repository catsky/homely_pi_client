script_abspath=$(cd ${0%/*} && echo $PWD/${0##*/})
parent=`dirname "$script_abspath"`
RELEASE_PATH=`dirname "$parent"`


echo ">>> Install Mysql Server >>>"
bash $RELEASE_PATH/misic/auto_mysql.sh

