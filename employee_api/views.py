from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import Employee
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated


class EmployeeApi(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
       
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):


        role = request.query_params.get('role')
        department = request.query_params.get('department')

        if id is not None:
            employee_data = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(employee_data)
            return Response(serializer.data)

        querySet = Employee.objects.all()

        if role:
            querySet = querySet.filter(role__iexact=role)

        if department:
            querySet=querySet.filter(department__iexact=department)


        paginator = PageNumberPagination()
        paginator.page_size = 10

        paginatorQry = paginator.paginate_queryset(querySet, request)
        serializer = EmployeeSerializer(paginatorQry, many=True)

        return paginator.get_paginated_response(serializer.data)

    def patch(self, request, id):

        try:
            employees = Employee.objects.get(id=id)
        except:
            return Response({'error': 'Check Emplyee ID, No Data Found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(
            employees, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):

        try:
            delete_employe = Employee.objects.get(id=id)
            delete_employe.delete()
            return Response({'success': 'User Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'error': 'No User found'}, status=status.HTTP_404_NOT_FOUND)

