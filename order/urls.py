
from django.urls import re_path
from .views import *
urlpatterns = [
    # re_path(r'upload',upload_resume),
    re_path(r'token', TokenView.as_view()),
    re_path(r'checkorder', CheckOrder.as_view()),
    re_path(r'mailview', MailView.as_view()),

    re_path(r'masterpost', MasterPost.as_view()),
    re_path(r'adminview', AdminView.as_view()),

    re_path(r'masterorder', Master.as_view()),
    re_path(r'customerorder', CustomerOrder.as_view()),

    re_path(r'getrole', Role.as_view()),

    re_path(r'upload',home),



    # re_path(r'verifyotp', VerifyOtp.as_view(), name='verifyotp')

]
