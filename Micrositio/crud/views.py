from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import PromocionSerializer, ConcursoSerializar, UserSerializer
from .models import promocion, concurso, user


class UserList(generics.ListCreateAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer


class PromocionListFillter(generics.ListAPIView):
    serializer_class = PromocionSerializer
    def get_queryset(self):
        cartera = self.kwargs['cartera']
        return promocion.objects.filter(promocion__cartera = cartera)


class PromocionList(generics.ListCreateAPIView):
    queryset = promocion.objects.all()
    serializer_class = PromocionSerializer


class PromocionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = promocion.objects.all()
    serializer_class = PromocionSerializer


class ConcursoListFillter(generics.ListAPIView):
    serializer_class = ConcursoSerializar

    def get_queryset(self):
        cartera = self.kwargs['cartera']
        return concurso.objects.fillter(concurso__cartera = cartera)


class ConcursoList(generics.ListCreateAPIView):
    queryset = concurso.objects.all()
    serializer_class = ConcursoSerializar


class ConcursoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = concurso.objects.all()
    serializer_class = ConcursoSerializar


