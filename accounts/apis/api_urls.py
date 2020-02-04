from django.urls import path
from accounts.apis.api_views import UserRegistrationAPIView

# urls
urlpatterns = [
    path("register/", UserRegistrationAPIView.as_view(), name="user_register"),
]