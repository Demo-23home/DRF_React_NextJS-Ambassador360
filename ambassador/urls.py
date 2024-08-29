from django.urls import path, include
from . import views


urlpatterns = [
    path("", include("common.urls")),
    path("products/frontend/", views.ProductFrontendAPIView.as_view()),
    path("products/backend/", views.ProductBackendAPIView.as_view()),
]
