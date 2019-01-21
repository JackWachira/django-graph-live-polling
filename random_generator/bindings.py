import json
import random

from channels import Group
from channels_api.bindings import ResourceBinding
from channels_api.decorators import detail_action


class PointsBinding(ResourceBinding):
    stream = "points"
    model = None

    @detail_action()
    def publish(self, pk, data=None, **kwargs):
        """Adds the channel to the group so as
        to start receiving the messages
        """

        Group('random-points').add(self.message.reply_channel)
        self.message.channel_session['random-points'] = 'random-points'
        points = {
            'x': random.random(),
            'y': random.random()
        }
        return {'text': points}, 200
