
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
from .function import tokennew, tokennewbom,weight

import re
from rest_framework import permissions, status



class ItemExcel(APIView):

    def get(self, request):
        new_data = tokennew()
        for i in new_data:
            no = i['No']
            Description = i['Description']
            Box_No = i['Box_No']
            AssemblyBOM = i['AssemblyBOM']
            Sales_Unit_of_Measure =i['Sales_Unit_of_Measure']
            Net_Weight = i['Net_Weight']
            # ItemCard.objects.all().delete()
            ItemCard.objects.create(No=no,Description=Description,Box_No=Box_No,AssemblyBOM=AssemblyBOM,Sales_Unit_of_Measure=Sales_Unit_of_Measure,Net_Weight=Net_Weight)
        print(new_data)

        return Response('hello')


class Bomtable(APIView):
    def get(self, request):
        new_data = tokennewbom()
        for i in new_data:
            Parent_Item_No = i['Parent_Item_No']
            No = i['No']
            Description = i['Description']
            AssemblyBOM = i['AssemblyBOM']
            Quantity_per = i['Quantity_per']
            Measure_code = i['Unit_of_Measure_Code']
            # print(Parent_Item_No,No,Description,AssemblyBOM,Quantity_per)
            # ItemCard.objects.all().delete()

            BomAssemblyTable.objects.create(Parent_Item_No=Parent_Item_No,No=No,Description=Description,AssemblyBOM=AssemblyBOM,Quantity_per=Quantity_per,unit_measure_code=Measure_code)
        return Response('hello')


class WeightTable(APIView):
    def get(self,request):
        # Weight.objects.all().delete()
        x = 122
        w = weight()
        
        new_data = [144]
        # for i in range(1000):
        #     x += 14
        #     new_data.append(x)
        new_amount = []
        for i in w :
            Document_No = i['Document_No']
            Line_No = i['Line_No']
            Courier_Channel = i['Courier_Channel']
            Country = i['Country']
            From_Weight = i['From_Weight']
            To_Weight = i['To_Weight']
            Amount = i['Amount']
            if Courier_Channel == "EMS" and Country == "HONG KONG":
                # print('Country',Country)
                # print('FROM',From_Weight)
                # print('TOO',To_Weight)

                # print('AMOUNTTT',Amount)
                new_amount.append(Amount)


                # Amount_new = Amount + 50
                # print('AMOUNTNEW',Amount_new)
                # Weight.objects.create(Document_No=Document_No,Line_No=Line_No,Courier_Channel=Courier_Channel,Country=Country,From_Weight=From_Weight,To_Weight=To_Weight,Amount=Amount)


            # print(x)

        # print(new_data)
        # for i in new_data:
        #     Weight.objects.create(C_num=i)
        # print(new_data)
                # Weight.objects.create(C_num=x)
            
                # Weight.objects.create(Document_No=Document_No,Line_No=Line_No,Courier_Channel=Courier_Channel,Country=Country,From_Weight=From_Weight,To_Weight=To_Weight,Amount=Amount)
        # fw = Weight.objects.get('C_num').first()
        # if fw:
        #     print(fw)
        # print(w)
        return Response('done')

    def post(self,request):
        # Weight.objects.all().delete()
        x = 122
        # w = weight()  
        w = list(Weight.objects.all().values_list())
        new_list = []
        new_ram_japan = []
        new_ems_japan = []
        for i in w:
            # print(i[0])
            if i[3] == "EMS" and i[4] == "HONG KONG":
                # print('HONG KONG',i[5],i[6],i[7])
                # new_list = []
                l  = i[7]
                new_list.append(l)
            elif i[3] == "RAM" and i[4] == "JAPAN":
                print('JAPAN',i[5],i[6],i[7])
                e = i[7]
                new_ram_japan.append(e)
            elif i[3] == "EMS" and i[4] == "JAPAN":
                print('JAPAN EMS',i[5],i[6],i[7])
                e = i[7]
                new_ems_japan.append(e)
            elif i[3] == "EMS" and i[4] == "CHINA":   
                print('CHINA',i[5],i[6],i[7])
                e = i[7]
                new_ram_japan.append(e)
            elif i[4] == "RAM" and i[4] == "S.KOREA":
                print('S.KOREA',i[5],i[6],i[7])
                e = i[7]
                new_ram_japan.append(e)

                # print((l))
        # print(new_list)
        res = [eval(i) for i in new_list]
        print(res)
        new=[]
        j=0
        for i in range(0,len(res)):
            j+=res[i]
            new.append(j)
        res = [eval(i) for i in new_list]
        print(res)
        new=[]
        j=0
        for i in range(0,len(res)):
            j+=res[i]
            new.append(j)
        print(new)
                



            # elif i[3] == "RAM" and i[4] == "JAPAN":
            #     print('JAPAN',i[5],i[6],i[7])
            # elif i[3] == "EMS" and i[4] == "JAPAN":
            #     print('JAPAN EMS',i[5],i[6],i[7])
            # elif i[3] == "EMS" and i[4] == "CHINA":   
            #     print('CHINA',i[5],i[6],i[7])
            # elif i[4] == "RAM" and i[4] == "S.KOREA":
            #     print('S.KOREA',i[5],i[6],i[7])


        new_data = [144]
        # for i in range(1000):
        #     x += 14
        #     new_data.append(x)


            # print(x)

        # print(new_data)
        # for i in new_data:
        #     Weight.objects.create(C_num=i)
        # print(new_data)
                # Weight.objects.create(C_num=x)
            
                # Weight.objects.create(Document_No=Document_No,Line_No=Line_No,Courier_Channel=Courier_Channel,Country=Country,From_Weight=From_Weight,To_Weight=To_Weight,Amount=Amount)
        # fw = Weight.objects.get('C_num').first()
        # if fw:
        #     print(fw)
        # print(w)
        return Response('done')
