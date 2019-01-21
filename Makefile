run:
	@python manage.py runserver

run-celery-worker:
	@celery -A django_graph worker -l info

run-celery-beat:
	@celery -A django_graph beat -l info

run-flower:
	celery flower -A django_graph.celery --address=127.0.0.1 --port=5555

run-redis:
	redis-server --daemonize yes

test: run-redis
	@python manage.py test