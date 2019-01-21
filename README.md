# django-graph-live-polling
Django app that exposes a Restful api endpoint for a random number generator and display a graph using a streaming plot.ly graph

# Setup and running
1. Install requirements from `requirements.txt` file.
2. Start redis by running `make run-redis`.
3. Start celery-beat by running `make run-celery-beat`.
4. Start celery worker by running `make run-celery-worker`.
5. Run the application `make run`.
6. Go to `http://localhost:8000`.
