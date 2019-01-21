from channels_api.bindings import ResourceBinding
from channels_api.decorators import detail_action


class PointsBinding(ResourceBinding):
    stream = "points"
    model = None

    @detail_action()
    def publish(self, pk, data=None, **kwargs):
        return {'action': 'action'}, 200
