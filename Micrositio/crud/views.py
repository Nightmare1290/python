from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import PromocionSerializer, ConcursoSerializar, UserSerializer
from .models import promocion, concurso, user, Client
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, RequestContext
from .forms import UploadConcursoImageForm, UploadPromocionImageForm
from django.http import HttpResponse
from pyexcel_xls import get_data as xsl_get
from pyexcel_xlsx import get_data as xlsx_get
from django.utils.datastructures import MultiValueDictKeyError
import openpyxl


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


def index(request):
    if request.method == 'POST':
        try:
            excel_file = request.FILES['excel_file']
            if str(excel_file).split('.')[-1] == "xls":
                data = xls_get(excel_file, column_limit=5)
            elif str(excel_file).split('.')[-1] == "xlsx":
                data = xlsx_get(excel_file,column_limit=5)
            else:
                return HttpResponse("Invalid File")

            details = data["Detalle"]
            if len(details) > 1:
                for detail in details:
                    if len(detail) > 0 and detail[0] != "Sucursal":
                        Client.objects.create(
                            sucursal=detail[0], cartera= detail[1], clientes=detail[2], fecha_alta=detail[3], saldo=detail[4])
            return HttpResponse("Data Readed")

        except MultiValueDictKeyError:
            return HttpResponse("Invalid File")
    else:
        return render(request, 'excelapp/index.html')


def index(request):
    if request.method == "GET":
        return render(request, 'excelapp/index.html')
    else:
        excel_file = request.Files["excel_file"]
        wb = openpyxl.load_workbook(excel_file)
        worksheet = wb["Detalle"]
        print(worksheet)
        excel_data = list()
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.appens(row_data)
        return render(request, 'excelapp/index.html', {"excel_data": excel_data})