from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class FirstApi(APIView):

    def get(self,request):
        print(request.data)
        data=request.data
        return Response(data=data,status=status.HTTP_200_OK)
    
    def post(self,request):
        print(request.data)
        data=request.data
        return Response(data=data,status=status.HTTP_201_CREATED)

    def put(self,request):
        print(request.data)
        print(request.query_params.get('xyz'))
        data=request.data
        return Response(data=data,status=status.HTTP_205_RESET_CONTENT)

    def delete(self,request):
        print(request.data)
        print(request.query_params.get('xyz'))
        data = request.data
        return Response(data=data,status=status.HTTP_204_NO_CONTENT)
