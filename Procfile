release: python sulleys/manage.py migrate --noinput
web: gunicorn --pythonpath=./sulleys sulleys.wsgi
