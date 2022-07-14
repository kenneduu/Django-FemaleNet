from django.urls import path

from .views import SignUpView
from .views import helpform

urlpatterns = [
    path("signup/", SignUpView.as_view(), name ="signup"),
    path("signup/helpform", helpform, name ="helpform")

]
