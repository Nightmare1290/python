from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('promocion', views.PromocionList.as_view()),
    path('promocion/<int:pk>', views.PromocionDetail().as_view()),
    path('concurso', views.ConcursoList().as_view()),
    path('concurso/<int:pk>', views.ConcursoDetail().as_view()),
    path('^promocion/(?<cartera>.+)/$', views.PromocionListFillter.as_view()),
    path('^concurso/(?<cartera>.+)/$', views.ConcursoListFillter.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)
