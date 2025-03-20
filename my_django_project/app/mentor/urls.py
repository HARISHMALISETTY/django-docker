from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'mentor'

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register('mentors', views.MentorViewSet, basename='mentor')

urlpatterns = [
    # Template URLs
    path('', views.mentor_list, name='mentor_list'),
    path('create/', views.mentor_create, name='mentor_create'),
    path('<int:pk>/', views.mentor_detail, name='mentor_detail'),
    
    # API URLs
    path('api/', include(router.urls)),
] 