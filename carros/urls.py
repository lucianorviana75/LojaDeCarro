from django.urls import path
from.import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('form/',views.form, name='form'),
    path('view/<int:pk>/',views.view, name='view'),
    path('create/',views.create, name='create'),
    path('edit/<int:pk>/',views.edit, name='edit'),
    path('update/<int:pk>/',views.update, name='update'),
    path('delete/<int:pk>/',views.delete, name='delete')
]



