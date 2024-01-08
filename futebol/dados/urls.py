from django.conf import settings
from django.urls import path
from dados import views
from django.conf.urls.static import static
app_name = 'dados'

urlpatterns = [
    path('', views.JogadorList.as_view(), name='list'),
    path('create/', views.JogadorCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.JogadorUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.JogadorDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.JogadorDelete.as_view(), name='delete'),
    path('dados/', views.DadosCreate.as_view(), name='dados'),
    path('dados/excluir/<int:pk>/', views.DadosDeleteView.as_view(), name='dados_delete'),
    path('clube_create/', views.ClubeCreate.as_view(), name='clube_create'),
    path('', views.pagina_inicial, name='pagina_inicial'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
