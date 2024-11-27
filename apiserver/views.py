from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def index(request):
    data = {"result": "success", 
            "data": [{"id":"id", "이름":"itstudy"},
                     {"id":"nick", "이름":"adam"}]}
    return Response(data, status=status.HTTP_200_OK)