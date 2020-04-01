from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.user
        fields = '__all__'


class PromocionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.promocion
        fields = '__all__'


class ConcursoSerializar(serializers.ModelSerializer):
    class Meta:
        model = models.concurso
        fields = '__all__'
