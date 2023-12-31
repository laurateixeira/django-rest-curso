from rest_framework.serializers import ModelSerializer, SerializerMethodField
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer

class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True) # many 2 many
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()
    
    class Meta:
        model = PontoTuristico
        fields = ["id","nome","descricao","aprovado","foto",
                  "atracoes","comentarios","avaliacoes","endereco",
                  "descricao_completa","descricao_completa2"]
        
    def get_descricao_completa(self, obj):
        return f"{obj.nome} - {obj.descricao}"    
