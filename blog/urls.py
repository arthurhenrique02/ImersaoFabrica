from django.urls import path
from .views import home, novo_contato, ver_contato, update, delete

 # criar os caminhos da url
urlpatterns = [
    path('', home, name = 'home'),
    path('novo_contato/', novo_contato, name='novo_contato'),
    path('post/<int:pk>/', ver_contato, name='ver_contato'),
    path('update/<int:pk>/', update, name='update'),
    path('dele/<int:pk>/', delete, name='delete'), 
]