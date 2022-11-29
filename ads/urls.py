from django.urls import path

from ads import views

urlpatterns = [
    path('ad/', views.AdsView.as_view()),
    path('ad/create/', views.AdsCreateView.as_view()),
    path('ad/<int:pk>/', views.AdsDetailView.as_view()),
    path('ad/<int:pk>/update/', views.AdsUpdateView.as_view()),
    path('ad/<int:pk>/delete/', views.AdsDeleteView.as_view()),
    path('ad/<int:pk>/upload_image/', views.AdsAddImage.as_view()),

    path('cat/', views.CategoryView.as_view()),
    path('cat/<int:pk>/', views.CategoryDetailView.as_view()),
    path('cat/create/', views.CategoryCreateView.as_view()),
    path('cat/<int:pk>/update/', views.CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete/', views.CategoryDeleteView.as_view()),

    path('user/', views.UsersView.as_view()),
    path('user/<int:pk>/', views.UsersDetailView.as_view()),
    path('user/create/', views.UsersCreateView.as_view()),
    path('user/<int:pk>/update/', views.UsersUpdateView.as_view()),
    path('user/<int:pk>/delete/', views.UsersDeleteView.as_view()),


]