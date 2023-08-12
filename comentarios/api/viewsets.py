from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from comentarios.models import Comentario
from .serializers import ComentarioSerializer


class ComentarioViewSet(ModelViewSet):
    """
    Viewset for Comentario app.
    """
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    authentication_classes = [TokenAuthentication] #allow only token authenticated users
    permission_classes = [IsAuthenticated]
