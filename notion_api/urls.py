from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views

app_name = "notion_api"

urlpatterns = [
    path("notion-list/", views.NotionListAPIView.as_view()),
    path("notion-list/<int:pk>", views.NotionDetailAPIView.as_view()),
    path("tag-list/", views.TagListAPIView.as_view()),
    path("tag-list/<int:pk>", views.TagDetailAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

# handler404 = api_page_not_found
