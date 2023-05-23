from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *

# Create your views here.
@api_view(['GET'])
def get_info(request):
    author_objs  = Author.objects.all()
    serializer = AuthorSerializers(author_objs, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def post_info(request):
    data = request.data
    serializer = AuthorSerializers(data=request.data)

    if not serializer.is_valid():
        return Response({'status': 403, 'messge':'something went wrong'})
    
    serializer.save()
    return Response({'status': 200, 'payload': data, 'messge':'you sent data'})