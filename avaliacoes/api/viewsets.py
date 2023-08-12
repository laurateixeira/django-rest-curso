from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerializer


class AvaliacaoViewSet(ModelViewSet):
    """
    Viewset for Avaliacao app.
    """
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    lookup_field = "comentario" #default is id: must be unique field
