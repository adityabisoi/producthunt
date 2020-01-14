from django.urls import path, include
from . import views

urlpatterns = [
    path('create',views.create, name='create'),
    path('<int:products_id>',views.details, name='details'),
    path('<int:products_id>/upvote',views.upvote, name='upvote')
]