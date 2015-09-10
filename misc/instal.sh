script_abspath=$(cd ${0%/*} && echo $PWD/${0##*/})
parent=`dirname "$script_abspath"`
RELEASE_PATH=`dirname "$parent"`


sudo apt-get update

echo ">>> Install software..."
sudo apt-get install libpq-dev python-dev

echo ">>> Install Postgresql... >>>"
sudo apt-get install postgresql postgresql-contrib
# sudo su - postgres
# createdb homelypi
# createuser -P #root
# psql
# GRANT ALL PRIVILEGES ON DATABASE homelypi TO root;

python manage.py syncdb