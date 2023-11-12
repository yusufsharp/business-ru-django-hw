from django.shortcuts import render, redirect
from .forms import MyProfileForm
from .models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from . import models, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response


def index(request):
    # if request.method == 'POST':
    #     form = MyProfileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('study')
    #     else:
    #         errors = form.errors
    #         for field, error_list in errors.items():
    #             for error in error_list:
    #                 print(f"Ошибка в поле '{field}': {error}")

    context = {'form': MyProfileForm()}
    return render(request, 'myapp/index.html', context)

# @api_view(['GET', 'POST'])
# def index(request):
#     if request.method == 'GET':
#         return Response({'message': f'Hello, {request.data["text"]}'})
#     return Response({'message': 'Hello world'})


def study(request):
    last_user = User.objects.latest('id')
    age = last_user.calculate_age()
    return render(request, 'myapp/study.html', {'last_user': last_user, 'age': age})


class UserViewSet(ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()


class ItemAPIView(APIView):
    serializer_class = serializers.UserSerializer

    def get(self, request):
        items = models.User.objects.all()
        serializer = self.serializer_class(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return Response(status=status.HTTP_302_FOUND, headers={'Location': '/myapp/study/'})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
