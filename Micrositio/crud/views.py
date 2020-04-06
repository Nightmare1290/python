from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import PromocionSerializer, ConcursoSerializar, UserSerializer
from .models import promocion, concurso, user
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, RequestContext
from .forms import UploadConcursoImageForm, UploadPromocionImageForm


def user_login(request):
    if request.method == "POST":
        username = request.POST['nombre']
        password = request.POST['contraseña']
        return user.objects.filter(user__nombre = username, user__contraseña = password)
    else:
        content = {'message' : 'Usuario no encontrado'}
        return Response(content)



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


def upload_image_concurso_view(request):
    if request.method == 'POST':
        form = UploadConcursoImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "Image uploaded succesfully"
        else:
            form = UploadConcursoImageForm()

        return render_to_response(context_instance = RequestContext(request))

def upload_image_promocion_view(request):
    if request.method == 'POST':
        form = UploadPromocionImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "Image uploaded succesfully"
        else:
            form =  UploadPromocionImageForm()

        return render_to_response(context_instance = RequestContext(request))
