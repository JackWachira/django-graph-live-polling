from channels_api.bindings import ResourceBinding

from .models import Point
from .serializers import PointsSerializer


class PointsBinding(ResourceBinding):

    model = Point
    stream = "points"
    serializer_class = PointsSerializer
    queryset = Point.objects.all()
