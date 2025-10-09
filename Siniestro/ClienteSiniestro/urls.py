from django.urls import path
from .views import sinCreate, sinDetail, sinEvid, sinView


urlpatterns = [
    path('', sinView, name='list'),
    path('create/', sinCreate, name='create'),
    path('evidence/<int:id>', sinEvid, name='evidence'),
    path('detail/<int:id>', sinDetail, name='detail')
]
