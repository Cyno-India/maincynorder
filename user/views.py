from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import CustomerSerializer, UserSerializer
from .models import UserAccount

class RegisterView(APIView):
    def post(self, request):
        request_data = request.data
        request_data['role'] = 'admin'
        serializer = CustomerSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)

class CustomerRegisterView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user_id= request.user.id
        user_instance = UserAccount.objects.filter(id=user_id).values_list('role')[0][0]
        if user_instance == "admin":
          print(user_instance)
          # request_data = request.data
          request.data['role'] = 'customer'
          serializer = CustomerSerializer(data=request.data)
          serializer.is_valid(raise_exception=True)
          serializer.save()
          return Response(serializer.data , status=status.HTTP_201_CREATED)


  # def post(self, request):
  #   data = request.data

  #   serializer = UserCreateSerializer(data=data)

  #   if not serializer.is_valid():
  #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  #   user = serializer.create(serializer.validated_data)
  #   user = UserSerializer(user)

  #   return Response(user.data, status=status.HTTP_201_CREATED)


class RetrieveUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = request.user
    print(user)
    # u = UserAccount.objects.filter(id=user).values_list('role')[0][0]
    # print(u)
    # if u == "Customer":
    user = UserSerializer(user)

    return Response(user.data, status=status.HTTP_200_OK)
