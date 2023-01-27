from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

from .serializers import MemberSerializer # serializer 가져오기

# Create your views here.

class MemberRegisterView(
    mixins.CreateModelMixin,
    generics.GenericAPIView   
):
    serializer_class = MemberSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)



# class MemberRegisterView(APIView):
#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = make_password(request.data.get('password'))
#         tel = request.data.get('tel')
        
#         if Member.objects.filter(username=username).exists():    # 이미 있다면
#             return Response({
#                 'detail': 'Already used',
#             }, status=status.HTTP_400_BAD_REQUEST)
        
#         member = Member(
#             username = username,
#             password = password,
#             tel = tel,
#         )
        
#         member.save()        
#         return Response(status=status.HTTP_201_CREATED)