from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    """
    A simple Viewset for viewing and editing pontos turisticos.
    """
    serializer_class = PontoTuristicoSerializer
    
    filter_backends = [SearchFilter]
    search_fields = ["nome", "descricao","^endereco__linha1"] #'^': 'istartswith',
                                                              #'=': 'iexact',
                                                              #'@': 'search',
                                                              #'$': 'iregex',

    def get_queryset(self):
        id = self.request.query_params.get("id")
        nome = self.request.query_params.get("nome")
        descricao = self.request.query_params.get("descricao")
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome__iexact=nome) #ignore case

        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)        
        
        return queryset
    
    @action(methods=["get"],detail=True)
    def denunciar(self, request, pk=None): #/pontoturistico/1/denunciar/
        pass


