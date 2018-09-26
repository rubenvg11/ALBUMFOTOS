from django.urls import path
from AlbumFotos import views
from django.contrib import admin

urlpatterns = [ 
    #path('', views.Primera_vista, name='Primera_vista'), 
    path('', views.base, name='base'), 
    path('categoria/', views.categoria, name='categoria_list'), 
    path('categoria/<int:categoria_id>/detalles', views.categoria_detalles, name='categoria-detalles'),

    path('foto/', views.FotoListView.as_view(), name='foto-list'),
    path('foto/<int:pk>/detalles', views.FotoDetailView.as_view(), name='foto-detail'), 
    # Update
    path('foto/<int:pk>/update/', views.FotoUpdate.as_view(),name='foto-update'),
    #Create
    path('foto/create/', views.FotoCreate.as_view(), name='foto-create'),
    #Delete
    path('foto/<int:pk>/delete/', views.FotoDelete.as_view(),name='foto-delete'),

    #AgregarCategoria
    #path('categoria/create/', views.CategoriaCreate.as_view(),name='categoria-create'),

]