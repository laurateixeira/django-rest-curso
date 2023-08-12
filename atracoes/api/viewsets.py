from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracaoSerializer

class AtracaoViewSet(ModelViewSet):
    """
    Viewset for Atracoes app.
    """
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    #filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome', 'descricao']
