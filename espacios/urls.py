from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.conf import settings


urlpatterns = [
    # Devuelve lista de Espacios
    path('api/espacios/',
         views.EspacioListCreate.as_view()),
    # Devuelve detalles de Usuario Logueado
    path('api/get_detalles_usuario',
         login_required(views.get_detalles_usuario),
         name='get_detalles_usuario'),
    # Devuelve un Espacio y sus Prestaciones
    path('api/espacio/<int:id>/', views.espacioDetail),
    # Devuelve lista de Prestaciones
    path('api/prestaciones/', views.PrestacionListCreate.as_view()),
    # Devuelve una Prestacion
    path('api/prestacion/<int:id>/', views.prestacionDetail),
    # Devuelve lista de Coworks
    path('api/coworks/', views.CoworkListCreate.as_view()),
    # Devuelve un Cowork, Espacios de ese Cowork, Prestaciones y Puestos de cada Espacio
    path('api/cowork/<int:id>/', views.coworkDetail),
    # Devuelve lista de Paises
    path('api/paises/', views.PaisListCreate.as_view()),
    # Devuelve lista de Provincias
    path('api/provincias/', views.ProvinciaListCreate.as_view()),
    # Devuelve lista de Localidades
    path('api/localidades/', views.LocalidadListCreate.as_view()),
    # Devuelve un Puesto y datos del Espacio al que pertenece el mismo, incluyendo Prestaciones y datos del Cowork al que pertenece
    path('api/puesto/<int:id>/', views.puestoDetail),
    # Devuelve lista de Contratos de un Usuario
    path('api/contratos/', login_required(views.contratosUsuario)),
    # Devuelve un Contrato y detalle de Pago de un Usuario
    # Graba puntuacion y reseña de Contrato
    # Graba Contrato y Pago
]
