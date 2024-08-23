from rest_framework.viewsets import ModelViewSet
from ..models import Post
from .serializer import PostSerializer
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets, filters, generics, permissions
from django.core.files.storage import default_storage

# @api_view(['POST'])
# @parser_classes([MultiPartParser, FormParser])
# def upload_image(request):
#     if 'file' not in request.data:
#         return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)
    
#     file = request.data['file']
#     file_name = default_storage.save(file.name, file)
#     file_url = default_storage.url(file_name)

#     return Response({"file_url": file_url}, status=status.HTTP_201_CREATED)

# class PostViewSet(ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)