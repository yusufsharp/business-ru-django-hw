from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# поменять
router = DefaultRouter()
router.register('user_data', views.UserViewSet, basename="user_dataset")

urlpatterns = [
    path('', views.index, name='index'),
    path('study/', views.study, name='study'),
    path('user_data/', views.ItemAPIView.as_view(), name='user_dataset'),
]
urlpatterns += [path(r'api/', include(router.urls))]