from rest_framework import viewsets
from .models import Fruit
from .serializers import FruitSerializer

class FruitViewSet(viewsets.ModelViewSet):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer
