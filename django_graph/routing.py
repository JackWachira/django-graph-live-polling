from channels.generic.websockets import WebsocketDemultiplexer
from channels.routing import route_class

from random_generator.bindings import PointsBinding


class APIDemultiplexer(WebsocketDemultiplexer):

    consumers = {
        'points': PointsBinding.consumer
    }


channel_routing = [
    route_class(APIDemultiplexer)
]
