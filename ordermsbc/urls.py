
from django.urls import re_path
from .views import *
urlpatterns = [
    # re_path(r'upload',upload_resume),
    re_path(r'itemcard', ItemExcel.as_view()),
    re_path(r'bomtable', Bomtable.as_view()),
    re_path(r'weighttable', WeightTable.as_view()),



    # re_path(r'verifyotp', VerifyOtp.as_view(), name='verifyotp')

]
#  for pl in new_data:
#                 yl = pl['particular']
#                 # print(yl)
#                 if yl in particular:
#                     ok = particular.remove(yl)
#                     print(ok)
#                     print(particular)