import requests
import json
from datetime import date, datetime
import random
#set these values to retrieve the oauth token
crmorg = 'https://xxx.crm6.dynamics.com' #base url for crm org
clientid = '00000000-0000-0000-0000-000000000000' #application client id
username = 'xxxxxx@xxxxxxxx' #username
userpassword = 'xxxxxxxx' #password

tokenendpoint = 'https://login.microsoftonline.com/0dca7849-754b-4305-9e47-0b59350d40a6/oauth2/v2.0/token'

     
#build the authorization token request
def token():
    tokenendpoint = 'https://login.microsoftonline.com/0dca7849-754b-4305-9e47-0b59350d40a6/oauth2/v2.0/token'
    tokenpost = {
        'client_id':'b3c2bebb-1721-4e41-b65d-ea08a9f93b38',
        'client_secret':'q7S8Q~qhhD~n18P3UkzWA0Bqc8Cj49rPG9C1Obvr',
        'grant_type':'Client_Credentials',
        'scope':'https://api.businesscentral.dynamics.com/.default',
        # 'client_authentication':'Send as Basic Auth header',
    }
    
    #make the token request
    tokenres = requests.get(tokenendpoint, data=tokenpost)
    new_token= tokenres.json()
    return new_token['access_token']
# token()


def tokennew():
    tokenendpoint = f"https://api.businesscentral.dynamics.com/v2.0/0dca7849-754b-4305-9e47-0b59350d40a6/Sandbox1/ODataV4/Company('CYNO%20MEDICAMENTS')/Item_Card_Excel"
    access = token()
    headers = {
        'Authorization': 'Bearer ' + access
    }
    
    #make the token request
    tokenres = requests.get(tokenendpoint, headers=headers)
    new_token= tokenres.json()
    datap = []
    n = new_token['value']
    for i in n:
        No = i['No']
        Description = i['Description']
        Box_No = i['Box_No']
        AssemblyBOM = i['AssemblyBOM']
        Sales_Unit_of_Measure = i['Sales_Unit_of_Measure']
        Net_Weight = i['Net_Weight']
        # ItemCard.objects.create(No=No,Description=Description,Box_No=Box_No,AssemblyBOM=AssemblyBOM)
        # print('hello')
        data = {
            "No":No,
            "Description":Description,
            "Box_No":Box_No,
            "AssemblyBOM":AssemblyBOM,
            "Sales_Unit_of_Measure":Sales_Unit_of_Measure,
            "Net_Weight":Net_Weight,

        }
        datap.append(data)
    # print(datap)
    return datap
    # print(new_token['access_token'])

def tokennewbom():
    tokenendpoint = f"https://api.businesscentral.dynamics.com/v2.0/0dca7849-754b-4305-9e47-0b59350d40a6/Sandbox1/ODataV4/Company('CYNO%20MEDICAMENTS')/Assembly_BOM_Excel"
    access = token()
    headers = {
        'Authorization': 'Bearer ' + access
    }
    
    #make the token request
    tokenres = requests.get(tokenendpoint, headers=headers)
    new_token= tokenres.json()
    datap = []
    n = new_token['value']
    for i in n:
        Parent_Item_No = i['Parent_Item_No']
        No = i['No']
        Description = i['Description']
        AssemblyBOM = i['Assembly_BOM']
        Quantity_per = i['Quantity_per']
        Unit_of_Measure_Code = i['Unit_of_Measure_Code']

        # ItemCard.objects.create(No=No,Description=Description,Box_No=Box_No,AssemblyBOM=AssemblyBOM)
        # print('hello')
        data = {
            "Parent_Item_No":Parent_Item_No,
            "No":No,
            "Description":Description,
            "AssemblyBOM":AssemblyBOM,
            "Quantity_per":Quantity_per,
            "Unit_of_Measure_Code":Unit_of_Measure_Code


        }
        datap.append(data)
    # print(datap)
    return datap

def weight():
    tokenendpoint = f"https://api.businesscentral.dynamics.com/v2.0/0dca7849-754b-4305-9e47-0b59350d40a6/Sandbox1/ODataV4/Company('CYNO MEDICAMENTS')/FreightChargesSubform"
    access = token()
    headers = {
        'Authorization': 'Bearer ' + access
    }
    
    #make the token request
    tokenres = requests.get(tokenendpoint, headers=headers)
    new_token= tokenres.json()
    datap = []
    n = new_token['value']
    for i in n:
        Document_No = i['Document_No']
        Line_No = i['Line_No']
        Courier_Channel = i['Courier_Channel']
        Country = i['Country']
        From_Weight = i['From_Weight']
        To_Weight = i['To_Weight']
        Amount = i['Amount']
        # Weight.objects.create(Document_No=Document_No,Line_No=Line_No,Courier_Channel=Courier_Channel,Country=Country,From_Weight=From_Weight,To_Weight=To_Weight,Amount=Amount)
        print('hello')
        data = {
            "Document_No":Document_No,
            "Line_No":Line_No,
            "Courier_Channel":Courier_Channel,
            "Country":Country,
            "From_Weight":From_Weight,
            "To_Weight":To_Weight,
            "Amount":Amount,
        }
        datap.append(data)
    # print(datap)
# weight()
    return datap


def randomnum():
    number = random.randint(10000,99999)
    return number

def createsalesorders(country_nonbom,address_nonbom,phone_nonbom,email_nonbom,consignee_nonbom,filename,itemId):
    # tokenendpoint = f"https://api.businesscentral.dynamics.com/v2.0/0dca7849-754b-4305-9e47-0b59350d40a6/Sandbox1/api/v2.0/salesOrders"
    tokenendpoint = f"https://api.businesscentral.dynamics.com/v2.0/0dca7849-754b-4305-9e47-0b59350d40a6/sandbox1/api/nimbus/customSalesOrder/v2.0/companies(7ba725d8-d449-ec11-9f08-6045bd7303c7)/customSalesOrders"

    # tokenendpoint = f"https://api.businesscentral.dynamics.com/v2.0/0dca7849-754b-4305-9e47-0b59350d40a6/Sandbox1/api/v2.0/salesOrders"
    access = token()
    custdate = datetime.today().date().strftime(f"%Y-%m-%d")
    print(custdate)
    number = random.randint(10000,99999)
    new_num = 10 + number
    print('numNON',number)
    print('HEEEEEEELLLLLLLOOOOOOO',filename,itemId)
    headers = {
        'Authorization': 'Bearer ' + access
    }
    data =  {
        "number":f"PRA{number}",
        "orderDate": custdate,
        "customerNumber": "MA",
        "shipToName":consignee_nonbom,
        "currencyCode": "USD",
        "sellToAddressLine1":f"{country_nonbom.capitalize()},{country_nonbom.capitalize()}",
        "sellToAddressLine2":f"{address_nonbom}",
        "sellToCity":f"{country_nonbom}",
        "phoneNumber":f"{phone_nonbom}",
        "email":f"{email_nonbom}",
        "sheetName":str(filename),
        "actualItem":str(itemId),
        "paymentTermsId": "00000000-0000-0000-0000-000000000000"
    }
    print(data)
       
    #make the token request
    tokenres = requests.post(tokenendpoint, headers=headers,json=data)
    new_token= tokenres.json()
    # new_data = new_token['id']
    return new_token['id']
    # print(new_token)
    # return new_data
def createsalesordersbom(country,address,phone,email,consignee,filename,itemId):
    # tokenendpoint = f"https://api.businesscentral.dynamics.com/v2.0/0dca7849-754b-4305-9e47-0b59350d40a6/Sandbox1/api/v2.0/salesOrders"
    tokenendpoint = f"https://api.businesscentral.dynamics.com/v2.0/0dca7849-754b-4305-9e47-0b59350d40a6/sandbox1/api/nimbus/customSalesOrder/v2.0/companies(7ba725d8-d449-ec11-9f08-6045bd7303c7)/customSalesOrders"
    access = token()
    custdate = datetime.today().date().strftime(f"%Y-%m-%d")
    print(custdate)
    number = random.randint(10000,99999)
    print('num',number)
    print('HEEEEEEELLLLLLLOOOOOOO ---- 2222',filename,itemId)

    new_num = 10 + number
    headers = {
        'Authorization': 'Bearer ' + access
    }
    data =  {
        "number":f"PRABOM{number}",
        "orderDate": custdate,
        "customerNumber": "MA",
        "currencyCode": "USD",
        "sellToAddressLine1":f"{country.capitalize()},{country.capitalize()}",
        "sellToAddressLine2":address,
        "sellToCity":country,
        "phoneNumber":phone,
        "email":email,
        "shipToName":consignee,
        "sheetName":str(filename),
        "actualItem":str(itemId),
        "paymentTermsId": "00000000-0000-0000-0000-000000000000"
    }
    print(data)
       
    #make the token request
    tokenres = requests.post(tokenendpoint, headers=headers,json=data)
    new_token= tokenres.json()
    # new_data = new_token['id']
    print(new_token['id'])
    return new_token['id']
# createsalesorders()

def getnonbomorder(desc,quan,unit,box,country_nonbom,address_nonbom,phone_nonbom,email_nonbom,consignee_nonbom,filename,newl,itemId):
    new_data = createsalesorders(country_nonbom,address_nonbom,phone_nonbom,email_nonbom,consignee_nonbom,filename,itemId)
    print('obtained id',new_data)
    print(desc,quan,unit)
    number = random.randint(10000,99999)
    tokenendpoint = f"https://api.businesscentral.dynamics.com/v2.0/0dca7849-754b-4305-9e47-0b59350d40a6/Sandbox1/api/v2.0/salesOrders({new_data})/salesOrderLines"
    access = token()
    print('reached')
    headers = {
        'Authorization': 'Bearer ' + access
    }
    # data =   {
    #     "sequence": 10000,
    #     "lineType": "Item",
    #     "description": desc,
    #     "unitOfMeasureCode": unit,
    #     "quantity": int(quan)
    # }
    json  = {
                "sequence": 10000,
                "lineType": "Item",
                "description": desc,
                "unitOfMeasureCode": unit,
                "quantity":int(quan),   
                
            }
    print(json)
    jdata =   {
        "lineType": "Account",
        "lineObjectNumber": "30002158",
        "description": "Freight on shipments",
        "quantity": 1,
        "unitPrice": int(newl),
    }
    print(jdata)
    data =   {
        "sequence": 30000,
        "lineType": "Item",
        "lineObjectNumber": box,
        "description":  box,
        "quantity": 1,
    }
   
   

    # print(json1)
    # data = {
    #     "sequence": 10000, 
    #     'lineType': 'Item', 
    #     'description': 'LECOURSE500MG 10TABS (1X1X10)',
    #     'unitOfMeasureCode': 'TAB', 
    #     'quantity': '1'
    # }
    print(data)
       
    #make the token request
    tokenres = requests.post(tokenendpoint, headers=headers,json=json)
    new_token= tokenres.json()
    print('NOOOOON BOOOM',new_token)
    tokenres1 = requests.post(tokenendpoint, headers=headers,json=jdata)
    new_token1= tokenres1.json()
    print('NOOOOON BOOOM',new_token1)
    tokenres2 = requests.post(tokenendpoint, headers=headers,json=data)
    new_token2= tokenres2.json()
    print('NOOOOON BOOOM',new_token2)
    # return new_token

def getsalesorders(desc,quan,unit,bom_box,country,address,phone,email,consignee,newl,filename,itemId):
    new_data = createsalesordersbom(country,address,phone,email,consignee,filename,itemId)
    print('obtained id bom',new_data)
    print(desc,quan,unit)
    number = random.randint(10000,99999)
   
    tokenendpoint = f"https://api.businesscentral.dynamics.com/v2.0/0dca7849-754b-4305-9e47-0b59350d40a6/Sandbox1/api/v2.0/salesOrders({new_data})/salesOrderLines"
    print(tokenendpoint)
    access = token()
    headers = {
        'Authorization': 'Bearer ' + access,
        'Content-Type'	:'application/json'
    }
    # json =   {
    # #     "sequence": 10000,
    # #     "lineType": "Item",
    # #     "description": desc,
    # #     "unitOfMeasureCode": unit,
    # #     "quantity":int(quan)
        
    # # }
    # }

    json = {
            "sequence": 10000,
            "lineType": "Item",
            "description": desc,
            "unitOfMeasureCode": unit,
            "quantity":int(quan),
                
    }        

    print(json)
    jdata =   {
        "lineType": "Account",
        "lineObjectNumber": "30002158",
        "description": "Freight on shipments",
        "quantity": int(quan),
        "unitPrice": int(newl),

    }
    data =   {
        "sequence": 30000,
        "lineType": "Item",
        "lineObjectNumber": bom_box,
        "description": bom_box,
        "quantity": int(quan),
    }
    
    
    #make the token request
    tokenres = requests.post(tokenendpoint, headers=headers,json=json)
    print(tokenres)
    new_token= tokenres.json()
    print('BOOOM',new_token)
    tokenres1 = requests.post(tokenendpoint, headers=headers,json=jdata)
    print(tokenres1)
    new_token1= tokenres1.json()
    print('20000BOOOM',new_token1)
    tokenres2 = requests.post(tokenendpoint, headers=headers,json=data)
    print(tokenres2)
    new_token2= tokenres2.json()
    print('20000BOOOM',new_token2)

# getsalesorders()
    # datap = []
    # n = new_token['value']
    # for i in n:
    #     Parent_Item_No = i['Parent_Item_No']
    #     No = i['No']
    #     Description = i['Description']
    #     AssemblyBOM = i['Assembly_BOM']
    #     Quantity_per = i['Quantity_per']
    #     Unit_of_Measure_Code = i['Unit_of_Measure_Code']

    #     # ItemCard.objects.create(No=No,Description=Description,Box_No=Box_No,AssemblyBOM=AssemblyBOM)
    #     # print('hello')
    #     data = {
    #         "Parent_Item_No":Parent_Item_No,
    #         "No":No,
    #         "Description":Description,
    #         "AssemblyBOM":AssemblyBOM,
    #         "Quantity_per":Quantity_per,
    #         "Unit_of_Measure_Code":Unit_of_Measure_Code


    #     }
    #     datap.append(data)
    # # print(datap)
    # return datap