script_abspath=$(cd ${0%/*} && echo $PWD/${0##*/})
parent=`dirname "$script_abspath"`
RELEASE_PATH=`dirname "$parent"`


echo ">>> Install software..."
sudo apt-get install libpq-dev python-dev

echo ">>> Install Mysql Server >>>"
bash $RELEASE_PATH/misc/auto_mysql.sh

