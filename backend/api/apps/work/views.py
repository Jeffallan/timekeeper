from rest_framework import viewsets
from .models import WorkPerformed
from .serializers import WorkPerformedSerializer


class WorkPerformedViewSet(viewsets.ModelViewSet):
    queryset = WorkPerformed.objects.all()
    serializer_class = WorkPerformedSerializer

    # TODO add get queryset and get serializer class methods and add DRF permissions
