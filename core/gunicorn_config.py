# gunicorn_config.py

bind = "0.0.0.0:8000"
module = "core.wsgi:application"

workers = 4  # Adjust based on your server's resources
worker_connections = 1000
threads = 4

certfile = "/etc/letsencrypt/live/easy-ege.ru/fullchain.pem"
keyfile = "/etc/letsencrypt/live/easy-ege.ru/privkey.pem"