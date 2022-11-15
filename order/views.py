
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from django.shortcuts import render

# Create your views here.
from urllib import request
from django.shortcuts import render, HttpResponse
from rest_framework.parsers import MultiPartParser, FormParser
import math
# Create your views here.

# Create your views here.
from logging import raiseExceptions
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
# from matplotlib.style import available

from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
import json
from .models import *
from rest_framework. exceptions import AuthenticationFailed
from rest_framework import status
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
import jwt  ,datetime
from rest_framework.authentication import BasicAuthentication
from datetime import date, datetime

from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import MasterDocs


import re
from rest_framework import permissions, status

# from .forms import ResumeForm

# Create your views here.

def home(request):
    # payload, user, user_id = authentication_user(self,request, 'customer')
    # user_instance = CustomUser.objects.filter(id=user_id)
    try:
        if request.method == "POST":

            file = request.FILES["file"]
            document = FileUpload.objects.create(orderfile=file)
            document.save()
            return HttpResponse("Your file is submitted")
    except BaseException as err:
        print(f"Unexpected {err}, {type(err)}")

    return render(request, "upload.html")

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .serializers import FileSerializer


class FileUploadViewSet(viewsets.ViewSet):

    def post(self, request):
        serializer_class = FileSerializer(data=request.data)
        if 'file' not in request.FILES or not serializer_class.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            #Single File
            #handle_uploaded_file(request.FILES['file'])

            #Multiple Files
            files = request.FILES.getlist('file')
            for f in files:
                handle_uploaded_file(f)

            return Response(status=status.HTTP_201_CREATED)

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
# class OrderView(APIView):

#     parser_classes = (FileUploadParser,)
#     parser_classes = (MultiPartParser, FormParser)


#     def post(self, request):
#         payload, user, user_id = authentication_user(self,request, 'customer')

#         # parser_classes = (MultiPartParser, FormParser)

#         file = request.data.get('file', None)
#         print(user_id)
#         m = CustomUser.objects.filter(id=user_id).create(ordefile=file)

#         # serializer = OrderSerializer(data=request_data)
#         # serializer.is_valid(raise_exception=True)
#         # serializer.save()
#         return Response({"msg":"failed"})
    
#     def get(self, request):
#         payload, user, user_id = authentication_user(self,request, 'customer')
#         try:
#             t = Order.objects.filter(customer_id=user_id).values_list('orderfile')[0][0]
#             file = open(t, 'w')
#             print(file)
#             o = my_file_handle=open(t)
#             # o = my_file_handle.read()
#             # print(o)
#         except BaseException as err:
#             print(f"Unexpected {err}, {type(err)}")
#             return Response("done")

from django.core.files.base import ContentFile, File
from rest_framework import parsers        

from django.core.files.storage import FileSystemStorage
import pandas
class Master(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # payload, user, user_id = authentication_user(self,request, 'customer')
        # t = Order.objects.filter(customer_id=user_id).values_list('orderfile')[0][0]
        # f = FileSystemStorage.open(t, 'r')
        # data = f.read()
        # print(data,'+++++++++++')
        # m =master()
        user = request.user.id
        u = UserAccount.objects.filter(id=user).values_list('role')[0][0]
        print(u)
        if u == "admin":    
            t = MasterDocs.objects.all().values_list('document')[0][0]
            print(t)
            excel_data_df = pandas.read_excel(t, sheet_name='Translator')
            for ind in excel_data_df.index:
                # print(excel_data_df['Particular'][ind], excel_data_df['Ordered ItemCode'][ind],excel_data_df['Base Itemcode'][ind], excel_data_df['Qty'][ind])
                p = excel_data_df['Particular'][ind]
                o = excel_data_df['Ordered ItemCode'][ind]
                b = excel_data_df['Base Itemcode'][ind]
                q = excel_data_df['Qty'][ind]
                print(p,o,b,q)
                MasterModel.objects.create(Particular=p,Ordered_ItemCode=o,Base_ItemCode=b,Qty=q)
            MasterDocs.objects.all().delete()
            return Response("hello")
        else:
            return Response("Acces Denied")

    def post(self, request):
        if request.method == "POST":
            allimages = request.FILES['file']
            allimages.save()
            t = MasterDocs.objects.create(document=allimages)
            p = MasterDocs.objects.all().values_list('document')[0][0]
            return Response(p)

class MasterPost(APIView):
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def post(self, request, *args, **kwargs):
        try:
            if request.method == "POST":
                allimages = request.FILES['file']
                t = MasterDocs.objects.create(document=allimages)
                return Response('hello')
        except BaseException as err:
            print(f"Unexpected {err}, {type(err)}")




# class CustomerOrder(APIView):
#     permission_classes = [permissions.IsAuthenticated]


#     def post(self, request):
#         user_id = request.user.id
#         user_instance = UserAccount.objects.filter(id=user_id)

#         print(user_id,'user id')
#         if request.method == "POST":
#                 allimages = request.FILES['file']
#                 fi = Docs.objects.create(customer_id=user_instance[0],document=allimages)
#         # request.data['customer_id'] = user_id
#         t = Docs.objects.filter(customer_id=user_id).values_list('document')[0][0]
#         print(t)
#         excel_data_df = pandas.read_excel(t, sheet_name='Sheet1')
#         print(user_instance)
#         custdate = datetime.today().date().strftime("%d%m%y")
#         print(user_id)
#         cust = f"{request.user.username}{custdate}"
#         # print(custdate)
#         usr = request.user.username
#         # print(cust)
#         master = list(MasterModel.objects.all().values_list('Particular','Ordered_ItemCode','Base_ItemCode','Qty'))
#         tab = list(MasterModel.objects.all().values_list('Particular'))
#         for i in tab:
#             i[0]
        

        
#             # print(d)
#         # print(master.count())
#         # print(master)
#         try:
#                     # print(d)
#             for ind in excel_data_df.index:
#                 p = excel_data_df['Particular[Ship]'][ind].replace('[RAM]',"")

#                 # if p in i[0]:
#                 #     cust = f"{user.username}{custdate}_02"
#                 # else:
#                 #     cust = f"{user.username}{custdate}"


#                 # r = excel_data_df['Particular[Ship]'][ind]   
#                 # print(r[-5:-0])
#                 # print(r[-5:])
#                 c = excel_data_df['Consignee Name'][ind]
#                 ca = excel_data_df['Complete Address'][ind]
#                 pc = excel_data_df['Pincode'][ind]
#                 coun = excel_data_df['COUNTRY'][ind]
#                 phn = excel_data_df['Phone'][ind]

#             for i in master:
#                     d =i
#                     print(d)
#                     # b = i[2]
#                     # print(d)
#                     if p in d:
#                         new_order= d[0]
#                         print(new_order)
#                         new_item= d[1]
#                         new_base= d[2]
#                         new_qty= d[3]
#                         data = {
#                             "filename" :cust,
#                             "partuclar":p,
#                             "itemcode":new_item,
#                             "base_item_code":new_base,
#                             "qty":new_qty,
#                             "cust":usr,
#                             "address":ca,
#                             "consignee":c,
#                             "country":coun,
#                             "phone":phn,
#                             "pincode":pc


#                         }
#                         serializer = OrderSerializer(data=data)
#                         serializer.is_valid(raise_exception=True)
#                         Order.objects.filter(customer_id=user_id).create(customer_id=user_instance[0],file_name=cust,particular=p,itemcode=new_item,base_item_code=new_base,qty=new_qty,cust=usr,address=ca,consignee=c,country=coun,phone=phn,pincode=pc)
#                         deletefile = Docs.objects.filter(customer_id=user_id).delete()
#                         # dt = Order.objects.filter(customer_id=user_id).values('file_name','particular','itemcode','base_item_code','qty','address','ship_by','consignee','phone','pincode')
                 
#                         # print(p)
                        

#                         # print(new_order,new_item,new_base,new_qty)
#                 # print(p)
#             dt = Order.objects.filter(customer_id=user_id).values('file_name','particular','itemcode','base_item_code','qty','address','ship_by','consignee','phone','pincode')
#             return Response(dt)
#         except BaseException as err:
#             print(f"Unexpected {err}, {type(err)}")
    
    



class CustomerOrder(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]


    def post(self, request):
        user_id = request.user.id
        user_instance = UserAccount.objects.filter(id=user_id)

        print(user_id,'user id')
        # if request.method == "POST":
        #         allimages = request.FILES['file']
        #         fi = Docs.objects.create(customer_id=user_instance[0],document=allimages)
        # request.data['customer_id'] = user_id
        t = Docs.objects.filter(customer_id=user_id).values_list('document')[0][0]
        print(t)
        excel_data_df = pandas.read_excel(t, sheet_name='Sheet1')
        print(user_instance)
        custdate = datetime.today().date().strftime("%y%m%d")
        print(user_id)
        cust = f"{request.user.username}_{custdate}"
        # print(custdate)
        usr = request.user.username
        # print(cust)
        master_object = Order.objects.filter(customer_id=user_id).values_list('file_name')
        print('master_object',master_object)

        master = list(MasterModel.objects.all().values_list('Particular','Ordered_ItemCode','Base_ItemCode','Qty'))
        tab = list(MasterModel.objects.all().values_list('Particular'))
        new_data = []
        new_con = []
        part = []
        hello = []

        # for ind in excel_data_df.index:
        #         shi = excel_data_df['Particular[Ship]'][ind][-5:]
        #         print('ship by',shi)
        # for i in tab:
        #     i[0]
        number = 0
        print('counttt',number)
        for mt in master_object:
            ml = mt[0]
            cust = f"{request.user.username}_{custdate}"
            print('master oasdasdas',ml)
            if cust in ml:
                number += 1
                cust = f"{request.user.username}-{custdate}-{number}"
                print('new num', cust)
            else:
                cust = f"{request.user.username}-{custdate}"

        

        
            # print(d)
        # print(master.count())
        # print(master)
        try:
                    # print(d)
            # for ind in excel_data_df.index:
            #     shi = excel_data_df['Particular[Ship]'][ind][-5:]
            #     print('ship by',shi)
            for ind in excel_data_df.index:
                p = excel_data_df['Particular[Ship]'][ind].replace('[RAM]',"")
                part.append(p)
                shi = excel_data_df['Particular[Ship]'][ind][-5:]
                print('ship by',shi)

                # if p in i[0]:
                #     cust = f"{user.username}{custdate}_02"
                # else:
                #     cust = f"{user.username}{custdate}"


                # r = excel_data_df['Particular[Ship]'][ind]   
                # print(r[-5:-0])
                # print(r[-5:])
                c = excel_data_df['Consignee Name'][ind]
                ca = excel_data_df['Complete Address'][ind]
                pc = excel_data_df['Pincode'][ind]
                coun = excel_data_df['COUNTRY'][ind]
                phn = excel_data_df['Phone'][ind]
                # print('pppppooooo',p)
                pdata = {
                    "filename":p,
                    "consignee":c,
                    "address":ca,
                    "country":coun
                }
                new_con.append(pdata)


                for i in master:
                        d =i
                        # print(d)
                        # print('for loop',p)
                        # b = i[2]
                        # print(d)
                        if p in d:
                            # print('ppppp',p)
                            new_order= d[0]
                            print(new_order)
                            new_item= d[1]
                            new_base= d[2]
                            new_qty= d[3]
                            data = {
                                "filename" :cust,
                                "particular":p,
                                "itemcode":new_item,
                                # "base_item_code":new_base,
                                # "qty":new_qty,
                                "cust":usr,
                                "address":ca,
                                "ship_by":shi,
                                "consignee":c,
                                "country":coun,
                                "phone":phn,
                                "pincode":pc


                            }
                            new_data.append(data)
                            serializer = OrderSerializer(data=data)
                            serializer.is_valid(raise_exception=True)
                            Order.objects.filter(customer_id=user_id).create(customer_id=user_instance[0],file_name=cust,particular=p,itemcode=new_item,base_item_code=new_base,qty=new_qty,cust=usr,address=ca,consignee=c,country=coun,phone=phn,pincode=pc,ship_by=shi)
                            deletefile = Docs.objects.filter(customer_id=user_id).delete()
                            dt = Order.objects.filter(customer_id=user_id).values('file_name','particular','itemcode','base_item_code','qty','address','ship_by','consignee','phone','pincode')
                    
                            print(p)
                            

                            # print(new_order,new_item,new_base,new_qty)
                    # print(p)
            master_country = UserAccount.objects.filter(id=user_id).values_list('country')[0][0].upper()

            user_email= UserAccount.objects.filter(id=user_id).values_list('email')[0][0]
            # user_txt= TextField.objects.filter(customer_id=user_id).values_list('txtfile')[0][0]
            for pl in new_data:
                yl = pl['particular']
                ylp = pl['consignee']
               
                # print(yl)
                if yl in part:
                    ok = part.remove(yl)
            # for i in part:
            #     t = {
            #         "filename":i,
            #     }
                # new_temp.append(t)
            if part not in new_con:
                print('aellloooo joy',part)
                party = part    
                print(party)
                for t in party:
                    tt = t
                    print('new tt',tt)
                    for i in new_con:
                        file = i['filename']
                        file_consginee = i['consignee']
                        file_address = i['address']
                        file_country = i['country']
                        print('file country',file_country)

                        if file_country == master_country:
                            print('-------------s',file_country)
                            file_country
                        else:
                            file_country = "NA"
                        
                        if tt == file:
                            data = {
                                "particular":tt,
                                "consinee":file_consginee,
                                "address":file_address,
                                "country":file_country,
                            }
                            hello.append(data)
            print('helllooo data',hello)
            new_e = TextField.objects.filter(customer_id=user_id).create(customer_id=user_instance[0],txtfile=hello)
            # mail(user_email,new_data)
            # dt = Order.objects.filter(customer_id=user_id).values('file_name','particular','itemcode','base_item_code','qty','address','ship_by','consignee','phone','pincode')
            return Response({"accept":new_data,"reject":hello})
        except BaseException as err:
            print(f"Unexpected {err}, {type(err)}")
    def get(self, request):
        user_id = request.user.id
        print(user_id,'user id')
        # request.data['customer_id'] = user_id
        t = Order.objects.filter(customer_id=user_id).values('file_name','particular','itemcode','base_item_code','qty','address','ship_by','consignee','phone','pincode')
        return Response(t)

class CheckOrder(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]


    def post(self, request):
        user_id = request.user.id
        user_instance = UserAccount.objects.filter(id=user_id)

        print(user_id,'user id')
        if request.method == "POST":
                print()
                allimages = request.FILES['file']
                print('fileeeeee',allimages)
                fi = Docs.objects.create(customer_id=user_instance[0],document=allimages)
        # request.data['customer_id'] = user_id
        t = Docs.objects.filter(customer_id=user_id).values_list('document')[0][0]
        print(t)
        excel_data_df = pandas.read_excel(t, sheet_name='Sheet1')
        print(user_instance)
        custdate = datetime.today().date().strftime("%y%m%d")
        print(user_id)
        # cust = f"{request.user.username}-{custdate}"
        master_object = Order.objects.filter(customer_id=user_id).values_list('file_name')

        # print(custdate)
        usr = request.user.username
        # print(cust)
        master = list(MasterModel.objects.all().values_list('Particular','Ordered_ItemCode','Base_ItemCode','Qty'))
        tab = list(MasterModel.objects.all().values_list('Particular'))
        master_country = UserAccount.objects.filter(id=user_id).values_list('country')[0][0].upper()
        # master_country = "JAPAN"
        print('master country',master_country)

        new_data = []
        part = []
        new_temp = []
        new_conginee = []
        hello = []
        
        # for i in tab:
        #     i[0]
        cust = f"{request.user.username}_{custdate}"

        number = 0
        print('counttt',number)
        for mt in master_object:
            ml = mt[0]
            print('master oasdasdas',ml)
            if cust in ml:
                number += 1
                cust = f"{request.user.username}-{custdate}-{number}"
                print('new num', cust)
            else:
                cust = f"{request.user.username}-{custdate}"

        
            # print(d)
        # print(master.count())
        # print(master)
        try:
                    # print(d)
            for ind in excel_data_df.index:
                p = excel_data_df['Particular[Ship]'][ind].replace('[RAM]',"")
                part.append(p)
                shi = excel_data_df['Particular[Ship]'][ind][-5:]
                print('ship by',shi,p)

                # if p in i[0]:
                #     cust = f"{user.username}{custdate}_02"
                # else:
                #     cust = f"{user.username}{custdate}"


                # r = excel_data_df['Particular[Ship]'][ind]   
                # print(r[-5:-0])
                # print(r[-5:])
                c = excel_data_df['Consignee Name'][ind]
                # new_conginee.append(c)
                ca = excel_data_df['Complete Address'][ind]
                pc = excel_data_df['Pincode'][ind]
                coun = excel_data_df['COUNTRY'][ind]
                phn = excel_data_df['Phone'][ind]
                pdata = {
                    "filename":p,
                    "consignee":c,
                    "address":ca,
                    "country":coun
                }
                new_conginee.append(pdata)
                # print('pppppooooo',p)


                for i in master:
                        d =i
                        # print(d)
                        # print('for loop',p)
                        # b = i[2]
                        # print(d)
                        if p in d:
                            # print('ppppp',p)
                            new_order= d[0]
                            # print(new_order)
                            new_item= d[1]
                            new_base= d[2]
                            new_qty= d[3]
                            data = {
                                "filename" :cust,
                                "particular":p,
                                "itemcode":new_item,
                                # "base_item_code":new_base,    ###### Will uncomment when data will provided as per abhishek sir
                                "cust":usr,
                                "address":ca,
                                "ship by":shi,
                                "consignee":c,
                                "country":coun,
                                "phone":phn,
                                "pincode":pc


                            }
                            new_data.append(data)
                            # serializer = OrderSerializer(data=data)
                            # serializer.is_valid(raise_exception=True)
                            # Order.objects.filter(customer_id=user_id).create(customer_id=user_instance[0],file_name=cust,particular=p,itemcode=new_item,base_item_code=new_base,qty=new_qty,cust=usr,address=ca,consignee=c,country=coun,phone=phn,pincode=pc)
                            # dt = Order.objects.filter(customer_id=user_id).values('file_name','particular','itemcode','base_item_code','qty','address','ship_by','consignee','phone','pincode')
                    
                            # print(p)
                            
            # print('old',part)
            for pl in new_data:
                yl = pl['particular']
                ylp = pl['consignee']
               
                # print(yl)
                if yl in part:
                    ok = part.remove(yl)
            # for i in part:
            #     t = {
            #         "filename":i,
            #     }
                new_temp.append(t)
            if part not in new_conginee:
                print('aellloooo joy',part)
                party = part    
                print(party)
                for t in party:
                    tt = t
                    print('new tt',tt)
                    for i in new_conginee:
                        file = i['filename']
                        file_consginee = i['consignee']
                        file_address = i['address']
                        file_country = i['country']
                        print('file country',file_country)

                        if file_country == master_country:
                            print('-------------s',file_country)
                            file_country
                        else:
                            file_country = "NA"
                        
                        if tt == file:
                            data = {
                                "particular":tt,
                                "consinee":file_consginee,
                                "address":file_address,
                                "country":file_country,
                            }
                            hello.append(data)
                            


                #         t = {
            #             "filename":part
            #         }
            #         new_temp.append(t)
            # print("new dta",new_conginee)
            print('new hello', hello)
            # print('new',part)               # print(new_order,new_item,new_base,new_qty)
                    # print(p)
            # dt = Order.objects.filter(customer_id=user_id).values('file_name','particular','itemcode','base_item_code','qty','address','ship_by','consignee','phone','pincode')
            return Response({"accept":new_data,"reject" : hello})
        except BaseException as err:
            print(f"Unexpected {err}, {type(err)}")




class Role(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user_id = request.user.id
        print(user_id,'user id')
        # request.data['customer_id'] = user_id
        t = UserAccount.objects.filter(id=user_id).values_list('role')[0][0]
        return Response(t)

from django.middleware.csrf import get_token
class TokenView(APIView):
    
    def post(self,request):
        return JsonResponse({'csrfToken': get_token(request)})


class AdminView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user_id = request.user.id
        user_name = request.user
        print(user_id,user_name)
        user_instance= UserAccount.objects.filter(id=user_id).values_list('role')[0][0]
        print(user_instance)
        if user_instance == "admin":
        # authentication_classes = [BasicAuthentication]
        # permission_classes = [IsAuthenticated]
            u = UserAccount.objects.all().values('username','phone','role')
            return Response(u)
        else:
            return Response("Access denied" ,status=status.HTTP_401_UNAUTHORIZED)

class MailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request):
        user_id = request.user.id
        user_name = request.user
        # ma = request.data['email']
        # print(user_id,user_name)
        user_instance= UserAccount.objects.filter(id=user_id).values_list('email')[0][0]
        user_usr= UserAccount.objects.filter(id=user_id).values_list('username')[0][0]
        user_txt= TextField.objects.filter(customer_id=user_id).values_list('txtfile').all()
        # print('helli',user_txt) 

        # print(user_instance, user_usr)
        t = Order.objects.filter(customer_id=user_id).values()
        # lo = ""
        new_data = []
        # for i in user_txt:
        #     print(i)
        #     lo = i
        # print('lol',lo)
        # rejectmail(user_instance,user_txt)
        TextField.objects.filter(customer_id=user_id).delete()
        # print('mail sent')
        # print(t)
        return Response('Mailed',status=status.HTTP_200_OK)



        
import smtplib



def mail(dt,return_data):
    
    gmail_user = 'info.skyrath@gmail.com'
    gmail_password = 'krnhpoggbebcqhcx'

    sent_from = gmail_user
    p = []
    # for i in data:
    #     n = i[0]['data']
    # # print(type(n))
    #     p.append(f"{n} \n")
    # o = ''.join(map(str,return_data))
    # print('oooooooooo')
    to = [dt]
    subject = f'Order from {dt} has been placed'
    body = return_data
    # for op in body:
    #     print(op)
    # print(body)
    message = 'Subject: {}\n\n{}'.format(subject, body).encode('utf-8')
    # print('mesage',message)
    email_text = """\
    From: %s
    To: %s
    Subject: %s
        %s
    """ % (sent_from, ", ".join(to), subject, body)
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to,message)
        # print('for loop run')
        print ("Email sent successfully!")

    except Exception as ex:
        print ("Something went wrong….",ex)
# mail()   
def rejectmail(dt,return_data):
    
    gmail_user = 'info.skyrath@gmail.com'
    gmail_password = 'krnhpoggbebcqhcx'

    sent_from = gmail_user
    p = []
    # for i in data:
    #     n = i[0]['data']
    # # print(type(n))
    #     p.append(f"{n} \n")
    # o = ''.join(map(str,return_data))
    # print('oooooooooo')
    to = [dt]
    subject = f'Order from {dt} has rejected items '
    body = return_data
    # for op in body:
    #     print(op)
    # print(body)
    message = 'Subject: {}\n\n{}'.format(subject, body).encode('utf-8')
    # print('mesage',message)
    email_text = """\
    From: %s
    To: %s
    Subject: %s
        %s
    """ % (sent_from, ", ".join(to), subject, body)
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to,message)
        # print('for loop run')
        print ("Email sent successfully!")

    except Exception as ex:
        print ("Something went wrong….",ex)
    
