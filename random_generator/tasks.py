import json
import random

from channels import Group

from django_graph.celery import app

app.conf.beat_schedule = {
    'generate-random-points': {
        'task': 'random_generator.tasks.get_random_number',
        'schedule': 5.0,
    },
}


@app.task
def get_random_number():
    points = {
        'x': random.random(),
        'y': random.random()
    }
    Group("random-points").send({
        "text": json.dumps(points)
    })
