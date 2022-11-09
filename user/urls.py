from django.urls import path
from .views import RegisterView, RetrieveUserView , CustomerRegisterView


urlpatterns = [
  path('register', RegisterView.as_view()),
  path('customerregister', CustomerRegisterView.as_view()),

  path('me', RetrieveUserView.as_view()),
]
