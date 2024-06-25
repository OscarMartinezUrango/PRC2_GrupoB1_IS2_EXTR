from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    
    path('opiniones', views.Opiniones, name='opiniones'),
    path('opiniones/add', views.CrearOpinion.as_view(), name='opinion_formulario'),
    path('opiniones/<int:pk>/update', views.ActualizarOpinion.as_view(), name='opinion_formulario'),
    
    path('destinations/', views.destinations, name='destinations'),
    path('destination/<int:pk>', views.DestinationDetailView.as_view(), name='destination_detail'),
    path('cruise/<int:pk>', views.CruiseDetailView.as_view(), name='cruise_detail'),
    path('info_request', views.InfoRequestCreate.as_view(), name='info_request'),
]