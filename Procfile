release: python manage.py migrate
web: daphne real_chat.asgi:application --port $PORT --bind 0.0.0.0 -v2
