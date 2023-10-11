from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('page2/', view=views.page2, name='page2'),
]
