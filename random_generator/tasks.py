from channels import Group

from django_graph.celeryconfig import app

app.conf.beat_schedule = {
    'generate-random-points': {
        'task': 'random_generator.tasks.get_bitcoin_price',
        'schedule': 5.0,
    },
}


@app.task
def get_random_number():
    Group('random-points').send({'text': 'data'})
