from channels import route
from channels.generic.websockets import WebsocketDemultiplexer
from channels.routing import route_class

from random_generator import consumers
from random_generator.bindings import PointsBinding


class APIDemultiplexer(WebsocketDemultiplexer):

    consumers = {
        'points': PointsBinding.consumer
    }


channel_routing = [
    route('websocket.disconnect', consumers.ws_disconnect),
    route_class(APIDemultiplexer),
]
