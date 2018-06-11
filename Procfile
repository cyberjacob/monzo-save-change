release: python3 manage.py migrate --noinput
web: gunicorn -b 0.0.0.0:$PORT monzohosting.wsgi --log-file -
