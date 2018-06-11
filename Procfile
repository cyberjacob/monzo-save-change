release: python monzohosting/manage.py migrate --noinput
web: gunicorn -b 0.0.0.0:$PORT monzohosting.monzohosting.wsgi --log-file -
