from django.urls import path
from .views import sinCreate, sinDetail, sinEvid, sinView


urlpatterns = [
    path('list/', sinView, name='list'),
    path('create/', sinCreate, name='create'),
    path('evidence/<int:id>', sinDetail, name='evidence'),
    path('detail/<int:id>', sinEvid, name='detail')
]
